from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from .models import Product
from .serializer import ProductSerializer
import math


# Create your views here.

class ProductFrontendAPIView(APIView):

    def get(self, request ):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductBackendAPIView(APIView):

    def get(self, request):
        s = request.GET.get('s')
        sort = request.GET.get('sort')
        page = int(request.GET.get('page',1))
        per_page = 9
        
        products = Product.objects.all()
        if s:
            products = products.filter(Q(title__icontains=s)|Q(description__icontains=s))
        if sort=='asc':
            products = products.order_by('price')
        elif sort=='desc':
            products = products.order_by('-price')

        total = products.count()
        start = (page-1) * per_page
        end = page*per_page

        print(page, start, end, products[start:end])
        serializer = ProductSerializer(products[start:end], many=True)
        # return Response(serializer.data)
        return Response({
                'page':page,
                'count': len(serializer.data),
                'last_page': math.ceil(total / per_page),
                'total': total,
                'data': serializer.data,
            })

