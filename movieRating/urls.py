from django.urls import path,include
from rest_framework import routers
from .views import MovieView,RatingView

router = routers.DefaultRouter()
router.register("movies",MovieView,basename="movies")
router.register("ratings",RatingView,basename="ratings")

urlpatterns = [
    path("",include(router.urls))
]