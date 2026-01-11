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
        MALE = 'Nam', 'Nam' # Trai la cho database phai la hien thi trong admin
        FEMALE = 'Nữ', 'Nữ'
    gender = models.CharField(
        max_length=3,
        choices=Gender.choices,
        default=Gender.MALE,
        verbose_name='Giới tính'
    )
    def __str__(self):
        return f"{self.ho} {self.ten}"

class UpdatePlus(models.Model):
    ho = models.CharField(max_length=100, null=True, verbose_name='Họ')
    ten = models.CharField(max_length=100, null=True, verbose_name='Tên')
    student_id = models.IntegerField(max_length=6, verbose_name='Mã số học sinh')
    additional_english_points = models.IntegerField(default=0, verbose_name='Điểm cộng thêm Anh')
    additional_literature_points = models.IntegerField(default=0, verbose_name='Điểm cộng thêm Văn')
    reason = models.TextField(verbose_name='Lý do cập nhật điểm')
    def __str__(self):
        return f"Update for {self.ho} {self.ten} (ID: {self.student_id})"