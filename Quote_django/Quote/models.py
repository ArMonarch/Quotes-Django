from django.db import models

# Create your models here.
class Category(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.CharField(max_length=255, null=True, default="Description")
    
    class Meta:
        ordering = ("Name",)
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.Name
