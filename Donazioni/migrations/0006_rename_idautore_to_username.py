from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Donazioni', '0005_alter_libro_classe_scolastica_alter_libro_materia'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autore',
            old_name='IdAutore',
            new_name='username',
        ),
    ]