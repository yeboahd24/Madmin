# Generated by Django 3.2.4 on 2021-06-20 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('Web Development', 'Web Development'), ('Graphic Design', 'Graphic Design'), ('Tech Gadget', 'Tech Gadget'), ('Other', 'Other')], max_length=300)),
                ('body', models.TextField(max_length=500)),
                ('slug', models.SlugField(max_length=200)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categorys',
            },
        ),
    ]
