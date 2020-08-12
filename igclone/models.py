from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.
class Post(models.Model):
    caption = models.TextField()
    date_posted = models.DateTimeField(auto_now_add = True)
    article_image = models.ImageField(upload_to = 'articles/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name = 'blog_posts')
    
    def __str__(self):
        return self.article_image
    

    def save(self):
        super().save()

        img = Image.open(self.article_image.path)

        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.article_image.path)

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk': self.pk})
    
    def total_likes(self):
        return self.likes.count()

class Follow(models.Model):
    follower = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='following')
    followed = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default=None)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s - %s' % (self.post.article_image, self.name)

    class Meta:
        pass

    def get_absolute_url(self):
        return u'/post/%d' % self.id



