# Generated by Django 3.2.14 on 2022-08-08 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lsbase', '0009_remove_learning_intentions_student_response'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='learning_intention_teacher',
            new_name='learning_intention_teach',
        ),
    ]
