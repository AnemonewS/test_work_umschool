from rest_framework.permissions import BasePermission

from main_app.models import UserRole


class IsUserPermission(BasePermission):
    message = 'Вы должны быть авторизованы как пользователь!'

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == UserRole.USER.value


class IsAuthorPermission(BasePermission):
    message = 'Вы должны быть авторизованы как автор!'

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == UserRole.AUTHOR.value
