from django.contrib.auth.models import Group
from . import models
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class FilePrintSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.FilePrint
        fields = ['url', 'file_name','pemesan','tipe_print','bolak_balik','printed','taken_at']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user) -> Token:
        token = super().get_token(user)

        token['username'] = user.username
        return token
