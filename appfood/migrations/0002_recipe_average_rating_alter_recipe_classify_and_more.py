# Generated by Django 5.1.3 on 2024-12-01 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='average_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='classify',
            field=models.CharField(choices=[('snacks', 'Món Ăn Vặt'), ('vegetarian', 'Chay'), ('Asian', 'Món Á'), ('European', 'Món Âu'), ('grill', 'Nướng'), ('appetizer', 'Khai Vị'), ('dessert', 'Tráng Miện')], max_length=10),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
