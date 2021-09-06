from django.db import models
from django.contrib import auth

# Create your models here.
class User(auth.models.AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Student'),
        (2, 'Teacher')
    )

    user_type = models.PositiveIntegerField(choices=USER_TYPE_CHOICES, default=1)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


# class Contact(models.Model):
#      sno= models.AutoField(primary_key=True)
#      name= models.CharField(max_length=255)
#      phone= models.CharField(max_length=13)
#      email= models.CharField(max_length=100)
#      content= models.TextField()
#      timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

#      def __str__(self):
#           return "Message from " + self.name + ' - ' + self.email