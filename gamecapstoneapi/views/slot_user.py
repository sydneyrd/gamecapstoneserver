import base64
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from gamecapstoneapi.models.slot_user import SlotUser

class SlotUserView(ViewSet):
    """Rare User view"""

    def retrieve(self, request, pk):
        """handle GET requests for a single user
        """

        try:
            user = SlotUser.objects.get(pk=pk)
            serializer = SlotUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except SlotUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all RareUsers

        Returns:
            Response -- JSON serialized list of RareUsers
        """
        slot_users = SlotUser.objects.all().order_by("user__username")
        
        serializer = SlotUserSerializer(slot_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def update(self, request, pk):
        """Response -- Empty body with 204 status code"""
        user = User.objects.get(pk=pk)
        slot_user = SlotUser.objects.get(user=request.auth.user)
        user.first_name = request.data['first_name']
        user.last_name = request.data['last_name']
        user.email = request.data['email']
        slot_user.save()
        user.save()
        serializer = UserSerializer(user)
        serializer = SlotUserSerializer(slot_user)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT) 

    def destroy(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)




    # @action(methods=['put'], detail=True)
    # def change_active_status(self, request, pk):
    #     """Handle PUT requests for a user
        
    #     Response --  200 OK status code"""
    #     rare_user = RareUser.objects.get(pk=pk)
    #     rare_user.user.is_active = not rare_user.user.is_active
    #     rare_user.user.save()
    #     serializer = UserSerializer(rare_user.user)
    #     return Response(serializer.data, status=status.HTTP_200_OK) 


    # @action(methods=["put"], detail=True)
    # def change_staff_status(self, request, pk):
    #     rare_user = RareUser.objects.get(pk=pk)
        
    #     rare_user.user.is_staff = not rare_user.user.is_staff
    #     rare_user.user.save()
    #     serializer = UserSerializer(rare_user.user)
    #     return Response(serializer.data, status=status.HTTP_200_OK)






class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff')
        # ordering =  ['username']

class SlotUserSerializer(serializers.ModelSerializer):
    """JSON serializer for RareUsers"""
    user = UserSerializer()
    class Meta:
        model = SlotUser
        fields = ('id',  'user', 'title', 'score', 'session_score')