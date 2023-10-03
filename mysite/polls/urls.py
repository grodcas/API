from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("drinks/", views.drink_list, name='drinks'),
    path("drinks/<int:id>", views.drink_detail, name='drink-details'),
    path('update/', views.update_variable, name='update_variable'),
    path('update2/', views.update_variable2, name='update_variable2'),
    path('update3/', views.update_variable3, name='update_variable3'),
    path('update4/', views.update_variable4, name='update_variable4'),

]   