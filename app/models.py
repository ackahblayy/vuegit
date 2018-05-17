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

