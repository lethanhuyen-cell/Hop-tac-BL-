# Sổ tay dự án (Project Handbook) & Nhật ký làm việc

> [!IMPORTANT]
> **Yêu cầu đối với AI ở phiên làm việc mới (Đọc để tiết kiệm Token):**
> 1. Hãy đọc duy nhất tài liệu này để nắm bắt tiến độ. **KHÔNG** chạy lệnh tìm kiếm toàn bộ codebase (`grep_search` hoặc `find`) để tránh tiêu tốn Token không cần thiết.
> 2. Chỉ truy cập trực tiếp các file được liệt kê dưới đây khi được yêu cầu sửa đổi.
> 3. Trạng thái hiện tại đã hoàn tất và được deploy sạch. Chờ yêu cầu mới từ người dùng ở phiên làm việc tiếp theo.

---

## 1. Nhật ký phiên làm việc (2026-05-28)

### Các công việc đã hoàn thành:
1. **Sửa lỗi nút đóng (Close Button) của Chatbot**:
   - Thêm `pointer-events-none` cho các thẻ trang trí tuyệt đối trong header và `relative z-10` cho nút `#close-chatbot-window` tại file `index.html` và `index_apple_demo.html`.
2. **Thiết kế & Triển khai phiên bản Demo phong cách Apple**:
   - Tạo bản sao demo tại file `index_apple_demo.html`.
   - Thiết lập giao diện tối giản, sang trọng: thu gọn Header (`h-14`), làm mờ kính `backdrop-blur-lg`, đổi nền Hero sang màu xám/đen đơn sắc, phông chữ Sans-serif mảnh tương phản cao và sử dụng nút bấm dạng viên thuốc.
3. **Cấu hình & Mở khóa Vercel**:
   - Gửi yêu cầu PATCH tới REST API Vercel để tắt chế độ bảo mật đăng nhập (`ssoProtection = null`). Giúp link deploy truy cập công khai không bị lỗi 401.
4. **Sửa lỗi đè lớp Bong bóng chào mừng (Bubble)**:
   - Sửa hàm `openChatWithContext()` để tự động gọi `hideBubble()` ẩn bong bóng thoại khi mở khung chat.
5. **Tối ưu hóa hiển thị Gợi ý nhanh (Suggestions)**:
   - Cấu hình tự động ẩn hộp gợi ý `#chatbot-suggestions` ngay khi người dùng chọn một mục hoặc tự gõ tin nhắn gửi đi, giữ cho khung chat gọn gàng và logic.

---

## 2. Đường dẫn các trang đang hoạt động (Đã được Vercel Deploy công khai)

- 🔗 **Trang chính gốc**: [https://web-du-an-ca-nhan-hzczsabyy-lethanhuyen-8639s-projects.vercel.app](https://web-du-an-ca-nhan-hzczsabyy-lethanhuyen-8639s-projects.vercel.app)
- 🔗 **Trang Demo Apple**: [https://web-du-an-ca-nhan-hzczsabyy-lethanhuyen-8639s-projects.vercel.app/index_apple_demo.html](https://web-du-an-ca-nhan-hzczsabyy-lethanhuyen-8639s-projects.vercel.app/index_apple_demo.html)

---

## 3. Các mục lưu ý cho phiên làm việc tiếp theo

- **Vị trí file mã nguồn chính**:
  - `index.html` (Bản gốc đã sửa lỗi chatbot).
  - `index_apple_demo.html` (Bản thiết kế phong cách Apple).
- **Quy tắc thao tác file**:
  - Luôn sử dụng định dạng kết thúc dòng CRLF (`
`) khi cập nhật các file HTML.
  - Vercel được kết nối tự động với GitHub. Đẩy mã nguồn lên nhánh `main` bằng lệnh `git push origin main` sẽ tự động kích hoạt tiến trình deploy.
