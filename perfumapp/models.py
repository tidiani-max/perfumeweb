from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perfume(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='perfumes/')  # Needs Pillow library for image handling
    whatsapp_link = models.URLField()  # URL link to WhatsApp for buying the product

    def __str__(self):
        return self.name

# Profile to distinguish the owner
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)  # If true, user can add/edit/delete products

    def __str__(self):
        return f"{self.user.username} - {'Owner' if self.is_owner else 'User'}"
    
class Testimony(models.Model):
    name = models.CharField(max_length=255)
    testimony = models.TextField()
    image = models.ImageField(upload_to='perfumes/testimony')  # Needs Pillow library for image handling
     # URL link to WhatsApp for buying the product

    def __str__(self):
        return self.name


