from django.urls import path
from .views import (ArticleList, ArticleDetail,
                     CateogryList, AuthorList, 
                     ArticleDetailPreview,SearchList)

app_name='myapp'
urlpatterns = [
    path('', ArticleList.as_view(), name='home'),
    path('article/<slug:slug>',ArticleDetail.as_view(), name='article_detail'),
    path('preview/<int:pk>',ArticleDetailPreview.as_view(), name='preview'),
    path('category/<slug:slug>',CateogryList.as_view(), name='category'),
    path('author/<slug:username>',AuthorList.as_view(), name='author'),

    path('search/', SearchList.as_view(), name='search'),
    path('search/page/<int:page>', SearchList.as_view(), name="search")

]
