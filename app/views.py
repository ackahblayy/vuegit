from django.shortcuts import render, redirect
from django.views import generic #allows to use class based views 
#from django.utils.decorators import method_decorator
#from allauth.account.signals import email_confirmed 
from django.http import HttpResponse
from app.signals import handlers
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import User,userUpdate
from django.urls import reverse, reverse_lazy

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['isNavTransparent'] = True
        return context

def profile(request):
    firstLogin = request.user.firstlogin
    if firstLogin:
        user = request.user
        user.firstlogin = False
        user.save()
        return redirect('user-update', user.id)
    else:
        user = request.user
        return redirect('user-profile', user.id)


class UserUpdate(UpdateView):
    model = User
    fields = ['first_name','last_name','profile_photo','cover_photo','bio', 'date_of_birth', 'Address','phonenumber', 'email',
        'website', 'facebook', 'instagram', 'twitter', 'linkedin', 'gender', 'language', 'currency',
        'is_agency','certification']

    

class UserProfile(generic.DetailView):
    model = User

    def get_object(self):
        object = super().get_object()
        firstLogin = object.firstlogin

        if firstLogin:
            object.firstlogin = False
            object.save()
            template_name = 'app/userupdate_form.html'
        else:
            template_name = 'account/user-profile.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # check if the navigation bar should be transparent 
        context['isNavTransparent'] = True
        return context


    
