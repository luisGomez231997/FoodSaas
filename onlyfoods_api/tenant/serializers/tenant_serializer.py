# Library seializer
from rest_framework import serializers
# Model of user
from ..models import Client
from datetime import datetime
"""-------------------------------Tenant Serializers------------------------------------------------"""



class TenantSerializer(serializers.ModelSerializer):
    """Serializer class to object tenant"""

    class Meta:
        model = Client
        fields = '__all__'

    def create(self, validated_data):
        """Create a new user object"""
        tenant = Client.objects.create(
            schema_name=validated_data['schema_name'],
            plan=validated_data['plan'],
            name=validated_data['name'],
            paid_until=validated_data['paid_until'],
            on_trial=validated_data['on_trial'],
            created_on=datetime.now(),
            is_active=validated_data['is_active']
        )
        # Guarda el usuario
        tenant.save()
        return tenant

    def update(self, instance, validated_data):
        """Update a user object"""
        tenant = super().update(instance, validated_data)
        tenant.save()
        return tenant

    def perform_destroy(self, instance):
        """Delete a user object"""
        instance.delete()
        return "ok"


class TenantShowPublicDataSerializer(serializers.ModelSerializer):
    """Serializer class to object user, expose the none sensible attributes"""

    class Meta:
        model = Client
        fields = ['name',
                  'paid_until',
                  'plan',
                  'on_trial',
                  'created_on',
                  'is_active', 'id']
        depth = 1
