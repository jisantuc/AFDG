import getpass

from django.core.management.base import BaseCommand
from django.db import transaction
from django.contrib.auth.models import User


class Command(BaseCommand):

    @transaction.atomic
    def handle(self, *args, **kwargs):
        """Create a user from prompts at the command line"""

        username = raw_input('Enter a username:  ')
        password = getpass.getpass('Enter a password:  ')
        password_check = getpass.getpass('Enter password again:  ')

        assert password == password_check, 'Passwords do not match'

        is_superuser = True
        is_staff = True
        is_active = True

        User.objects.create(**{
            'username': username, 'password': password,
            'is_superuser': is_superuser, 'is_staff': is_staff,
            'is_active': is_active
        })
