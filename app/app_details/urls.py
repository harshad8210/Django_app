from .views import AppDetailsView, AddEnvironmentVariableView, DeleteEnvironmentVarView
from django.urls import path

urlpatterns = [
    path('', AppDetailsView.as_view(), name='home'),
    path('add/env_var/<int:app_id>', AddEnvironmentVariableView.as_view(), name='add_env_variable'),
    path('delete/env_var/<int:app_id>/<env_key>/', DeleteEnvironmentVarView.as_view(), name='delete_env_var')
]