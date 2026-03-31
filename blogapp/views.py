from django.shortcuts import render,redirect
from .models import Blog
from django.contrib.auth.decorators import login_required

@login_required
def addBlogView(request):
    if(request.method=="POST"):
        title=request.POST.get("title")
        description=request.POST.get("description")
        blog_image = request.FILES.get("blog_image")
        blog=Blog()
        blog.title=title
        blog.description=description
        blog.blog_image=blog_image
        blog.user=request.user
        blog.save()
        return redirect("/home")
    else:
        return render(request, "blogform.html")
    
@login_required
def viewBlog(request, blog_id):
    blog=Blog.objects.get(id=blog_id)
    return render(request,"blog.html",{"blog":blog})

@login_required
def myblogView(request):
    blogs=Blog.objects.filter(user=request.user)
    return render(request,"myblog.html",{"blogs":blogs})

@login_required
def searchBlogView(request):
    q=request.GET.get("q")
    blogs=Blog.objects.filter(description__icontains=q)
    return render(request,"home.html",{"user":request.user,"blogs":blogs})

@login_required
def editBlogView(request, edit_id):
    blog = Blog.objects.get(id=edit_id)
    if request.method == "POST":
        blog.title = request.POST.get("title")
        blog.description = request.POST.get("description")
        if request.FILES.get("blog_image"): #checks:Did the user upload a new image?
            blog.blog_image = request.FILES.get("blog_image") #If they upload a new one:Then the image is updated.
            blog.save()
            return redirect("/home")
    return render(request, "editblog.html", {"blog": blog})

@login_required
def deleteBlogView(request,del_id):
    blog=Blog.objects.get(id=del_id)
    blog.delete()
    return redirect("/my-blogs")