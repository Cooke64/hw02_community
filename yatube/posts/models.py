from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="posts")
    group = models.ForeignKey(
        'Group',
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )


class Group(models.Model):
    title = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    prepopulated_fields = {"slug": ("title",)}

    def __str__(self, title):
        return self.title
