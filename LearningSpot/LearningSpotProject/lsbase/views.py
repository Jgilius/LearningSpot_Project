from django.shortcuts import redirect, render
from .models import LTComplete, LTInProgress, LTNeedHelp, LTNotStarted, Learning_Intention, Happy_Select, Learning_Task, Sad_Select, Unsure_Select

def index(request):
    return render(request, 'index.html')

def student(request):
    qs = Learning_Intention.objects.all()
    lt = Learning_Task.objects.all()
    user = request.user

    context = {
        'qs':qs,
        'lt':lt,
        'user':user,
    }

    return render (request,'student.html', context)


def teacher(request):
    learning_intentions = Learning_Intention.objects.all()

    dynamic_content = {'learning_intentions' : learning_intentions}

    return render(request, 'teacher.html', dynamic_content)


def learning_intention(request):
    qs = Learning_Intention.objects.all()
    user = request.user

    context = {
        'qs':qs,
        'user':user,
    }

    return render (request,'student.html', context)


def happy_select(request):
    user = request.user 
    if request.method == 'POST':
        learning_intention_id = request.POST.get('learning_intention_id')
        learning_intention_obj = Learning_Intention.objects.get(id=learning_intention_id)

        if user in learning_intention_obj.happy.all():
            learning_intention_obj.happy.remove(user)
        else:
            learning_intention_obj.happy.add(user)

        
        happy, created = Happy_Select.objects.get_or_create(user=user, learning_intention_id=learning_intention_id)

        if not created:
            if happy.value == 'Select':
                happy.value = 'Unselect'
            else: 
                happy.value = 'Select'
        
        happy.save()

    return redirect('student')



def unsure_select(request):
    user = request.user
    if request.method == 'POST':
        learning_intention_id = request.POST.get('learning_intention_id')
        learning_intention_obj = Learning_Intention.objects.get(id=learning_intention_id)

        if user in learning_intention_obj.unsure.all():
            learning_intention_obj.unsure.remove(user)
        else:
            learning_intention_obj.unsure.add(user)

        
        unsure, created = Unsure_Select.objects.get_or_create(user=user, learning_intention_id=learning_intention_id)

        if not created:
            if unsure.value == 'Select':
                unsure.value = 'Unselect'
            else: 
                unsure.value = 'Select'
        
        unsure.save()

    return redirect('student')



def sad_select(request):
    user = request.user
    if request.method == 'POST':
        learning_intention_id = request.POST.get('learning_intention_id')
        learning_intention_obj = Learning_Intention.objects.get(id=learning_intention_id)

        if user in learning_intention_obj.sad.all():
            learning_intention_obj.sad.remove(user)
        else:
            learning_intention_obj.sad.add(user)

        
        sad, created = Sad_Select.objects.get_or_create(user=user, learning_intention_id=learning_intention_id)

        if not created:
            if sad.value == 'Select':
                sad.value = 'Unselect'
            else: 
                sad.value = 'Select'
        
        sad.save()

    return redirect('student')


def learning_task(request):
    lt = Learning_Task.objects.all()
    user = request.user

    context = {
        'lt':lt,
        'user':user,
    }

    return render (request,'student.html', context)

def inprogress_select(request):
    user = request.user 
    if request.method == 'POST':
        learning_task_id = request.POST.get('learning_task_id')
        learning_task_obj = Learning_Task.objects.get(id=learning_task_id)

        if user in learning_task_obj.inprogress.all():
            learning_task_obj.inprogress.remove(user)
        else:
            learning_task_obj.inprogress.add(user)

        
        inprogress, created = LTInProgress.objects.get_or_create(user=user, learning_task_id=learning_task_id)

        if not created:
            if inprogress.value == 'Select':
                inprogress.value = 'Unselect'
            else: 
                inprogress.value = 'Select'
        
        inprogress.save()

    return redirect('student')

def notstarted_select(request):
    user = request.user 
    if request.method == 'POST':
        learning_task_id = request.POST.get('learning_task_id')
        learning_task_obj = Learning_Task.objects.get(id=learning_task_id)

        if user in learning_task_obj.notstarted.all():
            learning_task_obj.notstarted.remove(user)
        else:
            learning_task_obj.notstarted.add(user)

        
        notstarted, created = LTNotStarted.objects.get_or_create(user=user, learning_task_id=learning_task_id)

        if not created:
            if notstarted.value == 'Select':
                notstarted.value = 'Unselect'
            else: 
                notstarted.value = 'Select'
        
        notstarted.save()

    return redirect('student')

def needhelp_select(request):
    user = request.user 
    if request.method == 'POST':
        learning_task_id = request.POST.get('learning_task_id')
        learning_task_obj = Learning_Task.objects.get(id=learning_task_id)

        if user in learning_task_obj.needhelp.all():
            learning_task_obj.needhelp.remove(user)
        else:
            learning_task_obj.needhelp.add(user)

        
        needhelp, created = LTNeedHelp.objects.get_or_create(user=user, learning_task_id=learning_task_id)

        if not created:
            if needhelp.value == 'Select':
                needhelp.value = 'Unselect'
            else: 
                needhelp.value = 'Select'
        
        needhelp.save()

    return redirect('student')

def complete_select(request):
    user = request.user 
    if request.method == 'POST':
        learning_task_id = request.POST.get('learning_task_id')
        learning_task_obj = Learning_Task.objects.get(id=learning_task_id)

        if user in learning_task_obj.complete.all():
            learning_task_obj.complete.remove(user)
        else:
            learning_task_obj.complete.add(user)

        
        complete, created = LTComplete.objects.get_or_create(user=user, learning_task_id=learning_task_id)

        if not created:
            if complete.value == 'Select':
                complete.value = 'Unselect'
            else: 
                complete.value = 'Select'
        
        complete.save()

    return redirect('student')