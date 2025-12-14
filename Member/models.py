from django.db import models

# Create your models here.
class Member(models.Model):
    ho = models.CharField(max_length=100, null=True, verbose_name='Họ')
    ten = models.CharField(max_length=100, null=True, verbose_name='Tên')
    student_id = models.IntegerField(max_length=6, unique=True, verbose_name='Mã số học sinh')
    diem_cong_anh = models.IntegerField(default=0, verbose_name='Điểm cộng Anh')
    diem_cong_van = models.IntegerField(default=0, verbose_name='Điểm cộng Văn')
    slug = models.SlugField(unique=True)
    class Gender(models.TextChoices):
        MALE = 'M', 'Nam'
        FEMALE = 'F', 'Nữ'
    gender = models.CharField(
        max_length=2,
        choices=Gender.choices,
        default=Gender.MALE,
        verbose_name='Giới tính'
    )
    def __str__(self):
        return f"{self.ho} {self.ten}"