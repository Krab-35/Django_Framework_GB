from users.models import User, UserProfile
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.all()
        for user in users:
            user_profile = UserProfile.objects.create(user=user)
            user_profile.save()
