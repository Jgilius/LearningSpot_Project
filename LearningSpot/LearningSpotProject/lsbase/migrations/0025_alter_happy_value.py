# Generated by Django 3.2.14 on 2022-08-09 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lsbase', '0024_alter_learning_intention_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='happy',
            name='value',
            field=models.CharField(choices=[('no', 'no'), ('yes', 'yes')], default='yes', max_length=10),
        ),
    ]