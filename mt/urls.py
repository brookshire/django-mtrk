#
#  Copyright (C) 2016 David Brookshire <dave@brookshire.org>
#
from django.conf.urls import url, include
# from django.contrib.auth.models import User
from .models import Asset, AssetTransaction, Person, Genre
from rest_framework import routers, serializers, viewsets


class AssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Asset


class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person


class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre


class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'assets', AssetViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
