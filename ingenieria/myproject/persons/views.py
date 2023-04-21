from django.shortcuts import render
from .models import Student

# Create your views here.


def my_view(request):
    objs = Student.objects.all()
    print(objs)
    context = {'objs': objs}

    return render(request, 'orm.html', context)
