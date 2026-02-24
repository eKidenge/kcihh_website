# apps/blog/models.py
from django.db import models
from django.conf import settings  # use this for custom user model
from tinymce.models import HTMLField
from django.utils.text import slugify
from taggit.managers import TaggableManager

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('explainers', 'Climate Explainers'),
        ('spotlight', 'Community Spotlight Stories'),
        ('innovation', 'Innovation Features'),
        ('youth_voices', 'Youth Voices & Opinion Pieces'),
        ('indigenous', 'Indigenous Knowledge Reflections'),
        ('events', 'Event Reports & Announcements'),
    ]
    
    category_type = models.CharField(max_length=20, choices=CATEGORY_CHOICES, unique=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # reference custom user model
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts'
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = TaggableManager()
    featured_image = models.ImageField(upload_to='blog/')
    summary = models.TextField(max_length=300)
    content = HTMLField()
    video_url = models.URLField(blank=True)
    
    # Metadata
    featured = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    # SEO
    meta_description = models.CharField(max_length=160, blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True)
    
    # Statistics
    views = models.IntegerField(default=0)
    read_time = models.IntegerField(help_text="Reading time in minutes", default=5)
    
    class Meta:
        ordering = ['-published_date']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog_detail', args=[self.slug])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_date']
    
    def __str__(self):
        return f"Comment by {self.name} on {self.post}"