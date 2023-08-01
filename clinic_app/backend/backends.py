from django.contrib.auth.backends import ModelBackend as BaseBackend
from clinic_app.models.accounts import User


class ModelBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None):
        if not username is None:
            try:
                user: User = User.objects.get(username=username)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                pass
