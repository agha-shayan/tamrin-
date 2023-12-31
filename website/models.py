from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=66)
    email=models.EmailField()
    subject=models.CharField(max_length=90)
    message=models.TextField(max_length=1000)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['created_date']
    def __str__(self):
        return self.name