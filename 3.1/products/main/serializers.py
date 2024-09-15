from dataclasses import fields

from django.db.models import Prefetch
from rest_framework import serializers

from .models import Review, Product


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductListSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    # реализуйте поля title и price


class ProductDetailsSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'reviews')
    def get_reviews(self, obj):
        return ReviewSerializer(obj.reviews.all(), many=True).data
    # реализуйте поля title, description, price и reviews (список отзывов к товару)
