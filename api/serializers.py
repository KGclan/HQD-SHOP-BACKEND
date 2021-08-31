from django.db.models import fields
from rest_framework import serializers
from .models import Tastes, Product


class TastesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tastes
        fields = ["name"]

class ProductSerializer(serializers.ModelSerializer):

    tastes = TastesSerializer(many=True)

    class Meta:
        model = Product
        fields = ["id","name","img","description","tastes"]