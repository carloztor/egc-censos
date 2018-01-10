from rest_framework.test import APITestCase

from .models import Censo

from rest_framework.response import Response
from rest_framework import status


class CensoTests(APITestCase):
    def test_delete_censo(self):
        c1 = Censo.objects.create(id_votacion=196, id_grupo=101, fecha_ini='2017-11-15 11:11:11', nombre='Censocreate',
                                  fecha_fin='2018-12-15 11:11:11')
        c1.save()
        c2 = Censo.objects.all()
        self.assertEquals(c2.count(), 1)
        Censo.objects.filter(id=c1.id).delete()
        c3 = Censo.objects.all()
        self.assertEquals(c3.count(), 0)

    def test_filter_(self):
        c1 = Censo.objects.create(id_votacion=196, id_grupo=101, fecha_ini='2017-11-15 11:11:11', nombre='Censocreate',
                                  fecha_fin='2018-12-15 11:11:11')
        return Censo.objects.filter(nombre='Censocreate').exists() is True

    def test_filter_Negative(self):
        c1 = Censo.objects.create(id_votacion=196, id_grupo=101, fecha_ini='2017-11-15 11:11:11', nombre='Censocreate',
                                  fecha_fin='2018-12-15 11:11:11')
        return Censo.objects.filter(nombre='paco', id_votacion=196).exists() is False

    def test_update_censo(self):
        c1 = Censo.objects.create(id_votacion=196, id_grupo=101, nombre="Censocreate", fecha_ini="2017-12-15 11:11:11",
                                  fecha_fin="2019-12-15 11:11:11")
        Censo.objects.update(id=196, nombre="CensoUpdate")
        Censo.objects.get(nombre="CensoUpdate")

    def test_update_censo_group(self):
        c1 = Censo.objects.create(id_votacion=196, id_grupo=101, nombre="Censocreate",
                                  fecha_ini="2017-12-15 11:11:11",
                                  fecha_fin="2019-12-15 11:11:11")
        Censo.objects.update(id=196, nombre="CensoUpdate", id_grupo=103)
        Censo.objects.get(nombre="CensoUpdate")

    def test_create_positive(self):
        c1 = Censo.objects.create(id_votacion=200, rol='PONENTE' fecha_ini='2017-11-15 11:11:11', nombre='Censocreate',
                                  fecha_fin='2018-12-15 11:11:11')
        c1.save()
        c2 = Censo.objects.all()
        self.assertEquals(c2.count(), 1)
        return Censo.objects.filter(nombre='Censocreate').exists()

    def test_create_negative(self):
        try:
            censo = Censo.objects.create(id_votacion=200, rol='ASISTENTE', nombre='', fecha_ini='2017-11-15 11:11:11',
                                         fecha_fin='2018-12-15 11:11:11')
        except Exception:
            Response(status=status.HTTP_404_NOT_FOUND)

        return Response.status_code == 404