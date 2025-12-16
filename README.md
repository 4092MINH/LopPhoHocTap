# 🏫 ClassMate - Hệ thống Quản lý Lớp Chuyên 4.0

![Project Status](https://img.shields.io/badge/status-active-success.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-1.0.0-orange.svg)

> **Giải pháp "cứu cánh" cho Lớp phó học tập và Ban cán sự lớp.**
> Quản lý điểm cộng, quỹ lớp, trực nhật và hồ sơ học sinh - Tất cả trong một nền tảng duy nhất, minh bạch và hiệu quả.

---

## 📖 Giới thiệu

**ClassMate** là một ứng dụng web được thiết kế đặc biệt để phục vụ công tác quản lý của các lớp chuyên, nơi khối lượng công việc và áp lực học tập cao đòi hỏi sự chính xác và công bằng. Dự án này giúp số hóa các công việc thủ công (như ghi sổ tay, file Excel rời rạc), giúp Ban cán sự tiết kiệm thời gian và giúp các thành viên trong lớp dễ dàng theo dõi tình hình cá nhân.

## ✨ Tính năng chính
> [!Caution]
> Nhiều tính năng trong số này chỉ là dự tính, vẫn đang phát triển

### 1. 📈 Quản lý Điểm cộng & Thi đua (Key Feature)

* **Cập nhật theo thời gian thực:** Lớp phó học tập nhập điểm cộng/trừ ngay trên lớp.
* **Lịch sử chi tiết:** Xem lại lý do cộng/trừ, ngày giờ và người nhập.
* **Bảng xếp hạng:** Tự động tính tổng điểm và xếp hạng thi đua theo tuần/tháng.
* **Minh bạch hóa:** Mọi học sinh đều có thể xem điểm của mình (nhưng không thể sửa).

### 2. 💰 Quản lý Quỹ lớp (Class Fund)

* **Theo dõi thu/chi:** Ghi lại từng khoản thu (tiền photo, quỹ lớp, hoạt động ngoại khóa).
* **Báo cáo tài chính:** Tự động thống kê số dư hiện tại.
* **Danh sách đóng tiền:** Check-list ai đã đóng, ai chưa đóng để dễ dàng nhắc nhở.

### 3. 🧹 Phân công Trực nhật

* **Lịch tự động:** Tự động xếp lịch trực nhật (lau bảng, quét lớp) theo danh sách hoặc ngẫu nhiên.
* **Nhắc nhở:** Hiển thị tổ/nhóm trực nhật của ngày hôm sau.

### 4. 📝 Quản lý Hồ sơ Học sinh

* **Danh bạ lớp:** Lưu trữ thông tin liên lạc, ngày sinh, tổ/nhóm.
* **Sơ đồ lớp:** (Tính năng dự kiến) Hiển thị vị trí chỗ ngồi.

### 5. 📂 Kho tài liệu chung

* Nơi lưu trữ đề cương, file bài tập, thông báo từ giáo viên chủ nhiệm.

---

## 🛠 Công nghệ sử dụng

Dự án được xây dựng dựa trên các công nghệ hiện đại (Ví dụ bên dưới là MERN Stack, bạn hãy sửa lại theo công nghệ bạn dùng):

* **Frontend:** HTML5 & CSS3
* **Backend:** Python (Django/Flask)
* **Database:** MySQL
* **Authentication:** Nothing

---

## 🚀 Cài đặt và Chạy dự án

Hướng dẫn chi tiết để chạy dự án trên máy cá nhân (Localhost):

### Yêu cầu

- VSCode
- Python (Framework Django)
- Git

### Các bước thực hiện

1. Ấn nút Fork ở trên Github
2. Đợi dự án tải về
3. Khi cần chạy thì dùng lệnh

```
python manage.py runserver
```

---

## 🤝 Đóng góp (Contributing)

Dự án luôn hoan nghênh sự đóng góp từ các bạn trong lớp (đặc biệt là đội tuyển Tin học!).

1. Fork dự án.
2. Tạo nhánh tính năng mới (`git checkout -b feature/TinhNangMoi`).
3. Commit thay đổi (`git commit -m 'Thêm tính năng X'`).
4. Push lên nhánh (`git push origin feature/TinhNangMoi`).
5. Tạo Pull Request.

---

## 🛡 Bảo mật & Riêng tư

* Dữ liệu về quỹ lớp và điểm số là nhạy cảm, vui lòng không chia sẻ tài khoản Admin cho người không có nhiệm vụ.
* Dự án cam kết không thu thập dữ liệu cá nhân ngoài mục đích quản lý lớp.

---
KẾT
-
- Chúc công việc các bạn lớp phó nhẹ nhàng hơn nhờ trang web này
- Trang web chỉ đang trong giai đoạn thử nghiệm
- Dự án được phát triển bởi @4092MINH
- Made with ❤️ for Class **10 Tin**
