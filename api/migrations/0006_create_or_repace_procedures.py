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