import sys

input_file = r"C:\Users\Admin\Documents\Work_Folders\4_Hoat_Dong_Ca_Nhan\WEB-DU AN CA NHAN\index.html"
APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzTgSd4t4lY-DrWUMz770cXbe1fTTlSGNanoCyefksXqs9XVDwLr-yl58qqAORLXp84/exec"

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

c = content.replace('\r\n', '\n')

# ================================================================
# 1. Add Apps Script URL constant + contact form JS functions
#    Insert BEFORE the closing </script> of the main script
# ================================================================
js_to_add = f"""
            // ================================================================
            // CONTACT FORM - Google Apps Script Integration
            // ================================================================
            const APPS_SCRIPT_URL = "{APPS_SCRIPT_URL}";

            // Show contact form inside chat window
            window.showContactForm = function() {{
                const messagesArea = document.getElementById('chatbot-messages');
                const suggestionsArea = document.getElementById('chatbot-suggestions');

                // Hide suggestions
                if (suggestionsArea) suggestionsArea.classList.add('hidden');

                // Append contact form as a chat message
                const formHtml = `
                <div id="contact-form-bubble" class="flex items-start gap-2.5 animate-fade-in">
                    <div class="w-8 h-8 rounded-full overflow-hidden bg-gray-100 flex-shrink-0 shadow-sm border border-gray-200 dark:border-white/10">
                        <img src="images/laodong_assistant_avatar.png" alt="Consultant" class="w-full h-full object-cover">
                    </div>
                    <div class="flex-1 max-w-[85%]">
                        <div class="bg-white dark:bg-[#1E2530] border border-gray-150 dark:border-slate-800 p-3.5 rounded-2xl rounded-tl-none shadow-sm text-xs text-slate-800 dark:text-gray-200 leading-relaxed font-medium mb-2">
                            Vui lòng để lại thông tin, chuyên viên sẽ liên hệ lại ngay!
                        </div>
                        <div class="bg-white dark:bg-[#1E2530] border border-gray-200 dark:border-slate-800 rounded-2xl rounded-tl-none shadow-sm p-3.5 space-y-2.5">
                            <div>
                                <label class="block text-[10px] font-bold text-slate-500 dark:text-gray-400 uppercase tracking-wider mb-1">Họ và tên *</label>
                                <input type="text" id="cf-name" placeholder="Nguyễn Văn A"
                                    class="w-full text-xs border border-gray-200 dark:border-slate-700 bg-slate-50 dark:bg-[#252d3d] text-slate-800 dark:text-gray-100 rounded-lg px-3 py-2 focus:outline-none focus:border-brand-blue dark:focus:border-brand-blue transition font-medium placeholder-gray-400">
                            </div>
                            <div>
                                <label class="block text-[10px] font-bold text-slate-500 dark:text-gray-400 uppercase tracking-wider mb-1">Số điện thoại *</label>
                                <input type="tel" id="cf-phone" placeholder="0901 234 567"
                                    class="w-full text-xs border border-gray-200 dark:border-slate-700 bg-slate-50 dark:bg-[#252d3d] text-slate-800 dark:text-gray-100 rounded-lg px-3 py-2 focus:outline-none focus:border-brand-blue dark:focus:border-brand-blue transition font-medium placeholder-gray-400">
                            </div>
                            <div>
                                <label class="block text-[10px] font-bold text-slate-500 dark:text-gray-400 uppercase tracking-wider mb-1">Dịch vụ quan tâm</label>
                                <input type="text" id="cf-message" placeholder="Báo giá PR, Banner, Sự kiện..."
                                    class="w-full text-xs border border-gray-200 dark:border-slate-700 bg-slate-50 dark:bg-[#252d3d] text-slate-800 dark:text-gray-100 rounded-lg px-3 py-2 focus:outline-none focus:border-brand-blue dark:focus:border-brand-blue transition font-medium placeholder-gray-400">
                            </div>
                            <button onclick="submitContactForm()"
                                id="cf-submit-btn"
                                class="w-full bg-gradient-to-r from-[#A80000] to-brand-blue hover:opacity-90 text-white font-bold text-xs py-2.5 rounded-lg transition shadow-md flex items-center justify-center gap-2">
                                <i class="fa-solid fa-paper-plane text-[10px]"></i> Gửi thông tin
                            </button>
                        </div>
                    </div>
                </div>`;

                if (messagesArea) {{
                    messagesArea.insertAdjacentHTML('beforeend', formHtml);
                    messagesArea.scrollTop = messagesArea.scrollHeight;
                }}

                // Focus vào input tên
                setTimeout(() => {{
                    const nameInput = document.getElementById('cf-name');
                    if (nameInput) nameInput.focus();
                }}, 100);
            }};

            // Submit contact form to Google Apps Script
            window.submitContactForm = async function() {{
                const name = (document.getElementById('cf-name')?.value || '').trim();
                const phone = (document.getElementById('cf-phone')?.value || '').trim();
                const message = (document.getElementById('cf-message')?.value || '').trim();
                const messagesArea = document.getElementById('chatbot-messages');

                // Validate
                if (!name) {{
                    document.getElementById('cf-name').focus();
                    document.getElementById('cf-name').style.borderColor = '#A80000';
                    return;
                }}
                if (!phone || phone.replace(/\\D/g, '').length < 9) {{
                    document.getElementById('cf-phone').focus();
                    document.getElementById('cf-phone').style.borderColor = '#A80000';
                    return;
                }}

                // Disable button, show loading
                const btn = document.getElementById('cf-submit-btn');
                if (btn) {{
                    btn.disabled = true;
                    btn.innerHTML = '<i class="fa-solid fa-circle-notch fa-spin text-[10px]"></i> Đang gửi...';
                }}

                try {{
                    await fetch(APPS_SCRIPT_URL, {{
                        method: 'POST',
                        mode: 'no-cors',
                        headers: {{ 'Content-Type': 'application/json' }},
                        body: JSON.stringify({{
                            name: name,
                            phone: phone,
                            message: message,
                            source: 'Chatbot – web-du-an-ca-nhan.vercel.app'
                        }})
                    }});

                    // Remove form bubble
                    const formBubble = document.getElementById('contact-form-bubble');
                    if (formBubble) formBubble.remove();

                    // Show success message
                    const successHtml = `
                    <div class="flex items-start gap-2.5 animate-fade-in">
                        <div class="w-8 h-8 rounded-full overflow-hidden bg-gray-100 flex-shrink-0 shadow-sm border border-gray-200 dark:border-white/10">
                            <img src="images/laodong_assistant_avatar.png" alt="Consultant" class="w-full h-full object-cover">
                        </div>
                        <div class="max-w-[85%]">
                            <div class="bg-white dark:bg-[#1E2530] border border-green-200 dark:border-green-900/50 p-3.5 rounded-2xl rounded-tl-none shadow-sm">
                                <div class="flex items-center gap-2 mb-1.5">
                                    <span class="w-5 h-5 rounded-full bg-green-500/15 text-green-600 dark:text-green-400 flex items-center justify-center text-xs"><i class="fa-solid fa-check"></i></span>
                                    <span class="text-xs font-black text-green-700 dark:text-green-400">Gửi thành công!</span>
                                </div>
                                <p class="text-xs text-slate-700 dark:text-gray-300 leading-relaxed font-medium">
                                    Cảm ơn <strong>${{name}}</strong>! Chuyên viên sẽ gọi đến <strong>${{phone}}</strong> trong vòng <strong>2 giờ làm việc</strong>.
                                </p>
                            </div>
                        </div>
                    </div>`;

                    if (messagesArea) {{
                        messagesArea.insertAdjacentHTML('beforeend', successHtml);
                        messagesArea.scrollTop = messagesArea.scrollHeight;
                    }}

                }} catch (err) {{
                    if (btn) {{
                        btn.disabled = false;
                        btn.innerHTML = '<i class="fa-solid fa-paper-plane text-[10px]"></i> Gửi lại';
                    }}
                }}
            }};
"""

