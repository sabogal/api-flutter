from rest_framework import serializers
from login.models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['password', 'username', 'name', 'last_name' ,'document','number_phone']
        
    def to_representation(self, instance):
       
        return {
            'id': instance.id,
            'name': instance.name,
            'last_name': instance.last_name,
            'email': instance.username,
            'phone': instance.number_phone,
            'document': instance.document,
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
    
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'last_name': instance.last_name,
            'username': instance.username,
            'phone': instance.number_phone,
            'Document': instance.document,
        }