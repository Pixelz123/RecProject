from django.db import models

# Create your models here.
class Experience(models.Model) :
    title=models.CharField(max_length=255)
    content=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    author =models.TextField()
    role=models.CharField(max_length=255, default='SWE')
    serial=models.IntegerField(default=0)
    org=models.TextField(default="Google")
    
