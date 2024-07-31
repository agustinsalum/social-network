
from django.urls import path
from .router import router
from .viewsets import UserProfileViewSet, TakenLessonViewSet
from .viewsets import RandomDogImageView, HttpCatImageView, WeatherView

# Define the URLs to access the views. In our case with the help of the router that does them automatically.

app_name = "socialApp"

urlpatterns = [
    path('usersProfile/<int:pk>/friends/', UserProfileViewSet.as_view({'get': 'friends'}), name='user-friends'),
    path('usersProfile/<int:pk>/friends_lessons/', UserProfileViewSet.as_view({'get': 'friends_lessons'}), name='friends-lessons'),
    path('takenLessons/<int:pk>/user_lessons/', TakenLessonViewSet.as_view({'get': 'user_lessons'}), name='user-lessons'),
    path('random-dog/', RandomDogImageView.as_view(), name='random-dog'),
    path('http-cat/<int:status_code>/', HttpCatImageView.as_view(), name='http-cat'),
    path('weather/<str:city_name>/', WeatherView.as_view(), name='weather')
]

urlpatterns += router.urls