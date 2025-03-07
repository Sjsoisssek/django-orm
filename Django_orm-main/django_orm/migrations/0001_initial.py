# Generated by Django 5.1.4 on 2024-12-21 15:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_role', models.CharField(choices=[('a', 'admin'), ('u', 'user')], max_length=1)),
                ('full_role', models.CharField(choices=[('a', 'admin'), ('u', 'user')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_orm.role')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_orm.role')),
            ],
        ),
    ]
