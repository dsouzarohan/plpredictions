from django.urls import path, include
from . import views

urlpatterns = [
    path('predictions/', views.get_predictions),
    path('predictions/season', views.predict_season),
    path('predictions/standings', views.get_standings)
]
