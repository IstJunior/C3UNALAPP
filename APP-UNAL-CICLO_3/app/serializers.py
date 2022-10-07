from rest_framework import serializers
from .models import Familiar, HistoriaClinica, Medicos, Pacientes, SignosVitales, Usuarios

class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Familiar
        fields='__all__'


class MedicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicos
        fields = '__all__'

class PacientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = '__all__'
        
class Signos_vitalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignosVitales
        fields = '__all__'
        
        
class Historia_clinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriaClinica
        fields = '__all__'

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'

        
        