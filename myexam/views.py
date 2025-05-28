from django.shortcuts import render

from .models import ivexam
from django.http import HttpResponse

def exam_list(request):
    return HttpResponse("<h1>Список экзаменов</h1>")
def exam_list(request):
    exams = ivexam.objects.filter(is_public=True)
    context = {
        'exams': exams,
        'title': 'ФИО: Венедиктов Иван Дмитриевич, Группа: 241-671'
    }
    return render(request, 'myexam/exam_list.html', context)