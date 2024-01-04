from django.db import models


# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class meta:
        ordering = ['-date']


class comment(models.Model):
    post = models.ForeignKey(blog,related_name='comment',on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class meta:
        ordering = ['-date']
