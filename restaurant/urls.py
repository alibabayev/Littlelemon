from django.urls import path, include
from rest_framework.routers import DefaultRouter

from restaurant import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('menu/', views.MenuItemViewSet.as_view(), name='menu-list'),
    path('menu/<int:pk>/', views.SingleMenuItemViewSet.as_view(), name='menu-detail'),
]