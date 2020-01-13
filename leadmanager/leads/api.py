from rest_framework import viewsets, permissions
from . import models
from . import serializers


class LeadViewSet(viewsets.ModelViewSet):
    queryset = models.Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = serializers.LeadSerializer
