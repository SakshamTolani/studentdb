from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isTeacher = serializers.SerializerMethodField(read_only=True)
    isSuperAdmin = serializers.SerializerMethodField(read_only=True)
    isStudent = serializers.SerializerMethodField(read_only=True)
    

    class Meta:
        model = User
        fields = [ '_id', 'username', 'email', 'name', 'isTeacher','isSuperAdmin','isStudent' ]

    def get__id(self, obj):
        return obj.id

    def get_isTeacher(self, obj):
        return obj.is_staff

    def get_isSuperAdmin(self, obj):
        return obj.is_superuser

    def get_isStudent(self,obj):
        return obj.is_superuser==False and obj.is_staff==False

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email

        return name

#Serializer to display what all things should be displayed with the jwt token.
class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isTeacher','isSuperAdmin','isStudent', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
