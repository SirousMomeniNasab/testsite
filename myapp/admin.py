from django.contrib import admin
from .models import Article, Category, IPAddress
from django.contrib import messages
from django.utils.translation import ngettext


# Register your models here.

# Admin header change shortcut
admin.site.site_header = 'مدیریت سایت'


# django admin actions for articles

@admin.action(description="انتشار مقالات انتخاب شده")
def make_published(modeladmin, request, queryset):
    updated = queryset.update(status="p")
    modeladmin.message_user(
        request,ngettext("%d  مقاله منتشر شد. ", "%d مقاله منتشر شدند. ", updated,) % updated, messages.SUCCESS,)

@admin.action(description="پیش نویس مقالات انتخاب شده")
def make_draft(modeladmin, request, queryset):
    updated = queryset.update(status="d")
    modeladmin.message_user(
        request,ngettext("%d  مقاله پیش نویس شد. ", "%d مقاله پیش نویس شدند. ", updated,) % updated, messages.SUCCESS,)
    
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','thumbnail_tag', 'slug', 'author','jpublish','is_special', 'status', 'category_to_str')
    list_filter = ('publish','status', 'author')
    search_fields = ('title','description')
    prepopulated_fields = {"slug": ["title"]}
    ordering = ['-status','-publish']
    actions = [make_published, make_draft]

admin.site.register(Article, ArticleAdmin)


# django admin actions for categories

@admin.action(description="فعال کردن دسته بندی های انتخاب شده")
def make_active(modeladmin, request, queryset):
    updated = queryset.update(status=True)
    modeladmin.message_user(
        request,ngettext("%d  دسته بندی فعال شد. ", "%d دسته بندی فعال  شدند. ", updated,) % updated, messages.SUCCESS,)

@admin.action(description="غیرفعال کردن دسته بندی های انتخاب شده")
def make_deactive(modeladmin, request, queryset):
    updated = queryset.update(status=False)
    modeladmin.message_user(
        request,ngettext("%d  دسته بندی غیرفعال شد. ", "%d دسته بندی غیرفعال  شدند. ", updated,) % updated, messages.SUCCESS,)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title','slug', 'parent','status')
    list_filter = (['status'])
    search_fields = ('title','slug')
    prepopulated_fields = {"slug": ["title"]}
    actions = [make_active, make_deactive]

admin.site.register(Category, CategoryAdmin)


admin.site.register(IPAddress)
