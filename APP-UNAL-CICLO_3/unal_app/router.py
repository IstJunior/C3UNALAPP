from app.models import Medicos, Usuarios
from app.serializers import Signos_vitalesSerializer
from app.viewsets import FamiliarViewSet, Historia_clinicaViewSet, MedicosViewSet, PacientesViewSet, SignosVitalesViewSet, UsuariosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('familiar', FamiliarViewSet)
router.register('medicos', MedicosViewSet)
router.register('pacientes', PacientesViewSet)
router.register('historia-clinica', Historia_clinicaViewSet)
router.register('signos-vitales', SignosVitalesViewSet)
router.register('usuarios', UsuariosViewSet)