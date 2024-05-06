from django.contrib import admin
from django.urls import path,include
admin.site.site_header = "Madhur Ice-Cream Admin"
admin.site.site_title = "Madhur Admin Portal"
admin.site.index_title = "Welcome to Madhur Ice-Creames Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
]
