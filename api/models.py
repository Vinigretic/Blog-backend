from django.db import models


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(default='')
    title = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey('auth.user', related_name='posts', on_delete=models.CASCADE)


    class Meta:
        ordering = ['created']




