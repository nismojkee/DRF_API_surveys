from rest_framework import serializers
from .models import Person, Question, Survey, Response, Category, AnswerRadio, AnswerSelect, AnswerSelectMultiply, AnswerText

class SurveySerializer(serializers.ModelSerializer):
	class Meta:
		model = Survey
		fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Person
		fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'

class ResponseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Response
		fields = '__all__'