# Insert JS before closing </script> of DOMContentLoaded block
insert_before = "        });\n    </script>"
insert_idx = c.rfind(insert_before)
if insert_idx != -1:
    c = c[:insert_idx] + js_to_add + c[insert_idx:]
    print("JS contact form functions added successfully")
else:
    print("ERROR: Could not find JS insert point")
    # Try alternate
    insert_before2 = "    </script>"
    insert_idx2 = c.rfind(insert_before2)
    if insert_idx2 != -1:
        c = c[:insert_idx2] + js_to_add + "\n" + c[insert_idx2:]
        print("JS added via alternate method")

# ================================================================
# 2. Update chat suggestions: Replace first suggestion with form button
#    And add a prominent "Để lại thông tin" button
# ================================================================
old_suggestions = '''            <div id="chatbot-suggestions" class="p-3 bg-white/95 dark:bg-[#161B26]/95 border-t border-gray-150 dark:border-slate-800 flex flex-wrap gap-2 justify-start">
                <button class="chat-suggest-btn text-xs text-slate-700 dark:text-gray-300 font-bold bg-slate-50 dark:bg-[#1E2530] hover:bg-brand-blue hover:text-white dark:hover:bg-brand-blue dark:hover:text-white border border-gray-200 dark:border-slate-800 hover:border-brand-blue dark:hover:border-brand-blue px-3 py-1.5 rounded-full transition-all duration-300 shadow-sm hover:shadow">Báo giá bài viết PR</button>
                <button class="chat-suggest-btn text-xs text-slate-700 dark:text-gray-300 font-bold bg-slate-50 dark:bg-[#1E2530] hover:bg-brand-blue hover:text-white dark:hover:bg-brand-blue dark:hover:text-white border border-gray-200 dark:border-slate-800 hover:border-brand-blue dark:hover:border-brand-blue px-3 py-1.5 rounded-full transition-all duration-300 shadow-sm hover:shadow">Báo giá Banner Quảng cáo</button>
                <button class="chat-suggest-btn text-xs text-slate-700 dark:text-gray-300 font-bold bg-slate-50 dark:bg-[#1E2530] hover:bg-brand-blue hover:text-white dark:hover:bg-brand-blue dark:hover:text-white border border-gray-200 dark:border-slate-800 hover:border-brand-blue dark:hover:border-brand-blue px-3 py-1.5 rounded-full transition-all duration-300 shadow-sm hover:shadow">Tổ chức Sự kiện / Hội thảo</button>
                <button class="chat-suggest-btn text-xs text-slate-700 dark:text-gray-300 font-bold bg-slate-50 dark:bg-[#1E2530] hover:bg-brand-blue hover:text-white dark:hover:bg-brand-blue dark:hover:text-white border border-gray-200 dark:border-slate-800 hover:border-brand-blue dark:hover:border-brand-blue px-3 py-1.5 rounded-full transition-all duration-300 shadow-sm hover:shadow">Tải tài liệu Media Kit 2026</button>
            </div>'''

