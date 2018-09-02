from django.urls import path
from customuser import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
