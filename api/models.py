from django.db import models


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(default='')
    title = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)


    class Meta:
        ordering = ['created']


class Comments(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)


    class Meta:
        ordering = ['created']


class Categories(models.Model):
    category_title = models.CharField(max_length=250)
    owner = models.ForeignKey('auth.User', related_name='category', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='category', on_delete=models.CASCADE)


