from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from myapp.models import Article

# FieldsMixin for CRUD operations
class FieldsMixin():
    def dispatch(self, request, *args, **kwargs):
        self.fields = ["title", "slug", 
                       "category", "description", "thumbnail", 
                       "publish", "is_special", "status", ]
        if request.user.is_superuser:
            self.fields.append("author")
        return super().dispatch(request, *args, **kwargs)
    

class FormValidMixin():
    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
            if not self.obj.status == 'l':
                self.obj.status = 'd'
        return super().form_valid(form)
    
# access for one author
class AuthorAccessMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        if article.author == request.user and article.status in ['b', 'd'] or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You Can't See This Page!")
        
# access for all authors 
class AuthorsAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.is_author:
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect("account:profile")
        else:
            return redirect("login")
        

class SuperUserAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You Can't See This Page!")

        

    

    