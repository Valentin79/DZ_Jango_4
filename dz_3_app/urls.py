from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_orders/<int:user_id>/<int:days>', views.user_orders, name='User_orders'),
    path('chose_goods/', views.choose_goods, name='edit_goods'),
    path('edit_goods/', views.edit_goods, name='edit_goods'),
    path('upload_image/', views.add_image, name='upload_image'),
]