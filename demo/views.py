import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from demo.models import Students


def hello(request):
    return HttpResponse('hello world!')


def index(req):
    return render(req, 'index.html')


def adds(request):
    student = Students()
    student.name = "tom{}".format(random.randrange(100))
    student.sex = "male"
    student.save()  # 添加要保存
    return HttpResponse('add students {} success!'.format(student.name))


def get_students(req):
    students = Students.objects.all()  # 获取所有数据对象
    context = {
        "students": students,
    }
    return render(req, "index.html", context=context)


def update_students(req):
    students = Students.objects.get(id=3)  # 获取某个数据对象
    students.name = "gss"
    students.save()  # 更新要保存
    return HttpResponse("update student`name is {} success!".format(students.name))


def delete_students(request):
    student = Students.objects.get(id=5)
    student.delete()
    return HttpResponse('delete student {} success!'.format(student.name))
