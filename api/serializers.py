from .models import Artist, Albom, Song
from rest_framework import serializers

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class ArtistSerializerMobile(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class AlbomSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    class Meta:
        model = Albom
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields =('title', 'albom', 'image')
