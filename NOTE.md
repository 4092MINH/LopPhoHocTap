SETUP DJANGO
============

---

*Nguồn: [W3S](https://www.w3schools.com/django/index.php) và [Django Documentation](https://docs.djangoproject.com/en/6.0/intro/)*


CÁC LỆNH CHECK PHIÊN BẢN
----------------------------

### PYTHON

```
python --version
```

### PIP

```
pip --version
```

### DJANGO

```
py -m django --version
```

CÁC LỆNH TẢI VỀ
-------------------

### PIP

```
python get-pip.py
```

> [!Caution]
> Phải tải [gói pip](https://quantrimang.com/url?u=aHR0cHM6Ly9ib290c3RyYXAucHlwYS5pby9nZXQtcGlwLnB5) hoặc [gói pip cho python 3.2](https://quantrimang.com/url?u=aHR0cHM6Ly9ib290c3RyYXAucHlwYS5pby8zLjIvZ2V0LXBpcC5weQ%3D%3D) về trước

### TẢI VỀ DJANGO

```
python -m pip install django
```

---

SETUP DỰ ÁN
=============

---

TẠO DỰ ÁN MỚI
-----------------

```
django-admin startproject <Name project>
```

CHẠY DỰ ÁN
-------------

```
python manage.py runserver
```

Sau đó ấn vào đường link mà terminal phản hồi

TẠO APP
--------

```
python manage.py startapp <Name app>
```

---

MODEL-VIEW-TEMPLATE-URL
=======================

---

VIEW
----

> [!Note]
> View là tập hợp những hàm chuyên phụ trách xử lý cách yêu câu http

Chúng được tạo ở trong file `views.py` và có format như sau:

```py
from django.shortcuts import render

# Create your views here.
```

Hãy thử thay thế nó bằng nội dung như sau

```python
from django.shortcuts import render
from django.http import HttpResponse

def members(request):
     return HttpResponse("Hello world!")
```

Khi này thì nếu bạn **gọi hàm** này ra thì nó sẽ **phản hồi** thông điệp *Hello World*

> [!Warning]
> Hiện giờ nó vẫn chưa hiện phản hồi đâu. Nếu muốn hiện thì phải dùng một thứ làm cầu nối

URL
---

> [!nOTE]
> Url nó giống như một cầu nối để **kết nối** các views lại với nhau

Chúng nằm ở trong file `urls.py` **cùng thư mục** với file `views.py` và có format như sau:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'), # views.members thì members phải là tên view, không phải tên app
]
```

> [!Caution]
> Việc kết nối này mới chỉ có quy mô nằm trong **nội bộ app** thôi. Ta cần phải kết nối file này với file `urls.py` tổng **nằm ngay dưới** thư mục chính của project với format như sau:
>
> ```py
> from django.contrib import admin
> from django.urls import include, path
>   
> urlpatterns = [
>   path('', include('members.urls')), # Cái này mới là tên app :)
>   path('admin/', admin.site.urls),
> ]
> ```

Lúc này thì khi chạy dự án thì nó sẽ ra kết quả *Hello World*

TEMPLATE
--------

- Template là những trang html giúp phản hồi lại các yêu cầu http từ người dùng
- Nó nằm trong thư mục template và thư mục đó cũng **nằm trong** app members

Ta tạo tạm một file `index.html` như sau

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Hello</h1>
    Ta vừa mới tạo xong một template rồi đó
</body>
</html>
```

Sau đó, ta chỉnh sửa phản hồi trong phần views như sau:

```py
from django.shortcuts import render
from django.http import HttpResponse

def members(request):
     return render(request, 'index.html')
```

> [!caution]
> Nếu chúng ta muốn thực hiện những dự án phức tạp hơn thì ta phải thêm app vào trong `setting.py` để hệ thống dễ dàng kiểm soát bằng cách thêm tên app vào phần `INSTALLED_APP[]`

Sau đó thì ta chạy lệnh sau

```
python manage.py makemigration
python manage.py migrate
```

MODEL
-----

Một class trong model là một cái bảng trong databasse

TẠO MỘT MODEL
---------------

Trước tiên, trong Member ta mở file và ghi đoạn sau

```py
from django.db import models

class ModelMember(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
```

- Mục đầu tiên là `firstname` là một `CharField` chứa firstname
- `lastname` tương tự

Sau khi tạo xong một model thì ta thực hiện cặp lệnh makemigrations vào

---

DJANGO ADMIN
============

---

Django Admin là công cụ tuyệt vời giúp chúng ta thay đổi database một cách dễ dàng hơn

TẠO TÀI KHOẢN VÀ TRUY CẬP VÀO ADMIN SITE
----------------------------------------------

Thực hiện lệnh sau

```
python manage.py createsuperuser
```

Và chúng ta điền thông tin vào

Sau đó, ta chạy dự án và ở url ta thêm `/admin` là đến giao diện đăng nhập

CÁCH THÊM MODEL
-----------------

Chúng ta ghi đoạn code sau

```py
from django.contrib import admin
from .models import ModelMember
# Register your models here.

# minhpnk - Homnayemdotnha@23

admin.site.register(ModelMember)
```

Lúc này, khi quay lại thì ta đã thấy phần cập nhật member

CÁCH THAY ĐỔI NHÃN MODEL
----------------------------

Rất đơn giản, ta chỉ cần thêm một hàm `__str__()` vào trong model là ok

```py
from django.db import models

# Create your models here.
class ModelMember(models.Model):
    ho = models.CharField(max_length=255)
    ten = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ho} {self.ten}"
```

CÁCH THAY ĐỔI GIAO DIỆN CỦA TRANG ADMIN
--------------------------------------------

Ta có thể dùng `admin.site` để thay đổi giao diện như `title`, `header`, `index_title`

```py
from django.contrib import admin
from .models import Member

admin.site.site_header = "Hệ thống quản lý học sinh"
admin.site.site_title = "Quản lý học sinh"
admin.site.index_title = "Chúc một ngày tốt lành"
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'student_id', 'diem_cong', 'slug']
    search_fields = ['name', 'email', 'student_id']
    prepopulated_fields = {'slug': ('name',)} # Auto-generate slug from name field

admin.site.register(Member, MemberAdmin)
```

CÁCH THÊM MỤC HIỂN THỊ VÀ MỤC TÌM KIẾM
-----------------------------------------------

Tạo một hàm tên là `MemberAdmin()` và làm như sau

```py
from django.contrib import admin
from .models import ModelMember

class MemberAdmin(admin.ModelAdmin):
    list_display = ('codeforces_id', 'org')
    search_fields = ('ho', 'ten', 'codeforces_id')
admin.site.register(ModelMember, MemberAdmin)
```

TỪ MODEL CHO ĐẾN SẢN PHẨM
==============================

Bài này sẽ giúp chúng ta cách trình bày dữ liệu từ model lên html

TẠO TEMPLATE
-------------

Sau khi tạo model, thì ta làm một file html như sau

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Học sinh trong lớp thầy Thái</h1>
    <ul>
        {% for x in hocsinh %}
            <li>{{x.ho}} {{x.ten}}</li> <!--Cái này ta gọi là biến-->
        {% endfor %} <!--Những cái trong %% được gọi là Django Tag-->
    </ul>
</body>
</html>
```

CHỈNH SỬA VIEW
----------------

Ta phải bỏ model vào view. Trong file views ta phải import tên model và gửi nó sang template như sau:

```py
from django.shortcuts import render
from django.http import HttpResponse
from .models import ModelMember

def members(request):
     hocsinh = ModelMember.objects.all()
     return render(request, 'index.html', {'hocsinh': hocsinh})
```

CÁCH TẠO PAGE THÔNG TIN CHI TIẾT
====================================

TEMPLATE
--------

Ta vẫn cứ làm như cũ

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Học sinh trong lớp thầy Thái</h1>
    <ul>
        {% for x in hocsinh %}
            <li>{{x.ho}} {{x.ten}}</li>
        {% endfor %}
    </ul>

</body>
</html>
```

VIEWS
-----

Ta thêm hàm mới như sau

```py
def detail(request, member_id): # Đây là id mà lệnh sẽ gửi vào
    member = ModelMember.objects.get(id=member_id) # Nó sẽ lấy lệnh tương ứng
    return render(request, 'detail.html', {'hocsinh': member})
```

URLS
----

Ta cũng thêm đường link nhưng mà ta chỉnh sửa một chút

```py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.members),
    path('detail/<int:member_id>', views.detail, name='member_detail'),
]
```

CÁCH ẤN VÀO TÀI KHOẢN THÌ NÓ HIỂN THỊ THÔNG TIN
---------------------------------------------------------

Ta chỉnh sửa như sau. Cụ thể, ta thêm một cái `<a>` với đường link tương ứng là được

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Học sinh trong lớp thầy Thái</h1>
    <ul>
        {% for x in hocsinh %}
            <li><a href="detail/{{x.id}}">{{x.ho}} {{x.ten}}</a></li>
        {% endfor %}
    </ul>

</body>
</html>
```
CÁCH TẠO MỘT TRANG PAGE KHUNG
=
TẠO PAGE KHUNG
-

- Đầu tiên, ta tạo một file `master.html` và thiết lập sẵn những cấu hình cần thiết.
- Sẽ có một số chỗ ta phải thay đổi thì ta dùng `{% block <content> %}` với `<content>` là tag ta gán
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" type="images/png" href="{% static 'images/logo.png' %}"/>
    <title>{% block title %}{% endblock %}</title>
    {% block cssfile %}
    {% endblock %}
</head>
<body>
    <div class="header-box">
        <img src="{% static 'images/logo.png' %}" alt="Logo" class="logo-img">
        <h1><a href = "/"><b>Trang quản lý học sinh</b></a></h1>
    </div>
    {% block content %}
    {% endblock %}
</body>
</html>
```
LIÊN KẾT VỚI CÁC TRANG KHÁC
-
Để dùng được file này ở các trang web, 
- ở mỗi trang web ta thêm `{% extends 'master.html'}` 
- Và ta bắt đầu điền các block tương ứng như sau
```html
{% extends "master.html" %}
{% load static %}
{% block cssfile %}
    <link rel="stylesheet" href="{% static 'style/index.css' %}">
{% endblock %}
{% block title %}
    Quản lý học sinh
{% endblock %}
{% block content %}
    <div class="container">
        <h2 style="margin-top: 0; color: #555; border-bottom: 2px solid #eee; padding-bottom: 10px;">
            Danh sách học sinh
        </h2>
        <ul>
            {% for x in members %}
                <li>
                    <a href="details/{{x.slug}}">{{x.student_id}} - {{x.ho}} {{x.ten}}</a> 
                </li>
            {% endfor %}
        </ul>

    </div>
{% endblock %}
```



CÁCH DEPLOY DỰ ÁN
====================
[Link tham khảo](https://render.com/docs/deploy-django)
### Bước 1: Chuẩn bị file và thư viện (Tại máy local)

Render cần một server production (Gunicorn) và thư viện quản lý file tĩnh (WhiteNoise).

1.  **Cài đặt các thư viện cần thiết:**
    Mở terminal tại dự án và chạy:
    ```bash
    pip install gunicorn whitenoise dj-database-url psycopg2-binary
    ```
    *   `gunicorn`: Web Server để chạy Django trên production.
    *   `whitenoise`: Để Render hiển thị được CSS/JS/Images.
    *   `dj-database-url`: Để tự động cấu hình database.
    *   `psycopg2-binary`: Driver cho PostgreSQL.

2.  **Xuất file requirements:**
    ```bash
    pip freeze > requirements.txt
    ```

3.  **Tạo file `build.sh`:**
    Tạo một file tên `build.sh` ở thư mục gốc (cùng cấp với `manage.py`) để Render biết cần làm gì khi build:
    ```bash
    #!/usr/bin/env bash
    # exit on error
    set -o errexit

    pip install -r requirements.txt

    python manage.py collectstatic --noinput
    python manage.py migrate
    ```
    *Lưu ý: Nếu bạn dùng Windows, hãy đảm bảo file này lưu dưới định dạng **LF** (Unix) chứ không phải CRLF (Windows), hoặc cứ tạo file này nhưng khi push lên Git thì nhớ lệnh: `git update-index --chmod=+x build.sh`.*

---

### Bước 2: Cấu hình `settings.py`

Mở file `settings.py` và sửa các phần sau:

**1. Cho phép host:**
Render sẽ cấp cho bạn một tên miền đuôi `.onrender.com`.
```python
import os

# Thay vì hardcode, ta lấy từ biến môi trường, nếu không có thì mặc định là list rỗng
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')

if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
else:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']
```

**2. Cấu hình WhiteNoise (Static files):**
Tìm phần `MIDDLEWARE` và thêm dòng này vào **ngay sau** `SecurityMiddleware`:
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Thêm dòng này
    # ...
]
```
Cấu hình Static ở cuối file:
```python
STATIC_URL = 'static/'
# Đường dẫn nơi gom file tĩnh
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Engine nén file
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

**3. Cấu hình Database:**
Sửa lại phần `DATABASES` để nó tự động chuyển sang PostgreSQL khi lên Render:
```python
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        # Mặc định dùng sqlite nếu không tìm thấy biến môi trường DATABASE_URL (lúc chạy local)
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'),
        conn_max_age=600
    )
}
```

---

### Bước 3: Đẩy code lên GitHub
Push toàn bộ code của bạn lên một repository trên GitHub (đảm bảo đã có file `requirements.txt` và `build.sh`).

---

### Bước 4: Tạo Database trên Render

1.  Đăng nhập [Render Dashboard](https://dashboard.render.com/).
2.  Bấm **New +** -> chọn **PostgreSQL**.
3.  Đặt tên (ví dụ: `my-django-db`).
4.  Chọn Region (nên chọn Singapore cho gần Việt Nam).
5.  Chọn gói **Free**.
6.  Bấm **Create Database**.
7.  Đợi một chút để nó khởi tạo. Sau khi xong, hãy copy dòng **Internal Database URL** (bắt đầu bằng `postgres://...`). Bạn sẽ cần nó ở bước sau.

---

### Bước 5: Tạo Web Service trên Render (Deploy Django)

1.  Quay lại Dashboard, bấm **New +** -> chọn **Web Service**.
2.  Chọn **Build and deploy from a Git repository** -> Kết nối với GitHub repo của bạn.
3.  **Điền thông tin cấu hình:**
    *   **Name:** Tên dự án (ví dụ: `my-django-app`).
    *   **Region:** Chọn giống region của Database (Singapore).
    *   **Branch:** `main` (hoặc `master`).
    *   **Runtime:** Python 3.
    *   **Build Command:** `./build.sh`
    *   **Start Command:** `gunicorn project_name.wsgi:application`
        *(Thay `project_name` bằng tên thư mục chứa file `settings.py` của bạn. Ví dụ thư mục là `mysite` thì lệnh là `gunicorn mysite.wsgi:application`).*
4.  **Chọn gói:** Free.
5.  **Cấu hình biến môi trường (Environment Variables):**
    Bấm vào nút **Advanced** hoặc cuộn xuống phần **Environment Variables**, thêm các biến sau:
    *   `DATABASE_URL`: Paste cái link **Internal Database URL** bạn vừa copy ở Bước 4.
    *   `SECRET_KEY`: Điền một chuỗi ký tự ngẫu nhiên dài dài.
    *   `DEBUG`: `False` (Quan trọng để bảo mật).
    *   `PYTHON_VERSION`: `3.9.0` (hoặc 3.10.0 tùy version bạn dùng local).
6.  Bấm **Create Web Service**.

---

### Bước 6: Tạo Superuser (Admin)

Sau khi Render báo deploy thành công (Status: Live), bạn cần tạo tài khoản admin để đăng nhập `/admin`.

1.  Trong trang quản lý Web Service trên Render, chọn tab **Shell** (menu bên trái).
2.  Đợi nó kết nối, sau đó gõ lệnh:
    ```bash
    python manage.py createsuperuser
    ```
3.  Điền username, email, password như bình thường.

### Lưu ý quan trọng về gói Free của Render
1.  **Chế độ ngủ đông (Spin down):** Nếu dùng gói Free, sau 15 phút không có ai truy cập, web sẽ "ngủ". Khi bạn truy cập lại, sẽ mất khoảng **30-50 giây** để web khởi động. Đừng lo, sau đó nó sẽ nhanh bình thường.
2.  **Database Free:** Gói database Free của Render hiện tại thường chỉ tồn tại trong **90 ngày** (hết hạn sẽ bị xóa hoặc yêu cầu nâng cấp). Nếu bạn muốn dùng lâu dài miễn phí database, hãy dùng **Neon.tech** hoặc **Supabase** để lấy link Database rồi dán vào Render, thay vì tạo database trực tiếp trên Render.