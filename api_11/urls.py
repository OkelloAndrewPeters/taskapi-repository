from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



"""
schema_view = get_schema_view(
   openapi.Info(
      title="Tasks API",
      default_version='v1',
      description="Coseke Tasks API",   
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


router=DefaultRouter()
router.register('tasks',TaskViewset)



urlpatterns = [
    path('',include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

"""

urlpatterns = [
    path('', views.TaskView.as_view(), name=""),
    path('post', views.post, name='post'),
    path('update/<int:pk>/', views.update_task, name='update'),
    path('delete/<int:pk>/', views.delete_task, name='delete'),
]















"""
urlpatterns = [
    #path('update/<str:item_id>/', views.update_tasks, name="update" ),
    path('home', views.home, name='home'),
    path('task', views.index, name='task'),
    path('del/<str:item_id>', views.remove, name="del"),
    #path('post', views.post, name='post'),
    path('test', views.test, name='test'),
    
    path('post/', views.post, name='add-items'),
    path('update/<int:pk>/', views.update_task, name='update'),
    path('delete/<int:pk>/', views.delete_task, name='delete-task'),
    path('', views.TaskView.as_view(), name='all'),

]

"""