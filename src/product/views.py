"""
product app models
"""
from rest_framework.response import Response
from rest_framework import permissions, viewsets, status

from .models import Category, Product, ProductSeller, Review, ProductFeature, Feature, User
from seller.models import Seller, SellerUser
from .models import Wishlist
from rest_framework import viewsets, status
from rest_framework.response import Response
from .permissions import UserAccessPermission
from .serializers import (WishlistSerializer,
                          CategorySerializer,
                          ProductReviewSerializer,
                          SellerReviewSerializer,
                          ProductSellerSerializer,
                          ProductSerializer)

class WishlistViewset(viewsets.ModelViewSet):

    http_method_names = ('get', 'post', 'patch', 'delete')
    permission_classes = [UserAccessPermission]
    serializer_class = WishlistSerializer

    def get_queryset(self):
       return Wishlist.objects.filter(user=self.request.user)


class CategoryView(viewsets.ModelViewSet):
    '''
    category view -
    view to list all category to the db
    Anyone can access the view
    '''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.AllowAny,)


## Completed But needs Code improvement here
class ProductView(viewsets.ModelViewSet):
    def list(self, request):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer(queryset, many=True)
        permission_classes = (permissions.AllowAny,)
        return Response(serializer_class.data)

    def create(self, request):
        data = request.data
        queryset = Product.objects.filter(brand__in=data['brand'],
                                          category__in=data["category_id"],
                                          base_price__gte=data["min_price"],
                                          base_price__lte=data["max_price"])
        pro_id = queryset.values_list('id', flat=True)
        exclude_list = []
        for pid in pro_id:
            pro_ratings = Review.objects.filter(product=pid).values_list('rating', flat=True)
            if pro_ratings:
                if (sum(pro_ratings)/len(pro_ratings)) < data["rating"]:
                    exclude_list.append(pid)
            else:
                    exclude_list.append(pid)
        queryset = queryset.exclude(id__in=exclude_list)
        serializer_class = ProductSerializer(queryset, many=True)
        permission_classes = (permissions.AllowAny,)
        return Response(serializer_class.data)

class ProductSellerView(viewsets.ModelViewSet):
    queryset = ProductSeller.objects.all()
    lookup_field = 'product'
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProductSellerSerializer

class SellerReviewView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    lookup_field = 'seller_id'
    permission_classes = (permissions.AllowAny,)
    serializer_class = SellerReviewSerializer

class ProductReviewView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    lookup_field = 'product_id'
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProductReviewSerializer
