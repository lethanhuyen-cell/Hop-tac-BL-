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

// ================================================================
// HÀM CHÍNH: Nhận POST request từ website
// ================================================================
function doPost(e) {
  try {
    // Parse dữ liệu gửi lên
    const data = JSON.parse(e.postData.contents);
    const name = data.name || "(không có tên)";
    const phone = data.phone || "(không có SĐT)";
    const message = data.message || "";
    const source = data.source || "Chatbot Báo Lao Động";
    const timestamp = new Date();

    // --- 1. GHI VÀO GOOGLE SHEET ---
    writeToSheet(timestamp, name, phone, message, source);

    // --- 2. GỬI EMAIL THÔNG BÁO ---
    sendNotificationEmail(timestamp, name, phone, message, source);

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
function writeToSheet(timestamp, name, phone, message, source) {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName(SHEET_NAME);

  // Tạo sheet nếu chưa có
  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
    // Tạo header row
    sheet.appendRow([
      "STT",
      "Thời gian",
      "Họ tên",
      "Số điện thoại",
      "Tin nhắn",
      "Nguồn",
      "Trạng thái"
    ]);
    // Định dạng header
    const headerRange = sheet.getRange(1, 1, 1, 7);
    headerRange.setBackground("#A80000");
    headerRange.setFontColor("#FFFFFF");
    headerRange.setFontWeight("bold");
    sheet.setFrozenRows(1);
    // Độ rộng cột
    sheet.setColumnWidth(1, 50);
    sheet.setColumnWidth(2, 160);
    sheet.setColumnWidth(3, 180);
    sheet.setColumnWidth(4, 130);
    sheet.setColumnWidth(5, 250);
    sheet.setColumnWidth(6, 150);
    sheet.setColumnWidth(7, 120);
  }

  // Số thứ tự
  const lastRow = sheet.getLastRow();
  const stt = lastRow; // row 1 là header, nên lastRow = số bản ghi hiện tại

  // Format thời gian theo VN
  const formattedTime = Utilities.formatDate(
    timestamp,
    "Asia/Ho_Chi_Minh",
    "dd/MM/yyyy HH:mm:ss"
  );

  // Ghi dữ liệu
  sheet.appendRow([
    stt,
    formattedTime,
    name,
    phone,
    message,
    source,
    "Chưa xử lý" // Trạng thái mặc định
  ]);

  // Tô màu dòng mới theo kiểu zebra
  const newRow = sheet.getLastRow();
  if (newRow % 2 === 0) {
    sheet.getRange(newRow, 1, 1, 7).setBackground("#FFF8F0");
  }
}

// ================================================================
// HÀM GỬI EMAIL THÔNG BÁO
// ================================================================
function sendNotificationEmail(timestamp, name, phone, message, source) {
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
      <h1 style="margin-top:12px;">🔔 Có khách hàng mới!</h1>
      <p>Trung tâm Hợp tác Truyền thông – Báo Lao Động</p>
    </div>
    <div class="body">
      <div class="label">Họ và tên</div>
      <div class="value">${name}</div>

      <div class="label">Số điện thoại</div>
      <div class="value phone">📞 ${phone}</div>

      ${message ? `<div class="divider"></div>
      <div class="label">Tin nhắn / Ghi chú</div>
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
