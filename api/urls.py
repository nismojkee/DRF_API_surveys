from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import routers
from api.views import SurveyViewSet, PersonViewSet, QuestionViewSet, ResponseViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'survey', SurveyViewSet)
router.register(r'persons', PersonViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'response', ResponseViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [
	path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
