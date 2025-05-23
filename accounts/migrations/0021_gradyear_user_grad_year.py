# Generated by Django 5.0.6 on 2024-12-02 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_college_user_college'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='grad_year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.gradyear'),
        ),
    ]
