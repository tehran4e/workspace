from django.contrib import admin
from django.urls import path
from details import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('details/<id>', views.mdetail, name='mdetail')
]
