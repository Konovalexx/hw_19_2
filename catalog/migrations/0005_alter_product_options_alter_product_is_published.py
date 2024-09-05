# Generated by Django 5.0.7 on 2024-09-04 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_alter_product_options_alter_product_is_published"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "permissions": [
                    ("can_unpublish_product", "Может отменить публикацию продукта"),
                    (
                        "can_change_product_description",
                        "Может изменить описание любого продукта",
                    ),
                    (
                        "can_change_product_category",
                        "Может изменить категорию любого продукта",
                    ),
                ]
            },
        ),
        migrations.AlterField(
            model_name="product",
            name="is_published",
            field=models.BooleanField(default=False, verbose_name="Признак публикации"),
        ),
    ]
