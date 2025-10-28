
from djongo import models
import uuid

class Team(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')

class Activity(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=100)
    duration = models.IntegerField()  # minutes
    calories = models.IntegerField()
    date = models.DateField()

class Workout(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.ManyToManyField(User, related_name='workouts')

class Leaderboard(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboards')
    points = models.IntegerField()
    week = models.IntegerField()
