from django.core.exceptions import PermissionDenied


class GroupRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.groups.filter(name='staff_shoppingapp').exists():
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied