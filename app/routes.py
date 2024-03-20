from rest_framework.routers import DefaultRouter
from app.views import Employeeviewset

router = DefaultRouter()
router.register("employee", Employeeviewset)