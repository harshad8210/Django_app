from django.shortcuts import render, redirect
from django.views import View

from .forms import AppDetailsForm, EnvDetailsForm
from .models import AppDetails, EnvironmentDetails

class AppDetailsView(View):
    """
    View to display app details
    """
    def get(self, request):
        app_form = AppDetailsForm()
        return render(request, 'app_details/home.html', {'app_form': app_form})

    def post(self, request):
        app_form = AppDetailsForm(request.POST)
        if app_form.is_valid():
            app_details_obj, created = AppDetails.objects.get_or_create(app_name=app_form.cleaned_data['app_name'],
                                                                        database_type=app_form.cleaned_data[
                                                                            'database_type'],
                                                                        framework=app_form.cleaned_data['framework'],
                                                                        region=app_form.cleaned_data['region'],
                                                                        plan_type=app_form.cleaned_data['plan_type'])
            if created:
                print(f"Created App Details.")

            else:
                print(f"App Details already exist.")
            return redirect('add_env_variable', app_details_obj.id)
        else:
            return render(request, 'app_details/home.html', {'app_form': app_form})


class AddEnvironmentVariableView(View):
    """
    View to add environment variables
    """
    def get(self, request, app_id):
        app_obj = AppDetails.objects.get(id=app_id)
        app_env_var = app_obj.env_vars.all()
        env_vars = {}
        if app_env_var:
            for env_var in app_env_var:
                env_vars[env_var.key] = env_var.value
        env_details_form = EnvDetailsForm()
        return render(request, 'app_details/env_var.html',
                      {'env_details_form': env_details_form, 'env_dict': env_vars, 'app_id': app_id})

    def post(self, request, app_id):
        app_obj = AppDetails.objects.get(id=app_id)
        app_env_var = app_obj.env_vars.all()
        env_details_form = EnvDetailsForm()
        form = EnvDetailsForm(request.POST)
        env_vars = {}
        if app_env_var:
            for env_var in app_env_var:
                env_vars[env_var.key] = env_var.value

        if form.is_valid():
            env_name = form.cleaned_data['key']
            env_value = form.cleaned_data['value']

            env_key_exist = EnvironmentDetails.objects.filter(key=env_name, app_name=app_obj)
            if env_key_exist:

                env_key = env_key_exist.first()
                env_key.value = env_value
                env_key.save()
                print(f"env key {env_key.key} already exist. So updating it.")

            else:
                app_env_var, created = EnvironmentDetails.objects.get_or_create(key=env_name, value=env_value,
                                                                                app_name=app_obj)

                if created:
                    app_obj.env_vars.add(app_env_var)
                    print(f"Successfully added environment variable {env_name}")

            app_env_var = app_obj.env_vars.all()

            for env_var in app_env_var:
                env_vars[env_var.key] = env_var.value

            return render(request, 'app_details/env_var.html',
                          {'env_details_form': env_details_form, 'env_dict': env_vars, 'app_id': app_id})
        else:
            print(form.errors, "Error occurred while saving data")
            return render(request, 'app_details/env_varx.html',
                          {'env_details_form': env_details_form, 'env_dict': env_vars, 'app_id': app_id})


class DeleteEnvironmentVarView(View):
    """
    View to delete environment variables
    """
    def post(self, request, env_key, app_id):
        app_obj = AppDetails.objects.get(id=app_id)
        env_var = EnvironmentDetails.objects.get(key=env_key, app_name=app_obj)
        env_var.delete()

        app_env_var = app_obj.env_vars.all()
        env_vars = {}
        if app_env_var:
            for env_var in app_env_var:
                env_vars[env_var.key] = env_var.value
        env_details_form = EnvDetailsForm()
        return render(request, 'app_details/env_var.html',
                      {'env_details_form': env_details_form, 'env_dict': env_vars, 'app_id': app_id})
