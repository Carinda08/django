from django.urls import path, re_path
from . import views

urlpatterns = [
    path('books/', views.BookInfoView.as_view()),
    re_path('books/(\d+)', views.BookInfoDetailView.as_view()),
    path('heros/', views.HeroInfoView.as_view()),
]

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'book', views.Viewset, basename='books')
urlpatterns += router.urls