from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} Profile"
    
    def save(self):
        super().save()
        
        img = Image.open(self.image.path)

        max_size = 300
        if img.height > max_size or img.width > max_size:
            output_size = (max_size, max_size)
            img.thumbnail(output_size)
            img.save(self.image.path)
