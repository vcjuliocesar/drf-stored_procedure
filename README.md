# drf-stored_procedure

## Crear modelos apartir de una base de datos ya creada

```shell
    python manage.py inspectdb > models.py
```
Esto genera los modelos basados en la estructura de una la base de datos dentro de un archivo models.py, ese archiso se puede mover dentro de una app de django (api/models.py) por ejemplo

**Nota:** Es recomendable revisar y modificar manualmente los modelos generados, ya que inspectdb puede definir algunos campos como TextField() en lugar de tipos más específicos.

## Crear funciones desde un archivo de migracion

Dentro de la carpeta  migrations se puede crear una archivo que se egcarge de crear funciones

```python
from django.db import migrations
# migrations/0005_create_or_repace_functions.py
class Migration(migrations.Migration):
    
    dependencies = [
        ('api','0004_usersv2_delete_userssn')
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE OR REPLACE FUNCTION get_followers(username_param VARCHAR)
            RETURNS INTEGER
            LANGUAGE plpgsql
            AS $$
            BEGIN
                RETURN (SELECT followers FROM usersv2 WHERE username = username_param);
            END;
            $$;
            """
        ),
    ]
```


## Crear Procedimientos desde un archivo de migracion

Dentro de la carpeta  migrations se puede crear una archivo que se egcarge de crear procedimientos almacenados

```python
# migrations/0006_create_or_repace_procedures.py
from django.db import migrations

class Migration(migrations.Migration):
    
    dependencies = [
        ('api','0005_create_or_repace_functions')
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE OR REPLACE PROCEDURE delete_user(p_id VARCHAR) AS $$
            BEGIN
                DELETE FROM usersv2
                WHERE id = p_id;
            END;
            $$ LANGUAGE plpgsql;
            """
        ),
    ]

```

## Ejecutar un procedimiento almacenado desde un modelo

```python
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

# Uso
Usersv2.objects.p_follow_user(follower_username,followed_username)
```

## Ejecutar funciones o procedimientos usando cursor

```python
from django.db import connection

    with connection.cursor() as cursor:
        cursor.execute('select * from get_range_of_followers(%s,%s);',[min_value, max_value]) 
        users = cursor.fetchall()

    with connection.cursor() as cursor:
        cursor.execute('CALL reset_followers_following(%s);',[username]) 
```