from django import forms

framework_choices = (
    ('Vue.js', 'vuejs'),
    ('React', 'react'),
    ('Express.js', 'expressjs'),
    ('Ruby on Rails', 'rubyonrails'),
    ('Django', 'django'),
    ('FastAPI', 'fastapi'),
    ('Flask', 'flask')
)

database_choices = (
    ('PostgreSQL', 'postgres'),
    ('MySQL', 'mysql'),
    ('SQLite', 'sqlite'),
    ('MongoDB', 'mongodb'),
    ('SQL Server', 'sqlserver')

)


class AppDetailsForm(forms.Form):
    app_name = forms.CharField(max_length=50)
    region = forms.CharField(max_length=50)
    framework = forms.ChoiceField(choices=framework_choices)
    plan_type = forms.CharField(max_length=20)
    database_type = forms.ChoiceField(choices=database_choices)


class EnvDetailsForm(forms.Form):
    key = forms.CharField(max_length=20)
    value = forms.CharField(max_length=50)


