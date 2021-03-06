# Generated by Django 2.2.7 on 2019-11-30 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('bike', '0004_auto_20191130_1558'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('t_taskid', models.AutoField(primary_key=True, serialize=False)),
                ('t_taskcreated', models.DateTimeField(auto_now_add=True)),
                ('t_isactive', models.BooleanField(default=True)),
                ('t_istaskcomplete', models.BooleanField(default=False)),
                ('t_bikeid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bike.Bike')),
                ('t_customeroderid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.CustomerOrder')),
            ],
            options={
                'db_table': 'tblTask',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('s_scheduleid', models.AutoField(primary_key=True, serialize=False)),
                ('s_starttime', models.TimeField()),
                ('s_endtime', models.TimeField()),
                ('s_scheduledate', models.DateTimeField()),
                ('s_isactive', models.BooleanField(default=True)),
                ('s_employeeid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Employee')),
                ('s_taskid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='taskschedule.Task')),
            ],
            options={
                'db_table': 'tblSchedule',
            },
        ),
    ]
