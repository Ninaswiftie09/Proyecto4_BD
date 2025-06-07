from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_create_artista_view'),
    ]

    operations = [
        migrations.RunSQL(
            sql='''
                CREATE VIEW view_cliente AS
                SELECT id, nombre, email
                FROM api_cliente;
            ''',
            reverse_sql='''
                DROP VIEW IF EXISTS view_cliente;
            '''
        ),
    ]
