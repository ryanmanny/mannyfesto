from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse

from ckeditor.fields import RichTextField

from bs4 import BeautifulSoup


# Create your models here.
class Post(models.Model):
    class Meta:
        abstract = True

    detail_view_name = None

    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, blank=True)

    text = RichTextField()

    # For use in the list view
    preview = models.CharField(max_length=240)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(self.detail_view_name, kwargs={'slug': self.slug})

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while self.__class__.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    def _get_preview(self):
        html = self.text
        preview = BeautifulSoup(html, 'lxml').text
        return preview

    def save(self, *args, **kwargs):
        if not self.slug or \
                self.__class__.objects.filter(slug=self.slug).exists():
            self.slug = self._get_unique_slug()
        self.preview = self._get_preview()  # Always recalculate preview
        return super().save(*args, **kwargs)


class BlogPost(Post):
    detail_view_name = 'blog_post'

    parent = models.ForeignKey(
        'self',
        related_name='children',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    @property
    def siblings(self):
        return self.parent.children.exclude(pk=self.pk)


class Story(Post):
    class Meta:
        verbose_name_plural = 'stories'

    detail_view_name = 'story'
