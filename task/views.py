from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from task.forms import CreateTask, WhoCategoryTaskForm
from task.models import Task


def to_login_redirect(request):
    """redirect from index"""
    return HttpResponseRedirect('/login')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task/task_detail.html', {'task': task})


from django.http import JsonResponse


@login_required
def create_task(request):
    form = CreateTask(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        form.save_m2m()
        return HttpResponseRedirect(
            '{}?sent=True'.format(reverse('createTask')))
    return render(request, 'task/task.html',
                  {'form': form, 'sent': request.GET.get('sent', False)})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('createTask'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'task/index.html', {})


@login_required
def all_task(request):
    tasks_list = Task.objects.filter(
        Q(executive_man=request.user) | Q(author=request.user)).order_by(
        '-created_date')

    form = WhoCategoryTaskForm(request.POST or None)
    if form.is_valid():
        who_form = form.cleaned_data['who_form']
        category_form = form.cleaned_data['category_form']
        if who_form == 'me':
            tasks_who = tasks_list.filter(executive_man=request.user).filter(
                category_task=category_form)
            return render(request, 'task/task_list.html',
                          {'form': form, 'task_who': tasks_who})

        elif who_form == 'my':
            tasks_who = tasks_list.filter(author=request.user).filter(
                category_task=category_form)
            return render(request, 'task/task_list.html',
                          {'form': form, 'task_who': tasks_who})

    return render(request, 'task/task_list.html',
                  {'form': form, 'tasks_list': tasks_list})


@login_required
def validate_data_form(request):
    name_task = request.GET.get('name_task', None)
    id_category = request.GET.get('id_category', None)
    count_task = Task.objects.filter(
        name_task=name_task,
        category_task__id=id_category).exists()
    if count_task:
        data = {
            'is_taken': count_task,
        }
    else:
        data = {}
    return JsonResponse(data)
