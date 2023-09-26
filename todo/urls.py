from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    # Department URLs

    path('todos/', views.TodoListView.as_view(), name='todos-list'),
    path('todo/create/', views.TodoCreateView.as_view(), name='todo-create'),
    path('todo/<uuid:pk>/', views.TodoRetrieveView.as_view(), name='todo-detail'),
    path('todo/<uuid:pk>/update/', views.TodoUpdateView.as_view(), name='todo-update'),
    path('todo/<uuid:pk>/delete/', views.TodoDeleteView.as_view(), name='todo-delete'),
]
