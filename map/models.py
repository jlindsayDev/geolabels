from django.db import models

class User(models.Model):
  oauth_id = models.CharField(max_length=100)

class Point(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=150)
  longitude = models.DecimalField(decimal_places=7, max_digits=10)
  latitude = models.DecimalField(decimal_places=7, max_digits=10)

  POINT_TYPES = [
    ('LI', 'Liked'),
    ('SA', 'Saved'),
    ('LV', 'Loved'),
    ('FR', 'Friend')
  ]
  models.CharField(blank=True, choices=POINT_TYPES)
