from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from froala_editor.fields import FroalaField


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = FroalaField()
    #content = models.TextField() #TextField unrestricted text
    date_posted = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('forum-home')
       # return reverse('post-detail', kwargs={'pk': self.pk})


        #not using redirect. that's for finding the location for a specific post.
        #redirect - redirects you to specific route
        #reverse  - returns the full url to that route w a string.


#reply?
#(default=timezone.now)
#CASCADE if a user is deleted, delete their posts as well
#django uses pillow to handle Imagefield by default.