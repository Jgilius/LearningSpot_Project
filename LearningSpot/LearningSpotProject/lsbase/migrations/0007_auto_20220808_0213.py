# Generated by Django 3.2.14 on 2022-08-08 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lsbase', '0006_auto_20220808_0207'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='learning_intentions_student',
            options={},
        ),
        migrations.AddField(
            model_name='learning_intentions_student',
            name='reponse',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
