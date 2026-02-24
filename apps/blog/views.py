# /home/cs/Desktop/PROJECTS/kcihh_website/apps/blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.contrib import messages
from django.utils import timezone
from hitcount.views import HitCountDetailView
from hitcount.models import HitCount
from .models import Post, Category, Comment
from .forms import CommentForm

def blog_list(request):
    """View for listing all published blog posts"""
    # Get all published posts
    posts = Post.objects.filter(published=True, published_date__lte=timezone.now())
    
    # Get featured post (if any)
    featured_post = posts.filter(featured=True).first()
    
    # Get all categories with post counts
    categories = Category.objects.annotate(
        post_count=Count('posts', filter=Q(posts__published=True))
    )
    
    # Get popular tags (you might want to implement this differently)
    popular_tags = Post.tags.most_common()[:8]
    
    # Search functionality
    search_query = request.GET.get('q')
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) |
            Q(summary__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(author__first_name__icontains=search_query) |
            Q(author__last_name__icontains=search_query) |
            Q(tags__name__icontains=search_query)
        ).distinct()
    
    # Category filter
    category_slug = request.GET.get('category')
    if category_slug:
        posts = posts.filter(category__slug=category_slug)
    
    # Tag filter
    tag_name = request.GET.get('tag')
    if tag_name:
        posts = posts.filter(tags__name__iexact=tag_name)
    
    # Order by published date (newest first)
    posts = posts.order_by('-published_date')
    
    # Pagination
    paginator = Paginator(posts, 9)  # Show 9 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'posts': page_obj,
        'featured_post': featured_post,
        'categories': categories,
        'popular_tags': popular_tags,
        'search_query': search_query,
        'selected_category': category_slug,
        'selected_tag': tag_name,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
    }
    return render(request, 'blog/index.html', context)


class BlogDetailView(HitCountDetailView):
    """View for individual blog post with hit counting"""
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    count_hit = True  # This enables hit counting
    
    def get_queryset(self):
        # Only show published posts
        return Post.objects.filter(published=True, published_date__lte=timezone.now())
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get related posts (same category or tags)
        post = self.get_object()
        
        # Related by category
        related_by_category = Post.objects.filter(
            category=post.category, 
            published=True
        ).exclude(id=post.id)[:3]
        
        # Related by tags (if not enough by category)
        if related_by_category.count() < 3:
            tags = post.tags.all()
            related_by_tags = Post.objects.filter(
                tags__in=tags,
                published=True
            ).exclude(id=post.id).exclude(
                id__in=related_by_category.values_list('id', flat=True)
            ).distinct()[:3 - related_by_category.count()]
            
            context['related_posts'] = list(related_by_category) + list(related_by_tags)
        else:
            context['related_posts'] = related_by_category
        
        # Get previous and next posts
        context['prev_post'] = Post.objects.filter(
            published=True,
            published_date__lt=post.published_date
        ).order_by('-published_date').first()
        
        context['next_post'] = Post.objects.filter(
            published=True,
            published_date__gt=post.published_date
        ).order_by('published_date').first()
        
        # Get approved comments
        context['comments'] = post.comments.filter(approved=True)
        
        # Initialize comment form
        context['comment_form'] = CommentForm()
        
        return context
    
    def post(self, request, *args, **kwargs):
        """Handle comment submission"""
        self.object = self.get_object()
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.save()
            messages.success(request, 'Your comment has been submitted and is awaiting approval.')
            return redirect('blog:blog_detail', slug=self.object.slug)
        
        # If form is invalid, re-render the page with form errors
        context = self.get_context_data(object=self.object)
        context['comment_form'] = form
        return self.render_to_response(context)


# Alias for URL reverse
blog_detail = BlogDetailView.as_view()


def blog_category(request, category_slug):
    """View for posts filtered by category"""
    category = get_object_or_404(Category, slug=category_slug)
    
    posts = Post.objects.filter(
        category=category,
        published=True,
        published_date__lte=timezone.now()
    ).order_by('-published_date')
    
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'posts': page_obj,
        'category': category,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
    }
    return render(request, 'blog/category.html', context)


def blog_tag(request, tag_slug):
    """View for posts filtered by tag"""
    posts = Post.objects.filter(
        tags__slug=tag_slug,
        published=True,
        published_date__lte=timezone.now()
    ).order_by('-published_date')
    
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'posts': page_obj,
        'tag': tag_slug,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
    }
    return render(request, 'blog/tag.html', context)


def blog_search(request):
    """View for search results (can be combined with blog_list)"""
    query = request.GET.get('q', '')
    
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(summary__icontains=query) |
            Q(content__icontains=query) |
            Q(author__first_name__icontains=query) |
            Q(author__last_name__icontains=query) |
            Q(tags__name__icontains=query)
        ).filter(published=True, published_date__lte=timezone.now()).distinct()
    else:
        posts = Post.objects.none()
    
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'posts': page_obj,
        'query': query,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
    }
    return render(request, 'blog/search.html', context)


def blog_archive(request, year, month=None):
    """View for archive by date"""
    if month:
        posts = Post.objects.filter(
            published_date__year=year,
            published_date__month=month,
            published=True
        ).order_by('-published_date')
    else:
        posts = Post.objects.filter(
            published_date__year=year,
            published=True
        ).order_by('-published_date')
    
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'posts': page_obj,
        'year': year,
        'month': month,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
    }
    return render(request, 'blog/archive.html', context)