from djoser.serializers import  UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreationSerializer

class UserCreationSerializer(BaseUserCreationSerializer):
    class Meta(BaseUserCreationSerializer.Meta):
        fields=['id','username','password','email','first_name','last_name']

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields=['id','username','email','first_name','last_name']