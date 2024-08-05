from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name="Category name", max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return str(self.name)


class Tag(models.Model):
    name = models.CharField(verbose_name="Tag name", max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return str(self.name)


class Post(models.Model):
    title = models.CharField(verbose_name="Post title", max_length=200)
    body = models.TextField(verbose_name="Post body")
    author = models.CharField(verbose_name="Author", default="admin", max_length=100)
    publish_date = models.DateTimeField(verbose_name="publish date", auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="category")
    tags = models.ManyToManyField(Tag)
    published = models.BooleanField(default=True)
    on_top = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    author = models.CharField(verbose_name="comment author", max_length=100, blank=False)
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return str(self.author)


class Rating(models.Model):
    post = models.ForeignKey(Post,on_delete=models.PROTECT, related_name="ratings")
    value = models.PositiveIntegerField(verbose_name="Post rating", default=0)

    def __str__(self):
        return str(self.value)
