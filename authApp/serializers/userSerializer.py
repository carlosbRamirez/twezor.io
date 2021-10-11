from rest_framework import serializers
from authApp.models.user import User
from authApp.models.account import Account
from authApp.serializers.accountSerializer import AccountSerializer
#serializar 
class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
       #serializar de usuario los siguientes campos 
       model = User
       fields = ['id', 'username', 'password', 'name', 'email', 'account']
#deserializar de JSON a un Objeto 
    def create(self, validated_data):
        accountData = validated_data.pop('account')
        userInstance = User.objects.create(**validated_data)
        Account.objects.create(user=userInstance, **accountData)
        return userInstance
#serializar de Objeto a un JSON
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        account = Account.objects.get(user=obj.id)
        return {
                    'id': user.id,
                    'username': user.username,
                    'name': user.name,
                    'email': user.email,
                    'account': {
                        'id': account.id,
                        'balance': account.balance,
                        'lastChangeDate': account.lastChangeDate,
                        'isActive': account.isActive
                    }
                }