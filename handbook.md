# Sổ tay dự án (Project Handbook) & Nhật ký làm việc

> [!IMPORTANT]
> **Yêu cầu đối với AI ở phiên làm việc mới:**
> Hãy đọc kỹ tài liệu này trước khi thực hiện bất cứ chỉnh sửa nào trong mã nguồn của dự án. Đây là tài liệu lưu trữ trạng thái hiện tại, các sửa đổi cấu trúc và quy trình triển khai.

---

## 1. Nhật ký phiên làm việc (2026-05-28)

### Các công việc đã hoàn thành:
- **Sửa lỗi nút đóng (Close Button) của Chatbot**: 
  - Khắc phục sự cố nút "X" trên cửa sổ chatbot (`#close-chatbot-window`) không thể click được.
  - **Nguyên nhân**: Các vòng tròn bong bóng trang trí dạng `absolute` trong tiêu đề header đè lên nút tắt do thiếu lớp xếp chồng (`z-index`) và không có thuộc tính xuyên thấu sự kiện chuột.
  - **Cách xử lý**: Đã thêm class `pointer-events-none` vào các thẻ trang trí và thêm class `relative z-10` vào nút tắt trong file [index.html](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/WEB-DU%20AN%20CA%20NHAN/index.html).
- **Thiết kế & Triển khai phiên bản Demo phong cách Apple**:
  - Tạo bản sao demo tại file [index_apple_demo.html](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/WEB-DU%20AN%20CA%20NHAN/index_apple_demo.html).
  - Tối ưu hóa giao diện theo triết lý thiết kế của Apple:
    - **Header**: Giảm chiều cao từ `h-20` xuống `h-14`, sử dụng nền kính mờ `backdrop-blur-lg` và thay thế nút đăng ký bằng nút dạng viên thuốc (Pill-shape) tối giản.
    - **Hero Section**: Thay thế phông nền gradient phức tạp bằng phông nền xám sáng/tối thuần khiết (`#FAFAFA` / `#000000`), chữ không chân (Sans-serif) mảnh dẻ tương phản cao, loại bỏ đường viền đỏ cứng và sử dụng nút bấm dạng viên thuốc phẳng.
    - **Chatbot Window**: Chuyển tiêu đề khung chat sang dạng kính mờ tinh tế thay cho dải màu đỏ/xanh gradient cũ, làm lại nút đóng tròn và các nút gợi ý thành các viên thuốc bo tròn mềm mại.
  - Đã đẩy (push) lên GitHub và deploy thành công lên Vercel:
    - **Trang chính**: [https://web-du-an-ca-nhan.vercel.app](https://web-du-an-ca-nhan.vercel.app)
    - **Trang demo phong cách Apple**: [https://web-du-an-ca-nhan.vercel.app/index_apple_demo.html](https://web-du-an-ca-nhan.vercel.app/index_apple_demo.html)

---

## 2. Các mục cần lưu ý (Notes for Next Sessions)

- **Cấu trúc File dự án**:
  - `index.html`: Bản gốc của dự án (chứa giao diện gốc đã sửa lỗi nút đóng chatbot).
  - `index_apple_demo.html`: Bản thử nghiệm giao diện tối giản, cao cấp theo phong cách Apple.
- **Quy trình Deploy**:
  - Dự án kết nối tự động Vercel qua GitHub. Bất cứ khi nào push lên nhánh `main` của remote `origin`, Vercel sẽ tự động build lại.
  - Nếu cần deploy thủ công bằng Vercel CLI trên môi trường Windows của người dùng, hãy chạy qua Command Prompt bằng lệnh: `cmd.exe /c "npx -y vercel --prod --yes"` (không chạy trực tiếp trong PowerShell do rào cản Execution Policy).
- **Quy tắc định dạng mã nguồn**:
  - Giữ nguyên định dạng kết thúc dòng CRLF (`\r\n`) khi ghi file để tránh xung đột định dạng mã nguồn hiện tại của dự án.
