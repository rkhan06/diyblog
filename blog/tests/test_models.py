from django.test import TestCase
from blog.models import Blog, Author, Comment
from django.contrib.auth.models import User
from datetime import date


class BlogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        new_user = User.objects.create(username="bob", password="builder")
        author = Author.objects.create(user=new_user, bio="asd")
        Blog.objects.create(title='breaking news',
                            author=author, blog_post="iphone 11 is out !",
                            post_date=date.today())

    def test_title_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_title_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_blog_post_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('blog_post').max_length
        self.assertEquals(max_length, 1000)

    def test_get_absolute_url(self):
        blog = Blog.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(blog.get_absolute_url(), '/blog/blog/1')


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        new_user = User.objects.create(username="bob", password="builder")
        Author.objects.create(user=new_user, bio="hi i am bob the builder")

    def test_author_bio_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('bio').max_length
        self.assertEquals(max_length, 500)

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        self.assertEquals(author.get_absolute_url(), '/blog/blogger/1')


class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        new_user = User.objects.create(username="bob", password="builder")
        author = Author.objects.create(
            user=new_user, bio="hi i am bob the builder")
        blog = Blog.objects.create(title='breaking news',
                                   author=author, blog_post="iphone 11 is out !",
                                   post_date=date.today())
        Comment.objects.create(
            comment_text="cool", commenter=new_user, blog=blog, post_date=date.today())

    def test_comment_text_max_length(self):
        comment = Comment.objects.get(id=1)
        max_length = comment._meta.get_field('comment_text').max_length
        self.assertEquals(max_length, 500)
