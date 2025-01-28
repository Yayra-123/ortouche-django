from django.db import models

# Create your models here.

class Logo(models.Model):
    image = models.ImageField(upload_to='logo')
    titre = models.CharField(max_length= 255)
    
    def __str__(self):
        return self.titre