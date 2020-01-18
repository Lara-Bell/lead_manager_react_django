from rest_framework import viewsets, permissions
from . import models
from . import serializers


class LeadViewSet(viewsets.ModelViewSet):
    # queryset = models.Lead.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = serializers.LeadSerializer

    def get_queryset(self):
        return self.request.user.leads.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)