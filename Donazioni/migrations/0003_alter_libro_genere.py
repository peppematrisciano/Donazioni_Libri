from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Donazioni', '0002_amministratore_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='genere',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Donazioni.genere'),
        ),
    ]