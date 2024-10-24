from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Subject = models.CharField(max_length=1000)
    Mesaage = models.CharField(max_length=1000)

    def __str__(self):
        return f'Name: {self.Name} - Subject: {self.Subject}'