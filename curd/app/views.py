from django.shortcuts import render
from .models import Student

def index(req):
  return render(req, 'index.html')


def insertData(req):
  if req.method == 'POST':
    name = req.POST.get('name')
    email = req.POST.get('email')
    age = req.POST.get('age')
    gender = req.POST.get('gender')
    print(name, email, age)
    query = Student(name, email, age, gender)
    query.save()
  return render(req, 'index.html')
