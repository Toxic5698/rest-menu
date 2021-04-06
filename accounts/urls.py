from django.urls import path
from . import views
from .views import OrderListView




urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('', views.home, name='home'),


    path('edit_menu/<str:pk>/', views.editMenu, name='edit_menu'),
    path('make_order/', views.makeOrder, name='make_order'),
    path('orders/', views.orders, name='orders'),
    path('order_table/', OrderListView.as_view(), name='order_table'),
    path('edit_supper/<str:pk>', views.editSupper, name='edit_supper'),
    path('edit_meal/<str:pk>', views.editMeal, name='edit_meal'),
    path('edit_desert/<str:pk>', views.editDesert, name='edit_desert'),
    path('edit_order/<str:pk>/', views.editOrder, name='edit_order'),
    path('delete/<str:pk>/', views.deleteOrder, name='delete'),
    path('delete_all_orders/', views.deleteOrders, name='delete_all_orders'),
    path('print_menu/', views.printMenu, name='print_menu'),
    ]
