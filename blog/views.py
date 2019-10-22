from django.shortcuts import render
from django.shortcuts import get_object_or_404
from blog.models import Author, Blog, Comment
from django.http import HttpResponseRedirect
from blog.forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def index(request):
    num_blogs = Blog.objects.count()
    num_bloggers = Author.objects.count()
    num_comments = Comment.objects.count()

    context = {
        'num_blogs': num_blogs,
        'num_bloggers': num_bloggers,
        'num_comments': num_comments
    }
    return render(request, 'index.html', context=context)


def blogList(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/blog_list.html', context=context)


def blogDetail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    comments = Comment.objects.filter(blog=blog)

    if request.method == 'POST':
        # form = blogComment(request.POST)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = Comment()
            comment.comment_text = form.save(commit=False)
            comment.blog = blog
            comment.commenter = request.user
            comment.save()
            return HttpResponseRedirect(reverse('blog:blog-detail', kwargs={'pk': pk}))
    else:
        comment_form = CommentForm()

    context = {
        'blog': blog,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(request, 'blog/blog_details.html', context=context)


def bloggersList(request):
    bloggers = Author.objects.all()
    context = {
        'bloggers': bloggers
    }
    return render(request, 'blog/bloggers_list.html', context=context)


def bloggerDetail(request, bloggerId):
    blogger = get_object_or_404(Author, pk=bloggerId)
    blogs = Blog.objects.filter(author=blogger)

    context = {
        'blogger': blogger,
        'blogs': blogs
    }
    return render(request, 'blog/blogger_detail.html', context=context)
