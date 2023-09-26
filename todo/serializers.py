from rest_framework import serializers
from .models import TodoTags, TodoStatus, Todo


class TodoTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoTags
        fields = ['id', 'todo_tags']


class TodoStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoStatus
        fields = ['id', 'todo_status']


class TodoSerializer(serializers.ModelSerializer):
    status_data = TodoStatusSerializer(read_only=True)
    tags_data = TodoTagsSerializer(read_only=True)
    status = serializers.CharField(source='status.todo_status', read_only=True)

    class Meta:
        model = Todo
        fields = ['id',
                  'todo_name',
                  'status_data',
                  'tags_data',
                  'status',
                  'tags',
                  'created_at',
                  'updated_at']
