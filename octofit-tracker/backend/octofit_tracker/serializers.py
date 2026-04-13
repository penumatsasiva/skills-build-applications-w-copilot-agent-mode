from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'email', 'team']

class TeamSerializer(serializers.ModelSerializer):
	class Meta:
		model = Team
		fields = ['id', 'name', 'members']

class ActivitySerializer(serializers.ModelSerializer):
	class Meta:
		model = Activity
		fields = ['id', 'user', 'activity', 'distance']

class LeaderboardSerializer(serializers.ModelSerializer):
	class Meta:
		model = Leaderboard
		fields = ['id', 'team', 'points']

class WorkoutSerializer(serializers.ModelSerializer):
	class Meta:
		model = Workout
		fields = ['id', 'name', 'difficulty']
