from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from .models import UserAccount
User = get_user_model()

from djoser.serializers import UserSerializer



class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')
        



class usuario_serializador_creado(UserSerializer):
    label = serializers.SerializerMethodField()
    value = serializers.CharField(source='id', read_only=True)
    def get_label(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    class Meta:
        model = UserAccount
        fields = ('id', 'email', 'first_name', 'last_name','is_rectora','is_investigacion','is_docente','is_administrativo3','label','value','is_adminBolsa','is_adminBiblioteca','is_adminInventario','is_coor_estrategico')
        #fields = '__all__'



