# Generated by Django 4.0.4 on 2022-06-05 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_app', '0004_alter_applicant_user_staff_discountcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='discountcode',
            name='percentage',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
