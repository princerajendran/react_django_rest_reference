import uuid
from django.db import models


class TodoStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    todo_status = models.CharField(max_length=150, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.todo_status

    class Meta:
        ordering = ["-created_at", "-updated_at"]
        verbose_name = 'Todo Status'
        verbose_name_plural = 'Todo Status'


class TodoTags(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    todo_tags = models.CharField(max_length=150, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.todo_tags

    class Meta:
        ordering = ["-created_at", "-updated_at"]
        verbose_name = 'Todo Tags'
        verbose_name_plural = 'Todo Tags'


class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    todo_name = models.CharField(max_length=150, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(TodoStatus, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(TodoTags, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.todo_name

    class Meta:
        ordering = ["-created_at", "-updated_at"]
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
