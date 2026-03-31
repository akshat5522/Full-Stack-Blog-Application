from django.contrib import admin
from django.urls import path
from userapp.views import *
from blogapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",registerView),
    path("home",homeView),
    path("accounts/login/",loginView),
    path("accounts/logout/",logoutView),
    path("add-blog",addBlogView),
    path("blogs/<int:blog_id>",viewBlog),
    path("my-blogs",myblogView),
    path("search",searchBlogView),
    path("edit-blog/<int:edit_id>",editBlogView),
    path("delete-blog/<int:del_id>",deleteBlogView),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
