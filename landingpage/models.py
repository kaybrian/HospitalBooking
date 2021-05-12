from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from django.template.defaultfilters import slugify



class Blog(models.Model):
    title = models.CharField(max_length=550, blank=False)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True, unique_for_date="created_at", blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="posts/images/", null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-created_at']
    
