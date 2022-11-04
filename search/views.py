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
        s = request.GET.get('s')                      # cadena que debe estar en titulo o en descripción
        sort = request.GET.get('sort')                # ordenamiento asc o desc    (si no se proporciona no se ordena)
        page = int(request.GET.get('page',1))         # número de página a mostrar (default 1)
        per_page = int(request.GET.get('per_page',10)) # número de datos por página (default 10)
        
        products = Product.objects.all()
        if s:
            products = products.filter(Q(title__icontains=s)|Q(description__icontains=s))
        if sort=='asc':
            products = products.order_by('price')
        elif sort=='desc':
            products = products.order_by('-price')

        total = products.count()
        total_pages = math.ceil(total / per_page)
        # si la pagina solicitada está fuera del número de datos solicitados reinicia la página a 1
        if total_pages<page: 
            page = 1

        start = (page-1) * per_page
        end = page*per_page
    
        serializer = ProductSerializer(products[start:end], many=True)
        # return Response(serializer.data)
        return Response({
                'page':page,
                'count': len(serializer.data),
                'last_page': total_pages,
                'total': total,
                'data': serializer.data,
            })

