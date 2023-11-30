from django.db import models
from django.utils import timezone
# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=220)
    content=models.TextField(max_length=330)
    counted_view=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    created_date=models.DateField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True,)
    published_date=models.DateTimeField(null=True)
 
    class Meta:
        db_table_comment = "Question answers"
        verbose_name='پست'
        verbose_name_plural='پست ها'
    def __str__(self):
        return "{}-id={}".format(self.title,self.id) 