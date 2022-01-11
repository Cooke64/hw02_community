from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    prepopulated_fields = {"slug": ("title",)}
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="posts")
    group = models.ForeignKey(
        'Group',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )


class Group(models.Model):
    title = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    prepopulated_fields = {"slug": ("title",)}

    def __str__(self):
        return self.title
