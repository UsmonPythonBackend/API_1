from django.urls import path
from .views import ArtistAPIView, ArtistAPIViewMobile, AlbomAPIView, SongAPIView

urlpatterns = [
    path('artist/', ArtistAPIView.as_view(), name="artist"),
    path('artist-mobile/', ArtistAPIViewMobile.as_view(), name="artist-mobile"),
    path('albom/', AlbomAPIView.as_view(), name="album"),
    path('songs/', SongAPIView.as_view(), name="songs"),
]