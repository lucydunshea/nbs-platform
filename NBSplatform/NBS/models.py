from django.db import models
#from ckeditor.fields import RichTextField

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # long_description = RichTextField()
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    partners = models.CharField(max_length=255, blank=True)

    slug = models.SlugField(unique=True, max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name