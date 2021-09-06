from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from courses.models import Course
from django.shortcuts import render
from django.contrib import messages




class UserProfile(LoginRequiredMixin, generic.ListView):
    model = Course
    template_name = 'user_profile.html'

class mycourse(LoginRequiredMixin, generic.ListView):
    model = Course
    template_name = 'mycourse.html'



def index(request):
    return render(request, 'index.html')



def about(request):
    return render(request, 'about.html')





