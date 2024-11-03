from rest_framework.permissions import BasePermission
from django.conf import settings

class AllowSpecificIP(BasePermission):
    allowed_ips = getattr(settings, 'ALLOWED_SWAGGER_IPS', [])

    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        return ip_addr in self.allowed_ips
