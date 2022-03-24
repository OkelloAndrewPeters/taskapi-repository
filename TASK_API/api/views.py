from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from rest_framework import viewsets
from api.serializers import TaskSerializer
from .forms import TaskForm
from .models import Task
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
###############################################

"""
class TaskViewset(viewsets.ModelViewSet):
    serializer_class=TaskSerializer
    queryset=Task.objects.all()


"""
def index(request):
     
    item_list = Task.objects.order_by("-date")
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('test')
    form = TaskForm()
 
    page = {
             "forms" : form,
             "list" : item_list,
             "title" : "TASK LIST",
           }
    return render(request, 'index.html', page)



def test(request):
    item_list = Task.objects.order_by("-date")
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('test')
    form = TaskForm()
    page = {
             "list" : item_list,
             "title" : "TASK LIST",
           }
    return render(request, 'test.html', page)

def home(request):
    item_list = Task.objects.order_by("-date")
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = TaskForm()
    page = {
             "list" : item_list,
             "title" : "TASK LIST",
           }
    return render(request, 'home.html', page)

### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
    item = Task.objects.get(id=item_id)
    item.delete()
    messages.info(request, "task removed !!!")
    return redirect('test')

def update(request, item_id):
    item =  get_object_or_404(Task, pk=item_id)
    form = TaskForm(instance=item)
    context = {'item': item, 'form': form}
    
    if request.method == 'POST':
        title = request.POST.get('title')
        details = request.POST.get('details')
        responsible_person = request.POST.get('responsible_person')
        date = request.POST.get('date')
        start_date = request.POST.get('start_date')
        deadline = request.POST.get('deadline')
        created_by = request.POST.get('created_by')
        task_status_summary = request.POST.get('task_status_summary', False)
        

        item.title = title
        item.details = details
        item.responsible_person = responsible_person
        item.date = date
        item.start_date = start_date
        item.deadline = deadline
        item.created_by = created_by
        item.task_status_summary = True if task_status_summary == "on" else False

        
        item.save()

        messages.add_message(request, messages.SUCCESS, "Todo update success")
        return redirect('test')
    
    return render(request, 'update.html', context)

#api views


#CREATE - CRUD
@api_view(['POST'])
def post(request):
        serializer = TaskSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'message': "fghjkl;"})
        serializer.save()
        
        return Response({'status': 200, 'payload': serializer.data, 'message': "success"})
    

#RETRIEVE - CRUD
class TaskView(mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    
    #permission_classes = (IsAuthenticated, )
    
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)

#UPDATE - CRUD
@api_view(['POST'])
def update_task(request, pk):
    item = Task.objects.get(pk=pk)
    data = TaskSerializer(instance=item, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

#DELETE - CRUD
@api_view(['DELETE'])
def delete_task(request, pk):
    person = Task.objects.get(pk=pk)
    person.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
    



