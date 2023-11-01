from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('songs/', views.SongListView.as_view(), name='songs'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    #path('song/<uuid:pk>',views.SongDetailView.as_view(), name='song-detail'),
    path('song/<int:pk>', views.SongDetailView.as_view(), name='song-detail'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]