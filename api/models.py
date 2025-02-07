# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models,connection

# LLamar un pocedimiento desde un modelo
class Usersv2Manager(models.Manager):
    def p_follow_user(self,follower_username,followed_username):
        with connection.cursor() as cursor:
            cursor.execute('CALL follow_user(%s,%s);',[follower_username,followed_username])


class Usersv2(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=100)
    last_connection = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    username = models.CharField(unique=True, max_length=100)
    followers = models.IntegerField()
    following = models.IntegerField()

    objects = Usersv2Manager()

    class Meta:
        db_table = 'usersv2'
