from django.contrib import admin
from django.urls import path, include
from .views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('nimadur/', home),
    path('', include('blog.urls'))
    path('coffre/', include('coffee.urls'))
]

urlpatterns += static(settings.STATIC_URL)