from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Survey, Person, Question, Response, Category
from .serializers import (SurveySerializer, PersonSerializer,
							QuestionSerializer, CategorySerializer,
							ResponseSerializer)

class SurveyViewSet(viewsets.ModelViewSet):
	queryset = Survey.objects.all()
	serializer_class = SurveySerializer

class PersonViewSet(viewsets.ModelViewSet):
	queryset = Person.objects.all()
	serializer_class = PersonSerializer

class QuestionViewSet(viewsets.ModelViewSet):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer

class ResponseViewSet(viewsets.ModelViewSet):
	queryset = Response.objects.all()
	serializer_class = ResponseSerializer

class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer