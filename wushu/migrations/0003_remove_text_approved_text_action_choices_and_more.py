# Generated by Django 5.0.3 on 2024-03-12 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wushu', '0002_text_approved_text_desc_alter_text_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='approved',
        ),
        migrations.AddField(
            model_name='text',
            name='action_choices',
            field=models.CharField(choices=[('D', 'Delete'), ('U', 'Update'), ('C', 'Create'), ('P', 'Published'), ('0', 'N/A')], default='0', max_length=1),
        ),
        migrations.AlterField(
            model_name='text',
            name='art',
            field=models.CharField(choices=[('MO', 'Mountain'), ('ME', 'Medicine'), ('DI', 'Divination'), ('PI', 'Physical Inspection'), ('DE', 'Destiny'), ('NA', 'N/A')], default='NA', max_length=2),
        ),
        migrations.AlterField(
            model_name='text',
            name='link',
            field=models.URLField(max_length=100),
        ),
        migrations.AlterField(
            model_name='text',
            name='subtype',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='text',
            name='title',
            field=models.CharField(max_length=10),
        ),
    ]
