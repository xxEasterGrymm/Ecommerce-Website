from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='Home'),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls'))
]