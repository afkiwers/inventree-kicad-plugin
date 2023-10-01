# Generated by Django 3.2.21 on 2023-09-29 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventree_kicad', '0004_alter_selectedcategory_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='selectedcategory',
            name='default_value_parameter_template',
            field=models.ForeignKey(blank=True, help_text='Default value parameter template for this category, if not specified for an individual part', null=True, on_delete=django.db.models.deletion.SET_NULL, to='part.partparametertemplate', verbose_name='Default Value Parameter Template'),
        ),
    ]
