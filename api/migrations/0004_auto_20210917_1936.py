# Generated by Django 3.2.6 on 2021-09-17 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210912_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='teammember',
            name='type',
            field=models.CharField(choices=[('Coordinator', 'Coordinator'), ('Co-Coordinator', 'Co-Coordinator'), ('General Secretary-Tech', 'General Secretary-Tech'), ('Publicity and Core Team Coordinator', 'Publicity and Core Team Coordinator'), ('Publicity and Core Team Co-Coordinator', 'Publicity and Core Team Co-Coordinator'), ('Designing Team Coordinator', 'Designing Team Coordinator'), ('Designing Team Co-Coordinator', 'Designing Team Co-Coordinator'), ('Sponsor and Marketing Team Coordinator', 'Sponsor and Marketing Team Coordinator'), ('Sponsor and Marketing Team Co-Coordinator', 'Sponsor and Marketing Team Co-Coordinator'), ('Web Development Team Coordinator', 'Web Development Team Coordinator'), ('Web Development Team Co-Coordinator', 'Web Development Team Co-Coordinator')], default='Coordinator', max_length=100),
        ),
    ]
