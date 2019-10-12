from rest_framework import serializers
from apps.menu.models import Producto, Categoria
from apps.pedidos.models import Pedidos
from django.db import models



#En esta clase se serializan los eventos
class ProductoSerializer(serializers.ModelSerializer):
    # nombre = serializers.CharField()
    # descripcion = serializers.CharField()
    # precio = serializers.FloatField()
    # imagen = serializers.ImageField()
    # categoria = serializers.IntegerField(read_only=True)
   
    class Meta:
        model = Producto
        fields = [
            'id',
            'nombre',
            'descripcion',
            'precio',
            'imagen',
            'categoria', 
        ]



#En esta clase se serializan los eventos
class PedidoSerializer(serializers.Serializer):
    nombre_cliente = serializers.CharField(max_length=50)
    mesa = serializers.IntegerField()
    orden = serializers.CharField(max_length=500)
    total = serializers.DecimalField(decimal_places=15,max_digits=30)
    observacion = serializers.CharField(max_length=500)

    class Meta:
        model= Pedidos
        fields = (
            'nombre_cliente',
            'mesa',
            'orden',
            'total',
            'observacion', 
        )
        

    def create(self, validate_data):
        instance = Pedidos()
        instance.nombre_cliente = validate_data.get('nombre_cliente')
        instance.mesa = validate_data.get('mesa')
        instance.orden = validate_data.get('orden')
        instance.total = validate_data.get('total')
        instance.observacion = validate_data.get('observacion')
        instance.save()
        return instance