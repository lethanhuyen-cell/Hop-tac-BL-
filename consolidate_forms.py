import re
import os

os.environ['PYTHONIOENCODING'] = 'utf-8'
input_file = r"C:\Users\Admin\Documents\Work_Folders\4_Hoat_Dong_Ca_Nhan\WEB-DU AN CA NHAN\index.html"

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add `openChatWithContext` JS function
js_to_add = """
            // --- OPEN CHAT WITH CONTEXT ---
            window.openChatWithContext = function(contextMsg) {
                const chatbotWindow = document.getElementById('chatbot-window');
                const chatbotTrigger = document.getElementById('chatbot-trigger');
                
                // Open chat if closed
                if (chatbotWindow && chatbotWindow.classList.contains('hidden')) {
                    if (chatbotTrigger) {
                        chatbotTrigger.classList.add('scale-0');
                        setTimeout(() => {
                            chatbotTrigger.classList.add('hidden');
                            chatbotWindow.classList.remove('hidden');
                            setTimeout(() => {
                                chatbotWindow.classList.remove('opacity-0', 'translate-y-4');
                                // Wait for chat to open, then trigger context
                                setTimeout(() => {
                                    appendMessage('user', contextMsg);
                                    handleBotResponse(contextMsg);
                                }, 300);
                            }, 50);
                        }, 150);
                    }
                } else {
                    // Chat already open
                    appendMessage('user', contextMsg);
                    handleBotResponse(contextMsg);
                }
            };
"""

if "window.openChatWithContext = function" not in content:
    # Insert before closing </script> in DOMContentLoaded
    insert_before = "        });\n    </script>"
    idx = content.rfind(insert_before)
    if idx != -1:
        content = content[:idx] + js_to_add + content[idx:]

# 2. Update Header & Hero buttons
# Change href="#lien-he" to onclick="openChatWithContext('Tôi muốn nhận tư vấn hợp tác'); return false;" href="#"
content = content.replace(
    '<a href="#lien-he" class="hidden md:block text-sm font-bold text-slate-600 dark:text-gray-300 hover:text-brand-blue dark:hover:text-brand-blue">Nhận tư vấn</a>',
    '<a href="#" onclick="openChatWithContext(\'Tôi muốn nhận tư vấn hợp tác\'); return false;" class="hidden md:block text-sm font-bold text-slate-600 dark:text-gray-300 hover:text-brand-blue dark:hover:text-brand-blue">Nhận tư vấn</a>'
)

content = content.replace(
    '<a href="#media-kit" class="hidden sm:inline-block bg-[#A80000] hover:bg-[#8B0000] text-white px-5 py-2.5 rounded-md text-sm font-bold transition shadow-md hover:shadow-lg">Tải Media Kit</a>',
    '<a href="#" onclick="openChatWithContext(\'Tôi muốn tải tài liệu Media Kit\'); return false;" class="hidden sm:inline-block bg-[#A80000] hover:bg-[#8B0000] text-white px-5 py-2.5 rounded-md text-sm font-bold transition shadow-md hover:shadow-lg">Tải Media Kit</a>'
)

# Mobile menu
content = content.replace(
    '<a href="#lien-he" class="block text-center text-sm font-semibold text-slate-600 dark:text-gray-300 hover:text-brand-blue py-2">Nhận tư vấn</a>',
    '<a href="#" onclick="openChatWithContext(\'Tôi muốn nhận tư vấn hợp tác\'); return false;" class="block text-center text-sm font-semibold text-slate-600 dark:text-gray-300 hover:text-brand-blue py-2">Nhận tư vấn</a>'
)
content = content.replace(
    '<a href="#lien-he" class="block text-center border border-brand-blue text-brand-blue hover:bg-brand-blue hover:text-white py-3 rounded-md text-sm font-semibold transition shadow-sm">Đặt báo in</a>',
    '<a href="#" onclick="openChatWithContext(\'Tôi muốn đặt báo in\'); return false;" class="block text-center border border-brand-blue text-brand-blue hover:bg-brand-blue hover:text-white py-3 rounded-md text-sm font-semibold transition shadow-sm">Đặt báo in</a>'
)
content = content.replace(
    '<a href="#media-kit" class="block text-center bg-[#A80000] hover:bg-[#8B0000] text-white py-3 rounded-md text-sm font-semibold transition shadow-md">Tải Media Kit</a>',
    '<a href="#" onclick="openChatWithContext(\'Tôi muốn tải tài liệu Media Kit\'); return false;" class="block text-center bg-[#A80000] hover:bg-[#8B0000] text-white py-3 rounded-md text-sm font-semibold transition shadow-md">Tải Media Kit</a>'
)

# 3. Clean up Bottom Forms

# Find the media kit form and replace it
mk_form_start = '<form id="media-kit-form" class="space-y-4">'
mk_form_end = '</form>'
if mk_form_start in content:
    start_idx = content.find(mk_form_start)
    end_idx = content.find(mk_form_end, start_idx) + len(mk_form_end)
    
    new_mk_cta = """
                            <div class="text-center py-6">
                                <h4 class="text-sm font-bold text-slate-800 dark:text-white mb-4">Tải nhanh toàn bộ tài liệu qua Trợ lý ảo</h4>
                                <button onclick="openChatWithContext('Tôi muốn tải tài liệu Media Kit')" class="bg-[#A80000] hover:bg-[#8B0000] text-white font-bold py-3 px-8 rounded-lg transition duration-300 shadow-md text-sm inline-flex items-center gap-2">
                                    <i class="fa-solid fa-robot"></i> Trợ lý ảo hỗ trợ 24/7
                                </button>
                            </div>
    """
    content = content[:start_idx] + new_mk_cta + content[end_idx:]

# Find the contact form and replace it
contact_form_start = '<form id="contact-form" class="space-y-4">'
contact_form_end = '</form>'
if contact_form_start in content:
    start_idx = content.find(contact_form_start)
    end_idx = content.find(contact_form_end, start_idx) + len(contact_form_end)
    
    new_contact_cta = """
                    <div class="bg-slate-50/50 dark:bg-brand-dark/30 border border-gray-250 dark:border-white/10 rounded-xl p-6 text-center">
                        <p class="text-sm text-slate-600 dark:text-gray-300 mb-5 leading-relaxed">
                            Để tối ưu hóa thời gian và tư vấn chính xác nhất, Báo Lao Động hỗ trợ tiếp nhận yêu cầu tự động qua Hệ thống Trợ lý ảo thông minh.
                        </p>
                        <button onclick="openChatWithContext('Tôi muốn nhận tư vấn hợp tác')" class="w-full sm:w-auto bg-[#A80000] hover:bg-[#8B0000] dark:bg-brand-blue dark:hover:bg-blue-600 text-white font-black py-3 px-8 rounded-lg transition duration-300 shadow-md hover:shadow-lg hover:-translate-y-0.5 active:translate-y-0 text-xs uppercase tracking-wider inline-flex items-center justify-center gap-2">
                            <i class="fa-solid fa-comments text-[12px]"></i> Trò chuyện & Gửi yêu cầu ngay
                        </button>
                    </div>
    """
    content = content[:start_idx] + new_contact_cta + content[end_idx:]

with open(input_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Updated index.html")
