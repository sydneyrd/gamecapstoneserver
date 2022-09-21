import base64
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from gamecapstoneapi.models.solution import Solution

class SolutionView(ViewSet):
    """Rare User view"""

    def retrieve(self, request, pk):
        """handle GET requests for a single user
        """
        try:
            solution = Solution.objects.get(pk=pk)
            serializer = SolutionSerializer(solution)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Solution.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all RareUsers
        Returns:
            Response -- JSON serialized list of RareUsers
        """
        solution = Solution.objects.all()
        serializer = SolutionSerializer(solution, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def update(self, request, pk):
        """Response -- Empty body with 204 status code"""
        solution = Solution.objects.get(pk=pk)
        solution.label = request.data['label']
        solution.save()
        serializer = SolutionSerializer(solution)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT) 

    def destroy(self, request, pk):
        solution = Solution.objects.get(pk=pk)
        solution.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        """Handle POST operations"""
        solution = Solution.objects.create(
                label=request.data['label']
            )
        serializer = SolutionSerializer(solution)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    # @action(methods=["put"], detail=True)
    # def change_staff_status(self, request, pk):
    #     slot_user = SlotUser.objects.get(pk=pk)
    #     slot_user.user.is_staff = not slot_user.user.is_staff
    #     slot_user.user.save()
    #     serializer = UserSerializer(slot_user.user)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ('id','label')
