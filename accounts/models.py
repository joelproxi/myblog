from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


# User = get_user_model()
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/img/%Y/%m/%d', blank=True)
    
    def __str__(self):
        return 'Profile of %s' % self.user.username
    