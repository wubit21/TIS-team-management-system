from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings

#from .forms import inputForm
task = [
       ("General inqury","General inqury"),
       ("Support","support and speed issues"),
       ("Provision","Provision"),
       ("Site down","Site down fiber loss or power loss"),
]
class user_input(models.Model):
      username=models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
      site = models.CharField(max_length=255)
      date = models.DateField(max_length=255)
      time = models.TimeField(max_length=255)
      task = models.CharField(max_length=255, choices=task)
      details=models.TextField(max_length=400)
      images=models.ImageField(null=True,blank=True,upload_to='images/' )
      USERNAME_FIELD = 'site'
      REQUIRED_FIELDS=['username','site','date','time','task']
def __str__(self):
       return self.site 




           











































'''
if user.is_active=True



class MyAccountManager(BaseUserManager):
 def create_user(self, email , username ):
  if not firstname:
    raise ValueError("Users must have firstname")
    if not lastname:
      raise ValueError("Users must have lastname")
      if not email:
        raise ValueError("Users must have an email address")
        if not username:
          raise ValueError("Users must have username")
          if not password:
            raise ValueError("Users must have password")
            if not phoneno:
              raise ValueError("Users must have phone number")
              user = self.model(
               email=self.normalize_email(email),
               username=username,
               )
              user.set_password(password)
              user.save(using=self._db)
              return user
              def create_superuser(self, email , username , password=None):
                user = self.create_user(
                 email=self.normalize_email(email),
                 username=username,
                 password=password,
                 )

                user.is_admin=True
                user.is_staff=True
                user.is_superuser=True
                user.save(using=self._db)
                return user



       #users is a table
class user(AbstractBaseUser):
        firstname = models.CharField(max_length=255)
        lastname  = models.CharField(max_length=255)
        email     = models.EmailField(max_length=55,unique=True)
        username  = models.CharField(max_length=30,unique=True)
        password  = models.CharField(max_length=255)
        phoneno   = models.IntegerField(null=True)
        is_staff  = models.BooleanField(default=True)
        is_superuse=models.BooleanField(default=False)
        is_active = models.BooleanField(default=True)
        is_admin  = models.BooleanField(default=False)

        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS=['username','password']
        objects =MyAccountManager()
        def __str__(self):
          return self.firstname
          def has_perm(self, perm,obj_Label):
           return self.is_admin
           def has_module_perms(self, app_Label):
            return True
'''