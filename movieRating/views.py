from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from .models import Movie,Rating
from .serializers import MovieSerializer,RatingSerializer,GetMovieSerializer


class MovieView(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer 

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetMovieSerializer
        return MovieSerializer

class RatingView(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
