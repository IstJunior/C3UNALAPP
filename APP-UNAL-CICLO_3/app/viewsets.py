from pydoc import ModuleScanner
from rest_framework import viewsets
from . import models
from .serializers import FamiliarSerializer
from app import serializers
from rest_framework import generics
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DestroyAPIView


class FamiliarViewSet(viewsets.ModelViewSet):
    queryset = models.Familiar.objects.all()
    serializer_class = serializers.FamiliarSerializer

class UpdateFamiliarView(generics.UpdateAPIView):
    queryset = models.Familiar.objects.all()
    serializer_class = serializers.FamiliarSerializer

class DeleteFamiliarView(generics.DestroyAPIView):
    queryset = models.Familiar.objects.all()
    serializer_class = serializers.FamiliarSerializer


class MedicosViewSet(viewsets.ModelViewSet):
    queryset = models.Medicos.objects.all()
    serializer_class = serializers.MedicosSerializer

class UpdateMedicosView(generics.UpdateAPIView):
    queryset = models.Medicos.objects.all()
    serializer_class = serializers.MedicosSerializer

class DeleteMedicosView(generics.DestroyAPIView):
    queryset = models.Medicos.objects.all()
    serializer_class = serializers.MedicosSerializer

class PacientesViewSet(viewsets.ModelViewSet):
    queryset = models.Pacientes.objects.all()
    serializer_class = serializers.PacientesSerializer

class UpdatePacientesView(generics.UpdateAPIView):
    queryset = models.Pacientes.objects.all()
    serializer_class = serializers.PacientesSerializer

class DeletePacienteView(generics.DestroyAPIView):
    queryset = models.Pacientes.objects.all()
    serializer_class = serializers.PacientesSerializer

class Historia_clinicaViewSet(viewsets.ModelViewSet):
    queryset = models.HistoriaClinica.objects.all()
    serializer_class = serializers.Historia_clinicaSerializer
    
class UpdateHistoriaView(generics.UpdateAPIView):
    queryset = models.HistoriaClinica.objects.all()
    serializer_class = serializers.Historia_clinicaSerializer

class DeleteHistoriaView(generics.DestroyAPIView):
    queryset = models.HistoriaClinica.objects.all()
    serializer_class = serializers.Historia_clinicaSerializer

class SignosVitalesViewSet(viewsets.ModelViewSet):
    queryset = models.SignosVitales.objects.all()
    serializer_class = serializers.Signos_vitalesSerializer

class UpdateSignosView(generics.UpdateAPIView):
    queryset = models.SignosVitales.objects.all()
    serializer_class = serializers.Signos_vitalesSerializer

class DeleteSignosView(generics.DestroyAPIView):
    queryset = models.SignosVitales.objects.all()
    serializer_class = serializers.Signos_vitalesSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = models.Usuarios.objects.all()
    serializer_class = serializers.UsuariosSerializer

class UpdateUsuariosView(generics.UpdateAPIView):
    ueryset = models.Usuarios.objects.all()
    serializer_class = serializers.UsuariosSerializer

class DeleteUsuariosView(generics.DestroyAPIView):
    ueryset = models.Usuarios.objects.all()
    serializer_class = serializers.UsuariosSerializer
    
""" class RolesViewSet(viewsets.ModelViewSet):
    queryset = models.Roles.objects.all()
    serializer_class = serializers.RolesSerializer

class UpdateRolesView(generics.UpdateAPIView):
    ueryset = models.Roles.objects.all()
    serializer_class = serializers.RolesSerializer

class DeleteRolesView(generics.DestroyAPIView):
    ueryset = models.Roles.objects.all()
    serializer_class = serializers.RolesSerializer """


