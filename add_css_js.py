import sys

input_file = r"C:\Users\Admin\Documents\Work_Folders\4_Hoat_Dong_Ca_Nhan\WEB-DU AN CA NHAN\index.html"

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Normalize to LF
c = content.replace('\r\n', '\n')

# 1. Add CSS before </style>
css_to_add = """
        /* ===== PILLAR SHOWCASE STYLES ===== */
        .pillar-card {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .pillar-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 20px 40px -10px rgba(0,0,0,0.12);
            z-index: 2;
        }
        .dark .pillar-card:hover {
            box-shadow: 0 20px 40px -10px rgba(0,0,0,0.4);
        }
"""

style_end = "    </style>"
style_idx = c.find(style_end)
if style_idx != -1:
    c = c[:style_idx] + css_to_add + c[style_idx:]
    print("CSS added successfully")
else:
    print("WARNING: Could not find </style> tag")

# 2. Add JS function switchPillarConsoleTab AND expandPillar
# Find the existing switchPillarTab function to add after it
js_to_add = """
            // --- PILLAR CONSOLE TAB SWITCHER (Console Dashboard version) ---
            window.switchPillarConsoleTab = function(tabIndex) {
                // Update nav buttons
                for (let i = 1; i <= 3; i++) {
                    const btn = document.getElementById('pillar-nav-btn-' + i);
                    const panel = document.getElementById('pillar-console-panel-' + i);
                    if (!btn || !panel) continue;
                    if (i === tabIndex) {
                        // Active state
                        btn.classList.add('bg-[#A80000]', 'dark:bg-brand-blue', 'text-white', 'border-transparent', 'shadow-lg');
                        btn.classList.remove('bg-white', 'dark:bg-[#161B26]', 'text-slate-755', 'dark:text-gray-300', 'border-gray-200', 'dark:border-white/10');
                        panel.classList.remove('hidden', 'opacity-0', 'translate-x-4');
                        panel.classList.add('opacity-100', 'translate-x-0');
                    } else {
                        // Inactive state
                        btn.classList.remove('bg-[#A80000]', 'dark:bg-brand-blue', 'text-white', 'border-transparent', 'shadow-lg');
                        btn.classList.add('bg-white', 'dark:bg-[#161B26]', 'text-slate-755', 'dark:text-gray-300', 'border-gray-200', 'dark:border-white/10');
                        panel.classList.add('hidden', 'opacity-0', 'translate-x-4');
                        panel.classList.remove('opacity-100', 'translate-x-0');
                    }
                }
            };

            // --- PILLAR CARD EXPAND (New showcase version) ---
            window.expandPillar = function(index) {
                // Visual highlight on click - brief pulse effect
                const card = document.getElementById('pillar-card-' + index);
                if (card) {
                    card.style.transform = 'translateY(-6px)';
                    setTimeout(() => { card.style.transform = ''; }, 400);
                }
            };
"""

# Add after the switchPillarTab function closing brace
insert_after = "            startPillarAutoplay();"
insert_idx = c.find(insert_after)
if insert_idx != -1:
    end_of_line = c.find('\n', insert_idx)
    c = c[:end_of_line + 1] + js_to_add + c[end_of_line + 1:]
    print("JS functions added successfully")
else:
    print("WARNING: Could not find JS insert point, trying alternate")
    insert_after2 = "            startPillarAutoplay();"
    insert_idx2 = c.find("startPillarAutoplay();")
    if insert_idx2 != -1:
        end_of_line2 = c.find('\n', insert_idx2)
        c = c[:end_of_line2 + 1] + js_to_add + c[end_of_line2 + 1:]
        print("JS added via alternate method")

# Convert back to CRLF
c_crlf = c.replace('\n', '\r\n')

with open(input_file, 'w', encoding='utf-8', newline='') as f:
    f.write(c_crlf)

print("File saved successfully!")
print(f"New file size: {len(c_crlf)} bytes")
