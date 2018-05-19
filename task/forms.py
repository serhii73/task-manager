import datetime

from django import forms
from django.forms import DateInput

from task.models import LabelTask, Task, Category

ME_OR_MY_TASK = (('me', 'Tasks assigned to me',), ('my', 'The tasks I had assigned',))


class CreateTask(forms.ModelForm):
    deadline_task = forms.DateTimeField(required=True, widget=(DateInput(attrs={'type': 'datetime-local'})),
                                        initial=format(datetime.datetime.today(), '%Y-%m-%dT%H:%M'), localize=True,
                                        input_formats=['%Y-%m-%dT%H:%M'])
    label_task = forms.ModelMultipleChoiceField(queryset=LabelTask.objects.all(), required=False,
                                                widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Task
        exclude = ['author', 'created_date']


class WhoCategoryTaskForm(forms.Form):
    who_form = forms.ChoiceField(choices=ME_OR_MY_TASK, widget=forms.RadioSelect)
    category_form = forms.ModelChoiceField(queryset=Category.objects.all())
