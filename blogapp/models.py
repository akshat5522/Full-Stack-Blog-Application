from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Blog(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    # blog_image=models.ImageField(upload_to="blog_images/")
    blog_image=CloudinaryField('image', blank=True, null=True, help_text="Featured image for the blog")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        db_table="blogs"