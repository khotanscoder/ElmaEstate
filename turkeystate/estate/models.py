from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

# Create your models here.
from django.urls import reverse


class Estate(models.Model):
    verbose_name = 'properties'
    LABEL_CHOICES = (
        ('P', 'primary'),
        ('S', 'secondary'),
        ('D', 'danger'),
    )
    TYPE_CHOICES = [('S', 'FOR SALE'), ('R', 'FOR RENT')]
    title = models.CharField(max_length=150)
    code = models.CharField(max_length=5, default='A101', primary_key=True)
    address = models.CharField(max_length=150)
    area = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    distance_to_sea = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField
    label = models.CharField(max_length=1, choices=LABEL_CHOICES, blank=True, null=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    price = models.IntegerField()
    discount_price = models.FloatField(blank=True, null=True)
    img = models.ImageField()

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return reverse('estate', kwargs={
            'slug': self.slug
        })


class Project(models.Model):
    status = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField()
    img = models.ImageField()
    minimum = models.CharField(max_length=2, blank=True, null=True)


class Like(models.Model):
    pass


class View(models.Model):
    pass


class Blog(models.Model):
    author = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField()
    date = models.DateTimeField()
    # views = models.ForeignKey(View, on_delete=models.CASCADE, default=0)
    # likes = models.ForeignKey(Like, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.author


