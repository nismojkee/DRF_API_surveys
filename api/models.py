from django.db import models
from django.core.exceptions import ValidationError

class Person(models.Model):
	person_id = models.IntegerField(primary_key = True, unique = True)

class Survey(models.Model):
	name = models.CharField(max_length = 400, null = True, blank = True)
	description = models.TextField(default='')

	def __str__(self):
		return self.name

	def question(self):
		if self.pk:
			return Question.objects.filter(survey = self.pk)
		else:
			return None

class Category(models.Model):
	name = models.CharField(max_length = 400)
	survey = models.ForeignKey(Survey, null = True, blank = True, on_delete = models.DO_NOTHING)

	def __str__(self):
		return self.name

def validate_list(value):
	values = value.split(',')
	if len(values) < 2:
		raise ValidationError('The selected field requires an associated list')

class Question(models.Model):
	TEXT = 'text'
	RADIO = 'radio'
	SELECT = 'select'
	SELECT_MULTIPLE = 'select-multiple'
	
	QUESTION_TYPES = (
		(TEXT, 'text'),
		(RADIO, 'radio'),
		(SELECT, 'select'),
		(SELECT_MULTIPLE, 'select multiple')
	)

	text = models.TextField(default='')
	required = models.BooleanField()
	category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.DO_NOTHING)
	survey = models.ForeignKey(Survey, blank = True, null = True, on_delete = models.DO_NOTHING)
	question_type = models.CharField(max_length = 200, choices = QUESTION_TYPES, default = TEXT)
	choices = models.TextField(
		blank = True,
		null = True,
		help_text = 'Radio, Select or Select Multiple provides a comma-separated list of options'
	)

	def save(self, *args, **kwargs):
		if (self.question_type == Question.RADIO or
				self.question_type == Question.SELECT or
					self.question_type == Question.SELECT_MULTIPLE):
			validate_list(self.choices)
		super(Question, self).save(*args, **kwargs)

	def get_choices(self):
		choices - self.choices.split(',')
		choices_list = []
		for choice in choices:
			choice = choice.strip()
			choices_list.append( (choice, choice) )
			return choices_tuple

	def __str__(self):
		return self.text

class Response(models.Model):
	created = models.DateTimeField(auto_now_add = False)
	updated = models.DateTimeField(auto_now = False)
	survey = models.ForeignKey(Survey, on_delete = models.DO_NOTHING)
	person = models.CharField('Name of Interviewee', max_length = 250)
	response_uuid = models.CharField(max_length=100)

	def __str__(self):
		return ("response %s" & self.response_uuid)
	
class AnswerBase(models.Model):
	question = models.ForeignKey(Question, on_delete = models.DO_NOTHING)
	response = models.ForeignKey(Response, on_delete = models.DO_NOTHING)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	author = models.ForeignKey(Person, on_delete = models.DO_NOTHING)

class AnswerText(AnswerBase):
	body = models.TextField()

class AnswerRadio(AnswerBase):
	body = models.TextField()

class AnswerSelect(AnswerBase):
	body = models.TextField()

class AnswerSelectMultiply(AnswerBase):
	body = models.TextField()
