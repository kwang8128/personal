from django.db import models

# Create your models here.

class Text(models.Model):
  art_choices = {
    ('Mountain', 'Mountain'),
    ('Medicine', 'Medicine'),
    ('Divination', 'Divination'),
    ('Physical Inspection', 'Physical Inspection'),
    ('Destiny', 'Destiny'),
    ('NA', 'N/A')
  }
  art = models.CharField(max_length=20, choices=art_choices, default="NA")
  subtype = models.CharField(max_length=50)
  title = models.CharField(max_length=50)
  link = models.URLField(max_length=100)
  desc = models.TextField(blank=True, null=True)
  action_choices = {
    ('D', 'Delete'),
    ('U', 'Update'),
    ('C', 'Create'),
    ('P', 'Published'),
    ('0', 'N/A')
  }
  action = models.CharField(max_length=1, choices=action_choices, default="0")

  def __str__(self):
    return self.title