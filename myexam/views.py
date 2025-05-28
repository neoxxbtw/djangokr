from django.shortcuts import render

from .models import ivexam

def exam_list(request):
    exams = ivexam.objects.filter(is_public=True)
    context = {
        'exams': exams,
        'title': 'ФИО: Венедиктов Иван Дмитриевич, Группа: 241-671'
    }
    return render(request, 'exam/exam_list.html', context)