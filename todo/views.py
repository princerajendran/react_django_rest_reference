from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Todo, TodoTags, TodoStatus
from .serializers import TodoSerializer


# Todo views
class TodoListView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoCreateView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def create(self, request, *args, **kwargs):
        try:
            todo_name = request.data.get('todo_name', None)
            status = request.data.get('status', None)
            tags = request.data.get('tags', None)
            if status:
                status = TodoStatus.objects.get(id=str(status))
            if tags:
                tags = TodoTags.objects.filter(id__in=tags)
            todo = Todo.objects.create(todo_name=todo_name,
                                       status=status)
            todo.tags.set(tags)
            serializer = TodoSerializer(todo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class TodoRetrieveView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoUpdateView(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def update(self, request, *args, **kwargs):
        try:
            todo = Todo.objects.get(pk=kwargs['pk'])
            todo_name = request.data.get('todo_name', None)
            status = request.data.get('status', None)
            tags = request.data.get('tags', None)
            if status:
                status = TodoStatus.objects.get(id=str(status))
            if tags:
                tags = TodoTags.objects.filter(id__in=tags)
            if todo_name:
                todo.todo_name = todo_name
            if status:
                todo.status = status
            if todo_name:
                todo.tags.set(tags)
            todo.save()
            serializer = TodoSerializer(todo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class TodoDeleteView(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
