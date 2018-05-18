from django.contrib import admin
from .models import User, Property, Proprty_Amenities, Amenities, Review, Gallery
# Register your models here.

admin.site.register(User)

admin.site.register(Property)
admin.site.register(Proprty_Amenities)
admin.site.register(Amenities)
admin.site.register(Review)
admin.site.register(Gallery)