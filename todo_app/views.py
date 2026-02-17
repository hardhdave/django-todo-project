from django.shortcuts import render,redirect,get_object_or_404

from .models import Todo

# Create your views here.

def todo_list(request):
    tasks = Todo.objects.all()
    return render(request, 'todo_list.html', {'tasks':tasks})


def add_todo(request):
    if request.method == "POST":
        title =  request.POST['title']
        description= request.POST['description']

        Todo.objects.create(title = title, description = description)


        return redirect ('/')
    
    return render (request, 'add_todo.html')

def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id)

    if todo.is_submitted:

        return redirect('/')

    if request.method == "POST":
        todo.title= request.POST['title']
        todo.description  = request.POST['description']
        todo.save()
        return redirect('/')

    return render(request, 'edit_todo.html', {'todo': todo})



def mark_complete(request, id):

    todo = get_object_or_404(Todo, id=id)

    if not todo.is_submitted:
        todo.completed= True

        todo.save()


    return redirect('/')

def delete_todo(request,id):
    todo = get_object_or_404(Todo,id=id)

    todo.delete()


    return redirect ('/')


    