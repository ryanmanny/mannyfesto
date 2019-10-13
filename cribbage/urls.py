from django.urls import path

from cribbage import views as cribbage_views


urlpatterns = [
    path('', cribbage_views.cribbage_home, name='cribbage'),
    path('<slug>/', cribbage_views.cribbage_detail, name='cribbage_post'),
]
