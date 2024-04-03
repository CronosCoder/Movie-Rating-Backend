from django.contrib import admin
from . import models


#----------Movie Admin----------
@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','name','genre','rating','release_date']

#----------Rating Admin----------
@admin.register(models.Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['id','movie_id','user_id','rating']