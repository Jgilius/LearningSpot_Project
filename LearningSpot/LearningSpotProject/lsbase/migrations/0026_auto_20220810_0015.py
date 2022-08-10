# Generated by Django 3.2.14 on 2022-08-10 00:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lsbase', '0025_alter_happy_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='happy',
            name='value',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='yes', max_length=10),
        ),
        migrations.AlterField(
            model_name='learning_intention',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='learning_intention',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='auth.user'),
        ),
        migrations.AlterField(
            model_name='learning_intention',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]