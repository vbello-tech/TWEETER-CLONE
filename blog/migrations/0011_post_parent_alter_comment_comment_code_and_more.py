# Generated by Django 4.0.6 on 2022-10-28 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_likes_alter_comment_comment_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parenttweet', to='blog.post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_code',
            field=models.CharField(default='1n2cx28zzzrvlpkf8zup', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_code',
            field=models.CharField(default='zu4jkrze7swx9aj326gg', max_length=20),
        ),
    ]