from django.urls import path
from .views import firstone, delete_stu, update

urlpatterns = [
    path('',firstone, name='firstone'),
    
    path('delete_stu/<int:id>/', delete_stu,name='delete_stu'),
    path('update/<int:id>/', update,name='update')
]
