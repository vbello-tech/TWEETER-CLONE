# Generated by Django 4.0.6 on 2022-10-09 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_comments_comment_code_alter_post_post_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_code',
            field=models.CharField(default='nz7n7p3zojgukpt1cbki', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_code',
            field=models.CharField(default='ywa37c7i0yuh9pdzod0z', max_length=20),
        ),
    ]