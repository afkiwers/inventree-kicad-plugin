# Generated by Django 3.2.23 on 2023-12-31 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventree_kicad', '0007_auto_20231212_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectedcategory',
            name='footprint_parameter_template',
            field=models.ForeignKey(blank=True, help_text='Footprint parameter template for this category. Overrides the KICAD_FOOTPRINT_PARAMETER setting for this category.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='footprint_kicad_categories', to='part.partparametertemplate', verbose_name='Footprint Parameter Template'),
        ),
    ]