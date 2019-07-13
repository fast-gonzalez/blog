from django.views.generic.list import ListView

from blog.models import Article


class IndexListView(ListView):
    model = Article
    template_name = 'blog/index.html'