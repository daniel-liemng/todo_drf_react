from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer

# Create your views here.


@api_view(['GET'])
def home(request):
    example = {
        'a': 'dfdf',
        'b': '5455'
    }
    return Response(example)

# Get a list of tasks
@api_view(['GET'])
def taskList(request):

    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)


# Get a single task detail
@api_view(['GET'])
def taskDetail(request, pk):

    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)

    return Response(serializer.data)

# Create a new task
@api_view(['POST'])
def taskCreate(request):

    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


# Update a task
@api_view(['POST'])
def taskUpdate(request, pk):

    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


# Delete a task
@api_view(['DELETE'])
def taskDelete(request, pk):

    task = Task.objects.get(id=pk)

    task.delete()

    return Response('Item deleted successfully!!')
