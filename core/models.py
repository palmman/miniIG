from django.db import models
from user.models import Profile

# Create your models here.

class Post(models.Model):

    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    featured_image = models.ImageField(null=True, blank=False)
    like = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def reviewers(self):
        queryset = self.comment_set.all().values_list('owner__id', flat=True)
        return queryset

    # @property
    # def imageURL(self):
    #     try:
    #         url = self.featured_image.url
    #     except:
    #         url = ''
    #     return url

class Comment(models.Model):

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['owner', 'post']]

    def __str__(self):
        return self.body


    