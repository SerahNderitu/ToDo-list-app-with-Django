from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Todo
from .forms import TodoForm


def index(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    form = TodoForm()

    context = {
        "forms": form,
        "list": item_list,
        "title": 'ToDo List',
    }

    return render(request, 'notes/index.html', context)


def remove(request, item_id):  # function to remove item
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "Item was deleted!")
    return redirect('todo')



