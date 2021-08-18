from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()


class UserJsonData(models.Model):
    # user = models.ForeignKey(
    #     StudentProfile, on_delete=models.CASCADE, related_name="student_activity_data")
    country = models.CharField(max_length=500,null=True, blank=True)
    indicator = models.CharField(max_length=500,null=True, blank=True)
    value = models.CharField(max_length=500,null=True, blank=True)
    year = models.CharField(max_length=500,null=True, blank=True)



    def __str__(self):
        return self.country

class LastAccessData(models.Model):
    session_id = models.CharField(max_length=200)
    item_sent = models.PositiveIntegerField(default=50)
    last_access_id = models.CharField(max_length=500,null=True, blank=True)
    




    def __str__(self):
        return self.last_access_id