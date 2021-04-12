# Generated by Django 3.1.7 on 2021-04-12 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=3000, null=True)),
                ('logo', models.FileField(blank=True, null=True, upload_to='')),
                ('phone', models.CharField(blank=True, max_length=3000, null=True)),
                ('email', models.CharField(blank=True, max_length=3000, null=True)),
                ('address', models.CharField(blank=True, max_length=3000, null=True)),
                ('facebook', models.CharField(blank=True, max_length=3000, null=True)),
                ('twitter', models.CharField(blank=True, max_length=3000, null=True)),
                ('instagram', models.CharField(blank=True, max_length=3000, null=True)),
                ('website', models.CharField(blank=True, max_length=3000, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(blank=True, max_length=3000, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('project_type', models.CharField(choices=[('D', 'DIGITAL PROJECT'), ('P', 'PHYSICAL PROJECT')], max_length=3000)),
                ('location', models.CharField(blank=True, max_length=3000, null=True)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField(auto_now_add=True)),
                ('images', models.FileField(blank=True, null=True, upload_to='')),
                ('Videos', models.FileField(blank=True, null=True, upload_to='')),
                ('status', models.CharField(choices=[('P', 'PENDING'), ('R', 'REJECTED'), ('C', 'COMPLETED')], max_length=3000)),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.contractor')),
                ('subscribers', models.ManyToManyField(related_name='Subscribers', to='account.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
        ),
    ]