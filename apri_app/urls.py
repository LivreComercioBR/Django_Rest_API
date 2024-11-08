from django.urls import path
from .views import CreateUser, UserList, ListUsers, UpdateUser, DeleteUser
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('create_user/', CreateUser.as_view(), name='create'),
    path('user_detail/<int:pk>/', UserList.as_view(), name='user_detail'),
    path('list_users/', ListUsers.as_view(), name='list_users'),
    path('update_user/<int:pk>/', UpdateUser.as_view(), name='update_user'),
    path('delete_user/<int:pk>/', DeleteUser.as_view(), name='delete_user'),

]
