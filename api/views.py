from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Artist, Albom, Song
from .serializers import ArtistSerializer, ArtistSerializerMobile, AlbomSerializer, SongSerializer


class ArtistAPIView(APIView):
    def get(self, request):
        queryset = Artist.objects.all()
        serializer = ArtistSerializer(queryset, many=True)
        return Response(data=serializer.data)

class ArtistAPIViewMobile(APIView):
    def get(self, request):
        queryset = Artist.objects.all()
        serializer = ArtistSerializerMobile(queryset, many=True)
        return Response(data=serializer.data)


class AlbomAPIView(APIView):
    def get(self, request):
        alboms = Albom.objects.all()
        albom_serializer = AlbomSerializer(alboms, many=True)
        return Response(data=albom_serializer.data)


class SongAPIView(APIView):
    def get(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(data=serializer.data)