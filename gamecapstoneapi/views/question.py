import base64
from datetime import datetime
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, status
from gamecapstoneapi.models import Question
from gamecapstoneapi.models import Solution
from django.db.models import Q


class QuestionView(ViewSet):
    """ Question Views """

    def retrieve(self, request, pk):
        """Handle GET requests for single question
        Returns:
            Response -- JSON serialized question"""
        try:
            question = Question.objects.get(pk=pk)
            serializer = QuestionSerializer(question)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Question.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all questions
        Returns:
            Response -- JSON serialized list of questions
        """
        questions = Question.objects.all()
        search_text = self.request.query_params.get('search', None)
        difficulty = self.request.query_params.get('difficulty', None)
        if search_text is not None:
            questions = Question.objects.filter(
                Q(label__contains=search_text))
        if difficulty is None:
            questions = Question.objects.filter(
                difficulty=difficulty)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk):
        """handle put"""
        question = Question.objects.get(pk=pk)
        question.label = request.data["label"]
        question.difficulty = request.data["difficulty"]
        question.save()
        question.solution.clear()
        question.solution.add(*request.data['solution'])
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        """Handle POST operations"""
        question = Question.objects.create(
                label=request.data["label"],
                difficulty=request.data["difficulty"]
            )
        question.solution.add(*request.data['solution'])
        serializer = QuestionSerializer(question)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class QuestionSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Question
        fields = ('id', 'label', 'difficulty', 'solution')
        depth = 2
