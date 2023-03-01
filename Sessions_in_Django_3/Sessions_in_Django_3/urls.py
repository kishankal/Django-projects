
from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.settestcookie,name='set'),
    path('get/',views.checktestcookie,name='get'),
    path('del/',views.deltestcookie,name='del'),
    # path('get/',views.getcookie),

]
