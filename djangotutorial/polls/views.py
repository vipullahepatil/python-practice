from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Question, Student, Answer
from .serializers import QuestionSerializer

def question_list(request):
    questions = Question.objects.prefetch_related('answers').all()
    return render(request, 'polls/question_list.html', {'questions': questions})

class QuestionListCreateAPIView(APIView):

    def get(self, request):
        questions = Question.objects.prefetch_related('answers').all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        title = request.data.get("title")
        student_id = request.data.get("student_id")

        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=404)

        question = Question.objects.create(title=title, created_by=student)
        serializer = QuestionSerializer(question)
        return Response(serializer.data, status=status.HTTP_201_CREATED)