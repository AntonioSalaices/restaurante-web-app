from rest_framework import generics
from apps.menu.models import Producto
from apps.pedidos.models import Pedidos
from apps.api.serializers import ProductoSerializer, PedidoSerializer
from rest_framework import status
from rest_framework import filters
from rest_framework.response import Response

class PedidosAPI(generics.ListCreateAPIView):
    queryset = Pedidos.objects.all()
    serializer_class = PedidoSerializer    
    def post(self, request):
        serializer = PedidoSerializer(data = request.data)
        if serializer.is_valid(): #Validacion de lo que se obtiene para proceder a guardar y emitir status
            pedido = serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class ListProductosAPI(generics.ListAPIView):
    queryset = Producto.objects.all() #Consulta ORM que devuelve los productos
    serializer_class = PedidoSerializer #Metodo para serializar los campos del modelo
    filter_backends = [filters.SearchFilter] #Implementación del filtro
    search_fields = ['categoria']  # Aquí se determinan los filtros posibles     
    
    def get(self, request):
        if request.GET.get('categoria'):
            queryset= Producto.objects.filter(categoria__nombre__icontains=request.GET.get('categoria'))
        else:
            queryset= Producto.objects.all()
        serializer = ProductoSerializer(queryset,many=True)
        return Response(serializer.data)