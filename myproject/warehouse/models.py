from django.db import models
from django.utils.text import slugify


# Create your models here.
class Cloth(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="post_images")
    production_date = models.DateField()
    Sizes = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    ]
    sizes = models.CharField(max_length=1, choices=Sizes)
    slug = models.SlugField(default='', blank=True)

    def save(self):
        self.slug = slugify(self.name)
        super(Cloth, self).save()

    def __str__(self):
        return '%s' % self.name
