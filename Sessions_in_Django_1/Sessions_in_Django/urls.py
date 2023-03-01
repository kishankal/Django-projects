
from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.setsession,name='set'),
    path('get/',views.getsession,name='get'),
    path('del/',views.delsession,name='del'),
    # path('get/',views.getcookie),

]
