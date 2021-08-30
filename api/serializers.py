from rest_framework import serializers
from .models import Tastes, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id","name","img","description","tastes"]