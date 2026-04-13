from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from django.conf import settings
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all users
        User.objects.all().delete()

        # Sample users (super heroes)
        users = [
            {'username': 'ironman', 'email': 'ironman@marvel.com', 'team': 'marvel'},
            {'username': 'captainamerica', 'email': 'cap@marvel.com', 'team': 'marvel'},
            {'username': 'spiderman', 'email': 'spiderman@marvel.com', 'team': 'marvel'},
            {'username': 'batman', 'email': 'batman@dc.com', 'team': 'dc'},
            {'username': 'superman', 'email': 'superman@dc.com', 'team': 'dc'},
            {'username': 'wonderwoman', 'email': 'wonderwoman@dc.com', 'team': 'dc'},
        ]
        for u in users:
            User.objects.create_user(username=u['username'], email=u['email'], password='password')

        # Create teams, activities, leaderboard, workouts collections using raw pymongo
        db = connection.cursor().db_conn.client[settings.DATABASES['default']['NAME']]
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        teams = [
            {'name': 'marvel', 'members': ['ironman', 'captainamerica', 'spiderman']},
            {'name': 'dc', 'members': ['batman', 'superman', 'wonderwoman']},
        ]
        db.teams.insert_many(teams)

        activities = [
            {'user': 'ironman', 'activity': 'run', 'distance': 5},
            {'user': 'batman', 'activity': 'cycle', 'distance': 10},
        ]
        db.activities.insert_many(activities)

        leaderboard = [
            {'team': 'marvel', 'points': 100},
            {'team': 'dc', 'points': 90},
        ]
        db.leaderboard.insert_many(leaderboard)

        workouts = [
            {'name': 'pushups', 'difficulty': 'easy'},
            {'name': 'squats', 'difficulty': 'medium'},
        ]
        db.workouts.insert_many(workouts)

        # Ensure unique index on email for users
        db['auth_user'].create_index('email', unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
