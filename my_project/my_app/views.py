# views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import PersonForm

# Initialize data as a global variable for this example
# In a real application, you would use a database
sample_data = [
    {'id': 1, 'name': 'Alice', 'age': 30},
    {'id': 2, 'name': 'Bob', 'age': 25},
    {'id': 3, 'name': 'Charlie', 'age': 35},
]
next_id = 4

def home(request):
    form = PersonForm()
    return render(request, "home.html", {"data": sample_data, "form": form})

def add_person(request):
    global next_id
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            new_person = {
                'id': next_id,
                'name': form.cleaned_data['name'],
                'age': form.cleaned_data['age']
            }
            sample_data.append(new_person)
            next_id += 1
            return redirect('home')
    return redirect('home')

def delete_person(request, person_id):
    global sample_data
    sample_data = [p for p in sample_data if p['id'] != person_id]
    return redirect('home')

def update_person(request, person_id):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            for person in sample_data:
                if person['id'] == person_id:
                    person['name'] = form.cleaned_data['name']
                    person['age'] = form.cleaned_data['age']
                    break
    return redirect('home')