
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users import forms
# from users.models import Contact
from django.contrib import messages 

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'

# def contact(request):
#     if request.method=="POST":
#         name=request.POST['name']
#         email=request.POST['email']
#         phone=request.POST['phone']
#         content =request.POST['content']
#         if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
#             messages.error(request, "Please fill the form correctly")
#         else:
#             contact=Contact(name=name, email=email, phone=phone, content=content)
#             contact.save()
#             messages.success(request, "Your message has been successfully sent")
#     return render(request, "/contact.html")