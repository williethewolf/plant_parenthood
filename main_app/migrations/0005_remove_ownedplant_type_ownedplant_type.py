# Generated by Django 4.1.1 on 2022-10-08 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_ownedplant_comments_alter_ownedplant_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ownedplant',
            name='type',
        ),
        migrations.AddField(
            model_name='ownedplant',
            name='type',
            field=models.ForeignKey(default=1, limit_choices_to={'published': True}, on_delete=django.db.models.deletion.CASCADE, to='main_app.dbplant'),
            preserve_default=False,
        ),
    ]
