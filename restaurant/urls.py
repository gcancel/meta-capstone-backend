from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.MenuItemView.as_view(), name='menu'),
    path ('menu/<int:pk>', views.MenuItemView.as_view(), name='menu-single'),
    path('booking/<int:pk>', views.SingleBookingView.as_view(), name='single-booking'),
    path('api-token-auth/', obtain_auth_token),
]