from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.signals import email_confirmed
from django.forms import ModelForm
from django.urls import reverse 


#This class just extends the already existing user in django
#Edit with care will affect the entire DB schema
#See https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(null=True, blank=True)
    cover_photo = models.ImageField(null=True, blank=True)
    Address = models.CharField(max_length=200, null=True, blank=True)
    phonenumber = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=80, null=True, blank=True)
    website = models.CharField(max_length=50, null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    linkedin = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length = 8, null=True, blank=True)
    language = models.CharField(max_length = 12, null=True, blank=True)
    currency = models.CharField(max_length = 12, null=True, blank=True)
    is_agency = models.NullBooleanField(null=True, blank=True)
    certification = models.ImageField(null=True, blank=True) #if the user is an agency, business certification doc
    verified = models.NullBooleanField(null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True) #The priniciple of rating on the a user is based on the ratings of all properties/ no. of properties
    date_joined = models.DateTimeField(null=True, blank=True)
    firstlogin = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('user-profile', kwargs={'pk': self.pk})

    def __str__(self):
        return self.first_name

class userUpdate(ModelForm):
    class Meta:
        model = User
        fields = ['profile_photo','cover_photo','bio', 'date_of_birth', 'Address','phonenumber', 'email',
        'website', 'facebook', 'instagram', 'twitter', 'linkedin', 'gender', 'language', 'currency',
        'is_agency','certification']

class Property(models.Model):
    name = models.CharField(max_length=50, null = True, blank = True)
    tagline = models.CharField(max_length=100,null = True, blank = True)
    address = models.CharField(max_length=100,null = True, blank = True)
    profile_photo = models.ImageField(null=True, blank=True)
    cover_photo = models.ImageField(null=True, blank=True)
    for_rent = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    number_rated = models.PositiveSmallIntegerField(null=True, blank=True)
    area = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    bedrooms = models.PositiveSmallIntegerField(null=True, blank=True)
    bathrooms = models.PositiveSmallIntegerField(null=True, blank=True)
    garages = models.PositiveSmallIntegerField(null=True, blank=True)
    APARTMENT = 'APARTMENT'
    OFFICE = 'OFFICE'
    HOME = 'HOME'
    PROPERTY_TYPES = (
        (APARTMENT, 'Apartment'),
        (OFFICE, 'Office'),
        (HOME, 'Home'),
    )
    property_type = models.CharField(max_length=100, choices=PROPERTY_TYPES, blank=False)
    CONSTRUCTION_YEAR = (
        (1996, '1996'),
        (1997, '1997'),
        (1998, '1998'),
        (1999, '1999'),
        (2000, '2000'),
        (2001, '2001'),
    )
    construction_year = models.CharField(max_length=10,choices = CONSTRUCTION_YEAR, blank = False)
    last_renovation = models.CharField(max_length=10, choices = CONSTRUCTION_YEAR, blank = False)
    description = models.TextField(max_length=500, blank=True)
    amenities = models.ForeignKey('Amenities', on_delete = models.CASCADE,)
    gps = models.CharField(max_length=500,null=True, blank=True)
    user = models.ForeignKey('User', on_delete = models.CASCADE,)

class Proprty_Amenities(models.Model):
    amenities = models.ForeignKey('Amenities', on_delete = models.CASCADE,)
    user = models.ForeignKey('User', on_delete = models.CASCADE,)

class Amenities(models.Model):
    name = models.CharField(max_length=80,null=True, blank=True)

class Review(models.Model):
    title = models.CharField(max_length=40,null = True, blank = True)
    Date = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=500, blank=True)
    property = models.ForeignKey('Property', on_delete = models.CASCADE,)
    user = models.ForeignKey('User', on_delete = models.CASCADE,)

class Gallery(models.Model):
    images = models.ImageField(null=True, blank=True)
    property = models.ForeignKey('Property', on_delete = models.CASCADE,)





