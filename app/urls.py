from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from cars.views import CarView, CarRegistrationView
from accounts.views import user_registration, login_view, logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', CarView.as_view(), name='car_list'),
    path('newcar/', CarRegistrationView.as_view(), name='newcar'),

    path('register_user/', user_registration, name='register_user'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Serve arquivos de midia
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0]) # Serve arquivos estaticos
