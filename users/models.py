from django.db import models
from django.contrib.auth.models import User
from PIL import Image 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

#override save method to resize large imgs

#can print out instead of saying profile object.
    def __str__(self):
        return f'{self.user.username} Profile'

#save method already exists in parent class. run the save method with super()...
#get the img saved and resize it.
    def save(self):
        super().save()
 
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path) #overrides the large img


#male, female,
#zip code?
#etc. 