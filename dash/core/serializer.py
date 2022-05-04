"""
Serializers module

"""
from dash.core.models import *
from rest_framework import serializers

class AssetVulnerabilityMS(serializers.ModelSerializer):
    class Meta:
        model = AssetVulnerability
        fields = '__all__'
