from django.conf import settings
from django.db import models
class Menu23(models.Model):
    'Generated Model'
    menu = models.ManyToManyField("home.Main",related_name="menu23_menu",blank=True,)
class Main(models.Model):
    'Generated Model'
    main_menu = models.OneToOneField("users.User",on_delete=models.SET_DEFAULT,default="0123456789",related_name="main_main_menu",blank=True,)
