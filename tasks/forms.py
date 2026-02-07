from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'category']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('title', css_class='form-control'),
            Field('due_date', css_class='form-control'),
            Field('category', css_class='form-control'),
            Submit('submit', 'Add Task', css_class='btn btn-primary mt-3')
        )