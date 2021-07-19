from django.urls import path

from . import views

add_name = "tasks"

urlpatterns = [
    path("", views.index, name='index'),
    path("list/", views.tasks_by_tag, name='list'),
    path("list/tag/<slug:tag_slug>",views.tasks_by_tag, name="list"),
    path("list/create/", views.TaskCreateView.as_view(), name='create'),
    # path("list/create/add-task/", views.add_task, name="api-add-task"),
    path("list/complete/<int:uid>/", views.complete_task, name='complete'),
    path("list/delete/<int:uid>/", views.delete_task, name='delete'),
    path("details/<int:pk>", views.TaskDetailsView.as_view(), name="details"),
    path("edit/<int:pk>", views.TaskEditView.as_view(), name="edit"),
    path("export/", views.TaskExportView.as_view(), name="export"),
]