new_suggestions = '''            <div id="chatbot-suggestions" class="p-3 bg-white/95 dark:bg-[#161B26]/95 border-t border-gray-150 dark:border-slate-800 space-y-2">
                <!-- Primary CTA: Để lại thông tin -->
                <button onclick="showContactForm()" id="btn-leave-contact"
                    class="w-full text-xs font-black bg-gradient-to-r from-[#A80000] to-brand-blue hover:opacity-90 text-white px-3 py-2.5 rounded-xl transition-all duration-300 shadow-sm hover:shadow flex items-center justify-center gap-2">
                    <i class="fa-solid fa-address-card text-[11px]"></i> Để lại thông tin – nhận tư vấn ngay
                </button>
                <!-- Secondary suggestions -->
                <div class="flex flex-wrap gap-1.5">
                    <button class="chat-suggest-btn text-xs text-slate-700 dark:text-gray-300 font-bold bg-slate-50 dark:bg-[#1E2530] hover:bg-brand-blue hover:text-white dark:hover:bg-brand-blue dark:hover:text-white border border-gray-200 dark:border-slate-800 hover:border-brand-blue dark:hover:border-brand-blue px-3 py-1.5 rounded-full transition-all duration-300 shadow-sm hover:shadow">Báo giá PR</button>
                    <button class="chat-suggest-btn text-xs text-slate-700 dark:text-gray-300 font-bold bg-slate-50 dark:bg-[#1E2530] hover:bg-brand-blue hover:text-white dark:hover:bg-brand-blue dark:hover:text-white border border-gray-200 dark:border-slate-800 hover:border-brand-blue dark:hover:border-brand-blue px-3 py-1.5 rounded-full transition-all duration-300 shadow-sm hover:shadow">Báo giá Banner</button>
                    <button class="chat-suggest-btn text-xs text-slate-700 dark:text-gray-300 font-bold bg-slate-50 dark:bg-[#1E2530] hover:bg-brand-blue hover:text-white dark:hover:bg-brand-blue dark:hover:text-white border border-gray-200 dark:border-slate-800 hover:border-brand-blue dark:hover:border-brand-blue px-3 py-1.5 rounded-full transition-all duration-300 shadow-sm hover:shadow">Sự kiện &amp; Hội thảo</button>
                    <button class="chat-suggest-btn text-xs text-slate-700 dark:text-gray-300 font-bold bg-slate-50 dark:bg-[#1E2530] hover:bg-brand-blue hover:text-white dark:hover:bg-brand-blue dark:hover:text-white border border-gray-200 dark:border-slate-800 hover:border-brand-blue dark:hover:border-brand-blue px-3 py-1.5 rounded-full transition-all duration-300 shadow-sm hover:shadow">Media Kit 2026</button>
                </div>
            </div>'''

if old_suggestions.replace('\r\n','\n') in c:
    c = c.replace(old_suggestions.replace('\r\n','\n'), new_suggestions)
    print("Chat suggestions updated successfully")
else:
    # Try without exact whitespace match
    search_key = 'id="chatbot-suggestions"'
    idx = c.find(search_key)
    if idx != -1:
        print(f"Found suggestions at index {idx} - manual check needed")
    else:
        print("WARNING: Could not find suggestions section")

# Convert back to CRLF
c_crlf = c.replace('\n', '\r\n')

with open(input_file, 'w', encoding='utf-8', newline='') as f:
    f.write(c_crlf)

print(f"File saved! Size: {len(c_crlf)} bytes")
