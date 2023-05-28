from rest_framework import serializers
from .models import DiffExpression
from .models import Polynomial
from .models import LinearAlgebra

class DiffSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiffExpression
        fields = ['exp', 'user_name']


class PolySerializer(serializers.ModelSerializer):
    class Meta:
        model = Polynomial
        fields = ['exp', 'user_name']

class LalgSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinearAlgebra
        fields = ['exp', 'user_name']