from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from employees.views import EmployeeViewSet, DepartmentViewSet
from attendance.views import AttendanceViewSet, PerformanceViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

router = DefaultRouter()
router.register('employees', EmployeeViewSet)
router.register('departments', DepartmentViewSet)
router.register('attendance', AttendanceViewSet)
router.register('performance', PerformanceViewSet)

schema_view = get_schema_view(
   openapi.Info(title="Employee API", default_version='v1'),
   public=True,
   permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
