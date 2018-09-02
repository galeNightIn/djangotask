from django.urls import path
from customuser import views

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]
