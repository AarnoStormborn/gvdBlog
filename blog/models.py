from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, null=True)
    content = RichTextField()
    image = models.ImageField(upload_to='post/')
    meta_description = models.CharField(max_length=400, help_text="Short description for blog")
    meta_keywords = models.CharField(max_length=250, help_text="Add comma separated keywords for the blog")
    slug = models.SlugField(default='', null=False, editable=False, max_length=200)
    publish_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('post-detail', kwargs)

    class Meta:
        verbose_name_plural = 'Blog Post'

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class BlogComment(models.Model):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    comment = models.TextField(max_length=1200)
    show_comment = models.BooleanField(default=False)
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Blog Comment'
