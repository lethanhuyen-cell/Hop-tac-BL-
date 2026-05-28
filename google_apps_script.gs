// ================================================================
// GOOGLE APPS SCRIPT - Báo Lao Động: Nhận form liên hệ
// Hướng dẫn cài đặt:
//   1. Vào https://script.google.com → New project
//   2. Paste toàn bộ code này vào, thay ID sheet nếu cần
//   3. Deploy → Web app → Anyone → Copy URL
// ================================================================

// --- CẤU HÌNH ---
const EMAIL_RECIPIENT = "lethanhuyen@gmail.com";
const SHEET_NAME = "Danh sach lien he";
const SPREADSHEET_ID = "1r0FDeS1NCHifRjyEMXreP7bNsw1qjkJ4iY_WTnKpJmE";

// ================================================================
// HÀM CHÍNH: Nhận POST request từ website
// ================================================================
function doPost(e) {
  try {
    // Parse dữ liệu gửi lên
    const data = JSON.parse(e.postData.contents);
    const name = data.name || "(không có tên)";
    const phone = data.phone || "(không có SĐT)";
    const email = data.email || "";
    const company = data.company || "";
    const message = data.message || "";
    const source = data.source || "Chatbot Báo Lao Động";
    const timestamp = new Date();

    // --- 1. GHI VÀO GOOGLE SHEET ---
    writeToSheet(timestamp, name, phone, email, company, message, source);

    // --- 2. GỬI EMAIL THÔNG BÁO CHO QUẢN TRỊ VIÊN ---
    sendNotificationEmail(timestamp, name, phone, email, company, message, source);

    // --- 3. GỬI BÁO GIÁ TỰ ĐỘNG CHO KHÁCH HÀNG ---
    if (email) {
      sendQuoteToCustomer(email, name, message);
    }

    // Trả về thành công
    return ContentService
      .createTextOutput(JSON.stringify({ status: "success", message: "Đã nhận thông tin!" }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: "error", message: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

// Cho phép GET (để test trên trình duyệt)
function doGet(e) {
  return ContentService
    .createTextOutput(JSON.stringify({ status: "ok", message: "API hoat dong binh thuong!" }))
    .setMimeType(ContentService.MimeType.JSON);
}

// ================================================================
// HÀM GHI VÀO GOOGLE SHEET
// ================================================================
function writeToSheet(timestamp, name, phone, email, company, message, source) {
  const ss = SPREADSHEET_ID ? SpreadsheetApp.openById(SPREADSHEET_ID) : SpreadsheetApp.getActiveSpreadsheet();
  
  // Tự động chọn sheet đầu tiên trong file của bạn
  let sheet = ss.getSheets()[0];
  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
  }

  // Format thời gian theo VN
  const formattedTime = Utilities.formatDate(
    timestamp,
    "Asia/Ho_Chi_Minh",
    "dd/MM/yyyy HH:mm:ss"
  );

  // Ghi dữ liệu đúng thứ tự các cột trong ảnh:
  // Cột A: Họ và tên
  // Cột B: Số điện thoại
  // Cột C: Dịch vụ quan tâm
  // Cột D: Email
  // Cột E: Ngày đăng ký
  // Cột F: Ghi chú (Nguồn gửi)
  sheet.appendRow([
    name,
    phone,
    message,
    email,
    formattedTime,
    source
  ]);
}

// ================================================================
// HÀM GỬI EMAIL THÔNG BÁO CHO QUẢN TRỊ VIÊN
// ================================================================
function sendNotificationEmail(timestamp, name, phone, email, company, message, source) {
  const formattedTime = Utilities.formatDate(
    timestamp,
    "Asia/Ho_Chi_Minh",
    "dd/MM/yyyy - HH:mm"
  );

  const subject = `🔔 [Báo Lao Động] Khách hàng mới: ${name} - ${phone}`;

  const htmlBody = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    body { font-family: 'Segoe UI', Arial, sans-serif; background: #f5f5f5; margin: 0; padding: 20px; }
    .container { max-width: 560px; margin: 0 auto; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1); }
    .header { background: linear-gradient(135deg, #A80000, #8B0000); padding: 24px 28px; color: white; }
    .header h1 { margin: 0; font-size: 18px; font-weight: 700; letter-spacing: 0.5px; }
    .header p { margin: 6px 0 0; font-size: 12px; opacity: 0.8; }
    .body { padding: 28px; }
    .label { font-size: 11px; font-weight: 700; color: #888; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px; }
    .value { font-size: 16px; font-weight: 700; color: #1a1a1a; margin-bottom: 18px; }
    .value.phone { color: #A80000; font-size: 20px; }
    .divider { height: 1px; background: #eee; margin: 18px 0; }
    .meta { background: #f9f9f9; border-radius: 8px; padding: 14px 18px; margin-top: 18px; }
    .meta p { margin: 0; font-size: 12px; color: #666; line-height: 1.8; }
    .footer { padding: 18px 28px; background: #fafafa; border-top: 1px solid #eee; text-align: center; }
    .footer p { margin: 0; font-size: 11px; color: #aaa; }
    .badge { display: inline-block; background: #A80000; color: white; font-size: 10px; font-weight: 700; padding: 3px 10px; border-radius: 20px; text-transform: uppercase; letter-spacing: 1px; }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="badge">Liên hệ mới</div>
      <h1 style="margin-top:12px;">🔔 Có khách hàng mới từ Chatbot/Form!</h1>
      <p>Trung tâm Hợp tác Truyền thông – Báo Lao Động</p>
    </div>
    <div class="body">
      <div class="label">Họ và tên</div>
      <div class="value">${name}</div>

      <div class="label">Số điện thoại</div>
      <div class="value phone">📞 ${phone}</div>

      ${email ? `<div class="label">Email</div><div class="value">${email}</div>` : ''}
      ${company ? `<div class="label">Doanh nghiệp</div><div class="value">${company}</div>` : ''}

      ${message ? `<div class="divider"></div>
      <div class="label">Tin nhắn / Dịch vụ quan tâm</div>
      <div class="value" style="font-size:14px;font-weight:500;color:#333;">${message}</div>` : ''}

      <div class="meta">
        <p>
          🕐 <strong>Thời gian:</strong> ${formattedTime}<br>
          📍 <strong>Nguồn:</strong> ${source}
        </p>
      </div>
    </div>
    <div class="footer">
      <p>Email tự động từ hệ thống Cổng Hợp tác Truyền thông Báo Lao Động<br>
      <strong>web-du-an-ca-nhan.vercel.app</strong></p>
    </div>
  </div>
</body>
</html>
  `;

  // Gửi email
  GmailApp.sendEmail(EMAIL_RECIPIENT, subject, "", {
    htmlBody: htmlBody,
    name: "Cổng Hợp tác Báo Lao Động"
  });
}

// ================================================================
// HÀM GỬI BÁO GIÁ TỰ ĐỘNG CHO KHÁCH HÀNG
// ================================================================
function sendQuoteToCustomer(email, name, message) {
  const service = (message || "").toLowerCase();
  let quoteTitle = "Tài liệu Media Kit & Báo giá 2026 - Báo Lao Động";
  let quoteDetailHtml = "";

  // Phân loại tài liệu và link tải tương ứng
  if (service.indexOf("pr") !== -1) {
    quoteTitle = "Báo giá Dịch vụ bài viết PR & E-magazine 2026";
    quoteDetailHtml = `
      <p>Chúng tôi xin gửi tới Anh/Chị bảng báo giá dịch vụ đăng tải bài viết PR chuyên sâu, E-magazine, phóng sự ảnh và phóng sự truyền hình trên Báo Lao Động điện tử (laodong.vn).</p>
      <p>📍 <strong>Link xem & tải báo giá bài viết PR 2026:</strong> <a href="https://laodong.vn" style="color: #A80000; font-weight: bold; text-decoration: underline;">Tải Báo Giá PR tại đây</a></p>
    `;
  } else if (service.indexOf("banner") !== -1 || service.indexOf("quảng cáo") !== -1) {
    quoteTitle = "Báo giá Vị trí Banner hiển thị & Box chuyên mục 2026";
    quoteDetailHtml = `
      <p>Chúng tôi xin gửi tới Anh/Chị thông tin vị trí hiển thị và báo giá Banner trên trang chủ PC, Mobile cũng như các trang chuyên mục chuyên sâu của Báo Lao Động.</p>
      <p>📍 <strong>Link xem & tải báo giá Banner 2026:</strong> <a href="https://laodong.vn" style="color: #A80000; font-weight: bold; text-decoration: underline;">Tải Báo Giá Banner tại đây</a></p>
    `;
  } else if (service.indexOf("sự kiện") !== -1 || service.indexOf("hội thảo") !== -1) {
    quoteTitle = "Tài liệu Tổ chức & Tài trợ Sự kiện 2026 - Báo Lao Động";
    quoteDetailHtml = `
      <p>Chúng tôi xin gửi tới Anh/Chị thông tin về các giải pháp đồng hành, bảo trợ truyền thông, tổ chức Talkshow/Tọa đàm và tài trợ các Sự kiện lớn thường niên của Báo Lao Động.</p>
      <p>📍 <strong>Link xem thông tin sự kiện & hội thảo:</strong> <a href="https://laodong.vn" style="color: #A80000; font-weight: bold; text-decoration: underline;">Tải tài liệu sự kiện tại đây</a></p>
    `;
  } else {
    // Mặc định gửi Media Kit đầy đủ
    quoteDetailHtml = `
      <p>Chúng tôi xin gửi tới Anh/Chị bộ tài liệu giới thiệu năng lực (Media Kit) kèm Bảng giá tổng hợp các dịch vụ Quảng cáo & Truyền thông năm 2026 của Báo Lao Động.</p>
      <p>📍 <strong>Link xem & tải Media Kit trọn bộ 2026:</strong> <a href="https://laodong.vn" style="color: #A80000; font-weight: bold; text-decoration: underline;">Tải Media Kit 2026 tại đây</a></p>
    `;
  }

  const subject = `📩 [Báo Lao Động] Gửi ${name} ${quoteTitle}`;

  const htmlBody = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    body { font-family: 'Segoe UI', Arial, sans-serif; background: #f9f9f9; margin: 0; padding: 20px; }
    .container { max-width: 560px; margin: 0 auto; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-top: 4px solid #A80000; }
    .body { padding: 32px 28px; color: #333333; line-height: 1.6; }
    .greetings { font-size: 16px; font-weight: bold; color: #1a1a1a; margin-bottom: 12px; }
    .intro { margin-bottom: 20px; font-size: 14px; }
    .content-box { background: #fdf2f2; border-left: 4px solid #A80000; padding: 18px; border-radius: 0 8px 8px 0; margin-bottom: 24px; font-size: 14px; }
    .content-box p { margin: 0 0 10px 0; }
    .content-box p:last-child { margin-bottom: 0; }
    .cta-button { display: inline-block; background: #A80000; color: white !important; font-weight: bold; font-size: 14px; padding: 12px 28px; text-decoration: none !important; border-radius: 6px; box-shadow: 0 4px 10px rgba(168,0,0,0.2); margin-top: 10px; }
    .contact-info { font-size: 13px; color: #666; border-top: 1px solid #eee; padding-top: 20px; margin-top: 28px; }
    .footer { text-align: center; padding: 15px; background: #fafafa; border-top: 1px solid #eee; font-size: 11px; color: #999; }
  </style>
</head>
<body>
  <div class="container">
    <div class="body">
      <div class="greetings">Kính gửi Anh/Chị ${name},</div>
      <div class="intro">
        Lời đầu tiên, Trung tâm Hợp tác Truyền thông – Báo Lao Động xin gửi lời chào trân trọng và lời chúc thành công đến Anh/Chị và Quý doanh nghiệp.
      </div>
      
      <div class="content-box">
        ${quoteDetailHtml}
      </div>
      
      <div class="intro">
        Nếu Anh/Chị cần tư vấn giải pháp truyền thông đo ni đóng giày hoặc nhận báo giá ưu đãi với mức chiết khấu tốt nhất, xin vui lòng liên hệ trực tiếp bộ phận hỗ trợ khách hàng 24/7 của chúng tôi.
      </div>

      <div class="contact-info">
        <strong>Trung tâm Hợp tác Truyền thông - Báo Lao Động</strong><br>
        📞 Hotline hỗ trợ: <strong>024 3 999 8888</strong> / <strong>0904 123 456</strong><br>
        📧 Email: <a href="mailto:hoptactruyenthong@laodong.vn" style="color: #A80000;">hoptactruyenthong@laodong.vn</a><br>
        🏢 Địa chỉ tòa soạn: Số 6 Chùa Bộc, Đống Đa, Hà Nội.
      </div>
    </div>
    <div class="footer">
      Thư được gửi tự động dựa trên yêu cầu từ Chatbot cổng Báo Lao Động.<br>
      © 2026 Trung tâm Hợp tác Truyền thông Báo Lao Động. All rights reserved.
    </div>
  </div>
</body>
</html>
  `;

  // Gửi email
  GmailApp.sendEmail(email, subject, "", {
    htmlBody: htmlBody,
    name: "Cổng Hợp tác Báo Lao Động"
  });
}
