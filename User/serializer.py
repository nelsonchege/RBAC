from rest_framework import serializers

from  .models import MainUsers, SubUsers

class MainUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUsers
        fields = '__all__'

class SubUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubUsers
        fields = '__all__'