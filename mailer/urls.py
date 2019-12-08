from django.urls import include, path
from mailer import views
app_name = 'mailer'

urlpatterns = [
    path('compose/', views.compose_mail, name="compose_mail"),
]