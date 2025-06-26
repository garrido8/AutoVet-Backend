"""
URL configuration for database project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include 
from client_user import views as client_views
from staff import views as staff_views
from pet import views as pet_views
from appointment import views as appoinment_views
from answers import views as answers_views
from message import views as message_views
from conversation import views as conversation_views
from reassignment import views as reassignment_views
from appointmentmessage import views as appointment_message_views
from appointmentShare import views as appointment_share_views
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView, SpectacularAPIView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # API Schema
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    
    # Swagger UI
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    # Redoc UI
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    # Admin
    path('admin/', admin.site.urls),

    # Clients
    path('clients/', client_views.client_list, name='client-list'),
    path('clients/<int:pk>/', client_views.client_detail, name='client-detail'),

    # Staff (workers + admins)
    path('staff/', staff_views.staff_list, name='staff-list'),
    path('staff/<int:pk>/', staff_views.staff_detail, name='staff-detail'),

    # Pets
    path('pet/', pet_views.pet_list, name='pet-list'),
    path('pet/<int:pk>/', pet_views.pet_detail, name='pet-detail'),
    path('pet/by-owner/<int:propietario>/', pet_views.pets_by_owner, name='pets-by-owner'),

    # Appointments
    path('appoinment/', appoinment_views.appoinment_list, name='appoinment-list'),
    path('appoinment/<int:pk>/', appoinment_views.appoinment_detail, name='appoinment-detail'),

    # Answers
    path('answer/', answers_views.answer_list, name='answer-list'),
    path('answer/<int:pk>/', answers_views.answer_detail, name='answer-detail'),

    # Messages
    path('messages/', message_views.message_list, name='message-list'),
    path('messages/<int:pk>/', message_views.message_detail, name='message-detail'),

    # Conversations
    path('conversations/', conversation_views.conversation_list, name='conversation-list'),
    path('conversations/<int:pk>/', conversation_views.conversation_detail, name='conversation-detail'),

    # Reassignments
    path('reassignments/', reassignment_views.reassignment_list, name='reassignment-list'),
    path('reassignments/<int:pk>/', reassignment_views.reassignment_detail, name='reassignment-detail'),

    # Appointment Messages
    path('appointment-messages/', appointment_message_views.appointment_message_list, name='appointment-message-list'),
    path('appointment-messages/<int:pk>/', appointment_message_views.appointment_message_detail, name='appointment-message-detail'),

    # Appointment Shares
    path('shares/', appointment_share_views.appointment_share_list, name='appointment-share-list'),
    path('shares/<int:pk>/', appointment_share_views.appointment_share_detail, name='appointment-share-detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

