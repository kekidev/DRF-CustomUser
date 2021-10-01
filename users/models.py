from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None, **other_fields):
        if not email:
            raise ValueError(_('Users must have an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)

        user.set_password(password)
        user.save()
        
        return user

    def create_superuser(self, email, username, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username , password, **other_fields)

    def create_user(self, email, username, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_("username"), max_length=12)
    created_at = models.DateField(_("created at"), auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    objects = CustomAccountManager()
    class Meta:
        ordering = ['-created_at']
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self) -> str:
        return self.email
