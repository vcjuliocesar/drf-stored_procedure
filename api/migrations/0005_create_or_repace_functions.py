from django.db import migrations

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