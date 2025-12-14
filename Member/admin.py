from django.contrib import admin
from .models import Member
# Register your models here.
# minhpnk - Homnayemdotnha@23
admin.site.site_header = "Hệ thống quản lý học sinh"
admin.site.site_title = "Quản lý học sinh"
admin.site.index_title = "Chúc một ngày tốt lành"
class MemberAdmin(admin.ModelAdmin):
    list_display = ['ten', 'ho', 'gender', 'student_id', 'diem_cong_anh', 'diem_cong_van', 'slug']
    list_filter = ['gender', 'diem_cong_van', 'diem_cong_anh']
    search_fields = ['ten', 'student_id']
    sort_fields = ['ten', 'student_id', 'diem_cong_van', 'diem_cong_anh']
    prepopulated_fields = {'slug': ('ten',)} # Auto-generate slug from name field

admin.site.register(Member, MemberAdmin)