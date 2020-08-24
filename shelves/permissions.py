from rest_framework import permissions


class IsAuthenticatedOrCreateOnly(permissions.BasePermission):
    """
    Custom permission to only allow authenticated users to fetch.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

        return request.method == 'POST'
