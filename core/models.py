from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse

from django.template.loader import render_to_string

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from ckeditor.fields import RichTextField

from bs4 import BeautifulSoup


class AbstractPost(models.Model):
    class Meta:
        abstract = True

    category = None

    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, blank=True)

    author = models.CharField('written by', max_length=120)

    published_at = models.DateTimeField(auto_now_add=True)

    text = None

    # For use in the list view
    preview = models.CharField(max_length=240)

    comments = GenericRelation('Comment')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={
                'category_slug': self.category,
                'post_slug': self.slug,
                },
            )

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
        self.refresh_from_db()
        if not self.slug or \
                self.__class__.objects.filter(slug=self.slug).exists():
            self.slug = self._get_unique_slug()
        self.preview = self._get_preview()  # Always recalculate preview
        return super().save(*args, **kwargs)


class Post(AbstractPost):
    CATEGORIES = ['blog', 'stories']

    category = models.CharField(
        max_length=80,
        choices=(
            ('blog', 'Blog'),
            ('stories', 'Stories'),
        ),
    )

    text = RichTextField()


class HTMLPost(AbstractPost):
    class Meta:
        verbose_name = "HTML post"
        verbose_name_plural = "HTML posts"

    CATEGORIES = ['cribbage']  # Default to Post

    category = models.CharField(
        max_length=80,
        choices=(
            ('cribbage', 'Cribbage'),
        )
    )

    template_name = models.CharField(max_length=255)

    @property
    def text(self):
        return render_to_string(self.template_name)


class Comment(models.Model):
    author = models.CharField(max_length=40)
    text = models.TextField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
