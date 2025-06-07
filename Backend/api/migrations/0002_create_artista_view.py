from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            sql='''
                CREATE VIEW view_artista AS
                SELECT id, nombre, alias, genero, pais
                FROM api_artista;
            ''',
            reverse_sql='''
                DROP VIEW IF EXISTS view_artista;
            '''
        ),
    ]
