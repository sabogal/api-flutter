from rest_framework import serializers
from login.models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['password', 'username', 'name', 'last_name','is_active']
        
    def to_representation(self, instance):
       
        return {
            'contraseña': instance.password,
            'correo_electronico': instance.username,
            'nombre': instance.name,
            'apellido': instance.last_name,
            'estado': instance.is_active,

        }
    def create(self,validated_data):
       create_user = User(**validated_data)
       create_user.set_password(validated_data['password'])
       create_user.save()
       return create_user

    def update(self, instance, validated_data):
        updated_user = super().update(instance,validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user