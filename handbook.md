# Sổ tay dự án (Project Handbook) & Nhật ký làm việc

> [!IMPORTANT]
> **Yêu cầu đối với AI ở phiên làm việc mới (Đọc để tiết kiệm Token):**
> 1. Hãy đọc duy nhất tài liệu này để nắm bắt tiến độ. **KHÔNG** chạy lệnh tìm kiếm toàn bộ codebase (`grep_search` hoặc `find`) để tránh tiêu tốn Token không cần thiết.
> 2. Chỉ truy cập trực tiếp các file được liệt kê dưới đây khi được yêu cầu sửa đổi.
> 3. Trạng thái hiện tại đã hoàn tất và được deploy sạch. Chờ yêu cầu mới từ người dùng ở phiên làm việc tiếp theo.

---

## 1. Nhật ký phiên làm việc (2026-05-29)

### Các công việc đã hoàn thành:
1. **Tối ưu hóa Bảng giá / Gói dịch vụ (Pricing Table)**:
   - Loại bỏ các biểu tượng emoji không phù hợp với chuẩn B2B cao cấp.
   - Định hình các nút bấm dạng viên thuốc phẳng (Pill-shape): Gói Starter & Premium dùng nút viền xám sáng tối giản; Gói Standard (Nổi bật) dùng nút đen tuyền sang trọng làm điểm nhấn chính.
   - Thay checkmark đỏ thành checkmark xám nhẹ thanh lịch để tạo độ tương phản dịu mắt.
2. **Tối ưu hóa mục Sự kiện (Events Section)**:
   - Thay thế các nút hộp vuông màu đỏ đậm thành các nút viên thuốc xám/đen bo tròn sang trọng.
   - Tinh giản định dạng tag chương trình (Ví dụ: *"Chương trình Quốc gia"*, *"Bảng xếp hạng"*) thành các tag bo tròn nền kính mờ `backdrop-blur-md` kết hợp viền hairline siêu mảnh.
3. **Làm lại chân trang (Sitemap Footer) phong cách Apple**:
   - Thay thế footer cơ bản bằng hệ thống Sitemap Grid 4 cột chuẩn Apple giúp phân loại đường dẫn khoa học.
   - Tối giản hóa các icon mạng xã hội và phần bản quyền dưới cùng.
4. **Deploy & Cập nhật**:
   - Toàn bộ thay đổi đã được đẩy lên nhánh `main` và Vercel tự động build/deploy công khai.

---

## 2. Đường dẫn các trang đang hoạt động (Đã được Vercel Deploy công khai)

- 🔗 **Trang chính gốc**: [https://web-du-an-ca-nhan-nkk3sa2sv-lethanhuyen-8639s-projects.vercel.app](https://web-du-an-ca-nhan-nkk3sa2sv-lethanhuyen-8639s-projects.vercel.app)
- 🔗 **Trang Demo Apple**: [https://web-du-an-ca-nhan-nkk3sa2sv-lethanhuyen-8639s-projects.vercel.app/index_apple_demo.html](https://web-du-an-ca-nhan-nkk3sa2sv-lethanhuyen-8639s-projects.vercel.app/index_apple_demo.html)

---

## 3. Các mục lưu ý cho phiên làm việc tiếp theo

- **Vị trí file mã nguồn chính**:
  - `index.html` (Bản gốc đã sửa lỗi chatbot).
  - `index_apple_demo.html` (Bản thiết kế phong cách Apple đã được tối ưu hóa toàn diện).
