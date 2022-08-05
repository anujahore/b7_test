# Generated by Django 3.0 on 2022-08-04 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_board_main', '0002_remove_subscription_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='jobs',
            new_name='job',
        ),
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together={('user', 'job')},
        ),
    ]