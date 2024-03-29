# Generated by Django 5.0.1 on 2024-02-28 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='portfolio_models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('top_portfolio', models.BooleanField(default=False)),
                ('author', models.CharField(max_length=50, null=True)),
                ('position', models.CharField(max_length=50, null=True)),
                ('author_detail', models.CharField(max_length=50, null=True)),
                ('time_start', models.DateField()),
                ('time_end', models.DateField()),
                ('link', models.CharField(max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/portfolio/portfolio_main_img')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='images/portfolio/portfolio_2img')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='images/portfolio/portfolio_3img')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='images/portfolio/portfolio_4img')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='images/portfolio/portfolio_5img')),
                ('paragraph1', models.CharField(max_length=255, null=True)),
                ('paragraph2', models.CharField(max_length=255, null=True)),
                ('paragraph3', models.CharField(max_length=255, null=True)),
                ('paragraph4', models.CharField(max_length=255, null=True)),
                ('paragraph5', models.CharField(max_length=255, null=True)),
                ('paragraph6', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
