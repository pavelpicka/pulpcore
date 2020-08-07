# Generated by Django 2.2.13 on 2020-08-07 18:51

from django.db import migrations, models, transaction


def update_download_concurrency(apps, schema_editor):
    with transaction.atomic():
        Remote = apps.get_model('core', 'Remote')
        Remote.objects.filter(download_concurrency=20).update(download_concurrency=10)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_repository_remote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remote',
            name='download_concurrency',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.RunPython(update_download_concurrency),
    ]