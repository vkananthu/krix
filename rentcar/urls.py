from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from huur import views  # Change 'huur' to your app name if different


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signup_view, name='signup'),
    path('login/',views.login_view, name='login'),
    path('home/', views.home_view, name='home'),  # Create a home view to redirect after login/signup
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),  # Add additional URLs from the first set


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)