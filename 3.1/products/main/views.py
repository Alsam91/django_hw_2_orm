from itertools import product

from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import title
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer

from main.models import Review, Product


class ReviewView(APIView):
    def get(self, request, pk):
        queryset = Review.objects.all()
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def products_list_view(request):
    queryset = Product.objects.all()
    serializer = ProductListSerializer(queryset, many=True)
    return Response(serializer.data)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        try:
            prod = Product.objects.get(id=product_id)
            serializer = ProductDetailsSerializer(prod)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response(status=404)



# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        pass
        # """обработайте значение параметра mark и
        # реализуйте получение отзывов по конкретному товару с определённой оценкой
        # реализуйте сериализацию полученных данных
        # отдайте отсериализованные данные в Response"""
