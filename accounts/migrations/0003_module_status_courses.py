# Generated by Django 4.0 on 2022-02-04 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_module'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=250)),
                ('status', models.BooleanField(default=False)),
                ('modules', models.ManyToManyField(related_name='modules', to='accounts.Module')),
            ],
        ),
    ]
