from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [

]

urlpatterns += router.urls
