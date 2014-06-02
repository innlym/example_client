# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, access_token, refresh_token):
        user = self.model(
            username = username,
            access_token = access_token,
            refresh_token = refresh_token,
            )
        user.set_password('innlym')
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):

    username = models.CharField(max_length=32,unique=True,db_index=True)
    access_token = models.CharField(max_length=256, null=True, blank=True)
    refresh_token = models.CharField(max_length=256, null=True, blank=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

