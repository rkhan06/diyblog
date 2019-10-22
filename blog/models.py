from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=500, help_text='enter bio', null=True)

    class Meta():
        ordering = ['user', 'bio']

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('blog:blogger-details', args=[str(self.id)])


class Blog(models.Model):
    title = models.CharField(
        max_length=200, help_text='Title for the blog post')
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    post_date = models.DateField(null=False, blank=False)
    blog_post = models.TextField(max_length=1000, help_text='write your blog')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog-detail', args=[str(self.id)])


class Comment(models.Model):
    comment_text = models.TextField(
        max_length=500, help_text='Enter a comment')
    post_date = models.DateTimeField(auto_now_add=True)
    commenter = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta():
        ordering = ['-post_date']

    def __str__(self):
        return self.comment_text
