from .models import Censo
from rest_framework import serializers


class CensoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Censo
        fields = ('id', 'id_votacion', 'rol', 'nombre', 'fecha_ini', 'fecha_fin')

    fecha_ini = serializers.DateTimeField(format='%d/%m/%Y %H:%M')
    fecha_fin = serializers.DateTimeField(format='%d/%m/%Y %H:%M')


class DeleteSerializer(serializers.Serializer):
    exito = serializers.BooleanField()
    mensaje = serializers.CharField(max_length=60)


class ResultSerializer(serializers.Serializer):
    result = serializers.BooleanField()


