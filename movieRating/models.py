from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    rating = models.CharField(max_length=50)
    release_date = models.DateField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']

class Rating(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='user')
    movie_id = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='movie')
    rating = models.FloatField(validators=[MinValueValidator(1,message="Rating should be start with 1"),MaxValueValidator(5,message="Rating should not greater than 5")])

    class Meta:
        ordering = ['movie_id']



