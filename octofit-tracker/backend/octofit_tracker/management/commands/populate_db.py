
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
import uuid

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data (avoid unhashable error)
        User.objects.filter(pk__isnull=False).delete()
        Team.objects.filter(pk__isnull=False).delete()
        Activity.objects.filter(pk__isnull=False).delete()
        Workout.objects.filter(pk__isnull=False).delete()
        Leaderboard.objects.filter(pk__isnull=False).delete()

        # Create teams
        marvel = Team.objects.create(id=str(uuid.uuid4()), name='Marvel')
        dc = Team.objects.create(id=str(uuid.uuid4()), name='DC')

        # Create users
        users = [
            User.objects.create(id=str(uuid.uuid4()), name='Peter Parker', email='spiderman@marvel.com', team=marvel),
            User.objects.create(id=str(uuid.uuid4()), name='Tony Stark', email='ironman@marvel.com', team=marvel),
            User.objects.create(id=str(uuid.uuid4()), name='Steve Rogers', email='captainamerica@marvel.com', team=marvel),
            User.objects.create(id=str(uuid.uuid4()), name='Clark Kent', email='superman@dc.com', team=dc),
            User.objects.create(id=str(uuid.uuid4()), name='Bruce Wayne', email='batman@dc.com', team=dc),
            User.objects.create(id=str(uuid.uuid4()), name='Diana Prince', email='wonderwoman@dc.com', team=dc),
        ]

        # Create activities
        Activity.objects.create(id=str(uuid.uuid4()), user=users[0], type='Running', duration=30, calories=300, date='2025-10-28')
        Activity.objects.create(id=str(uuid.uuid4()), user=users[1], type='Cycling', duration=45, calories=400, date='2025-10-27')
        Activity.objects.create(id=str(uuid.uuid4()), user=users[3], type='Swimming', duration=60, calories=500, date='2025-10-26')

        # Create workouts
        workout1 = Workout.objects.create(id=str(uuid.uuid4()), name='Cardio Blast', description='High intensity cardio workout')
        workout2 = Workout.objects.create(id=str(uuid.uuid4()), name='Strength Training', description='Full body strength workout')
        workout1.suggested_for.set([users[0], users[1], users[3]])
        workout2.suggested_for.set([users[2], users[4], users[5]])

        # Create leaderboards
        Leaderboard.objects.create(id=str(uuid.uuid4()), team=marvel, points=250, week=1)
        Leaderboard.objects.create(id=str(uuid.uuid4()), team=dc, points=200, week=1)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
