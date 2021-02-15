# Generated by Django 3.1.6 on 2021-02-15 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='제목')),
                ('desc', models.TextField(verbose_name='설명')),
                ('category', models.CharField(choices=[('language', '어학'), ('job', '취업'), ('NCS', '고시/공무원'), ('programming', '프로그래밍'), ('certificate', '자격증'), ('other', '기타')], max_length=100, verbose_name='분류')),
                ('private', models.IntegerField(choices=[(0, '전체 공개'), (1, '친구 공개'), (2, '나만 보기')], verbose_name='공개 상태')),
                ('status', models.IntegerField(blank=True, choices=[(0, '대기 중'), (1, '진행 중'), (2, '완료')], null=True, verbose_name='진행 상태')),
                ('min_pp', models.PositiveIntegerField(verbose_name='최소 인원')),
                ('max_pp', models.PositiveIntegerField(verbose_name='최대 인원')),
                ('duration', models.PositiveIntegerField(verbose_name='기간')),
                ('start_date', models.DateField(verbose_name='시작일')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='생성일')),
                ('invitation_key', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EnrollmentDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chEnrollment_set2', to='challenge.challenge', verbose_name='챌린지')),
            ],
        ),
    ]
