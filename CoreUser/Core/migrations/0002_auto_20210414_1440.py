# Generated by Django 3.1.3 on 2021-04-14 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coreusers',
            options={'verbose_name_plural': 'Users'},
        ),
        migrations.AlterModelOptions(
            name='userlogs',
            options={'get_latest_by': 'created_at', 'verbose_name_plural': 'Logs'},
        ),
        migrations.AlterField(
            model_name='userlogs',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]