from rest_framework import serializers
from django.db.models import Avg
from .models import Movie,Rating

'''Movie Serializer'''
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields =  ['id','name','genre','rating','release_date']

class GetMovieSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    total_rating = serializers.SerializerMethodField()

    def get_avg_rating(self,movie:Movie):
        return Rating.objects.filter(movie_id=movie.id).aggregate(Avg('rating', default=0))["rating__avg"]

    def get_total_rating(self,movie:Movie):
        return Rating.objects.filter(movie_id=movie.id).count()

    class Meta:
        model = Movie
        fields =  ['id','name','genre','rating','release_date','avg_rating','total_rating']


'''Rating Serializer'''
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id','user_id','movie_id','rating']


