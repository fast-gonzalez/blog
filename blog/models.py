from django.db import models
from django.utils.text import slugify


class Article(models.Model):
    title = models.CharField(max_length=128)
    pub_date = models.DateTimeField('date published')
    content = models.TextField()
    slug = models.SlugField(max_length=128)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Article, self).save(*args, **kwargs)

    @property
    def short(self):
        return self.content.split('\n\n')[0]