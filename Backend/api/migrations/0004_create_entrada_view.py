from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_create_cliente_view'),
    ]

    operations = [
        migrations.RunSQL(
            sql='''
                CREATE VIEW view_entrada AS
                SELECT id,
                       tipo_entrada,
                       precio,
                       cantidad_disponible
                FROM api_entrada;
            ''',
            reverse_sql='''
                DROP VIEW IF EXISTS view_entrada;
            '''
        ),
    ]
