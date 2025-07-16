from rest_framework import serializers
from .models import Student, Question, Answer

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email']

class AnswerSerializer(serializers.ModelSerializer):
    created_by = StudentSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = ['id', 'content', 'created_by', 'created_at']

class QuestionSerializer(serializers.ModelSerializer):
    created_by = StudentSerializer(read_only=True)
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'created_by', 'answers']
