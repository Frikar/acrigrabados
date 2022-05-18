from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(null=True, blank=True, max_length=100)
    msg = models.TextField()
    
    # cambiar Date por DateTime
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name
