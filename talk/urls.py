from django.urls import path
from talk import views

urlpatterns = [
    path('',views.Dashboard.as_view(),name='dashboard'),
    path('profile-list/',views.profile_list.as_view(),name='profile_list'),
    path('profile/<int:pk>/',views.Profile.as_view(),name='profile')
]
