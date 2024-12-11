from django.views.generic import ListView, DeleteView
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from account.models import User
from account.mixins import AuthorAccessMixin
from django.db.models import Q





# generic display Views: ListView, DeleteView

# Model >> ArticleList get data from Article model
# View >> ArticleList is list of articles
# Template >> home.html

# ArticleList is for show list of articles in home page
class ArticleList(ListView):
    # model = Article
    # context_object_name = "articles"
    queryset = Article.objects.published()
    template_name = "myapp/home.html"
    paginate_by = 2

class ArticleDetail(DeleteView):
    template_name = "myapp/article_detail.html"

    def get_object(self):
        slug = self.kwargs.get('slug')
        article = get_object_or_404(Article.objects.published(), slug=slug)
        ip_address = self.request.user.ip_address
        if ip_address not in article.hits.all():
            article.hits.add(ip_address)
        return article
     
# see preview of article before publish in website
class ArticleDetailPreview(AuthorAccessMixin,  DeleteView):
    template_name = "myapp/article_detail.html"

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk)
    

# paginator for articles and categories
'''def category(request, slug):
    category = get_object_or_404(Category, slug=slug, status=True)
    articles_list = category.articles.published()
    paginator = Paginator(articles_list, 2)  # Show 2 article per page.
    page_number = request.GET.get("page")
    articles = paginator.get_page(page_number)

    context = {
        "category": category,
        "articles": articles,
    }
    return render(request, 'myapp/category.html', context)
''' 

class CateogryList(ListView):
    template_name = "myapp/category.html"
    paginate_by = 2
    def get_queryset(self):
        global category # for next function
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.published()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context
    

class AuthorList(ListView):
    template_name = "myapp/author.html"
    paginate_by = 2
    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User ,username=username)
        return author.articles.published()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context
    

#search box
class SearchList(ListView):
    template_name = "myapp/search_list.html"
    paginate_by = 2
    def get_queryset(self):
        search = self.request.GET.get('q')
        return Article.objects.filter(Q(description__icontains=search) | Q(title__icontains=search))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q')
        return context