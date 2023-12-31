from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog.models import Post


class PostListView(ListView):
    """Альтернативное вывод списка постов"""
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


# Create your views here.
# def post_list (request):
#     posts_list = Post.published.all()
#     paginator = Paginator(posts_list, 2)
#     page_number = request.GET.get('page', 1)
#     posts = paginator.get_page(page_number)
#     return render(request, 'blog/post/list.html', {"posts": posts})


def post_detail (request, post, year, month, day):
    post = get_object_or_404(Post,
                             slug = post,
                             publish__year = year,
                             publish__month = month,
                             publish__day = day,
                             status = Post.Status.PUBLISHED)
    return render(request, "blog/post/detail.html", {'post': post})
