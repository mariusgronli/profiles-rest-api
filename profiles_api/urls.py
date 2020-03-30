from django.urls import path,include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('api-viewset',views.HelloViewSet, base_name='api-viewset')
router.register('profile-viewset',views.UserProfileViewSet)

urlpatterns=[
    path('hello-view/', views.HelloApiView.as_view()),
    path('',include(router.urls)),
]
