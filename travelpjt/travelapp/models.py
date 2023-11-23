from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length= 250)
    image=models.ImageField(upload_to='pics')
    des=models.TextField()
    def __str__(self):
        return self.name
class person(models.Model):
    image = models.ImageField(upload_to='pics')
    name=models.CharField(max_length=250)
    des = models.TextField()
    def __str__(self):
        return self.name