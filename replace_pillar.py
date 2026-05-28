import sys
import os

os.environ['PYTHONIOENCODING'] = 'utf-8'

input_file = r"C:\Users\Admin\Documents\Work_Folders\4_Hoat_Dong_Ca_Nhan\WEB-DU AN CA NHAN\index.html"
new_pillar_file = r"C:\Users\Admin\Documents\Work_Folders\4_Hoat_Dong_Ca_Nhan\WEB-DU AN CA NHAN\pillar_new_html.txt"

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

with open(new_pillar_file, 'r', encoding='utf-8') as f:
    new_pillar = f.read()

# The file uses CRLF (\r\n). Let's normalize to find markers
content_normalized = content.replace('\r\n', '\n')

start_marker = "            <!-- NEW: Pillar Console Dashboard (Responsive Premium Interactive Console) -->"
end_marker = "            </div>\n        </div>\n</section>"

start_idx = content_normalized.find(start_marker)
print(f"Start found at index: {start_idx}")

if start_idx == -1:
    print("Start marker not found!")
    sys.exit(1)

# Find end_marker in the area after start
search_area = content_normalized[start_idx:]
end_idx_local = search_area.find(end_marker)
print(f"End found at local offset: {end_idx_local}")

if end_idx_local == -1:
    # Try alternate end - section closes with </div>\n        </div>\n</section>
    # Check what's actually there around line 651
    # The section end is: 651:             </div> then 652:         </div> then 653: </section>
    end_marker2 = "            </div>\n        </div>\n</section>"
    end_idx_local = search_area.find(end_marker2)
    print(f"End2 found at: {end_idx_local}")
    
    if end_idx_local == -1:
        # Find it differently - go to close of the pillar grid
        end_marker3 = "        </div><!-- end pillar-showcase -->"
        # Actually let's search for section closing
        end_marker3 = "</section>"
        idx3 = search_area.find(end_marker3)
        print(f"Section end found at: {idx3}")
        
        # Grab context
        with open("debug_out.txt", "w", encoding="utf-8") as df:
            df.write(search_area[:3000])
        print("Wrote first 3000 chars of search area to debug_out.txt")
        sys.exit(1)

end_idx_global = start_idx + end_idx_local

new_content = (
    content_normalized[:start_idx] +
    new_pillar +
    "\n        </div>\n</section>" +
    content_normalized[end_idx_global + len(end_marker):]
)

# Convert back to CRLF for Windows
new_content_crlf = new_content.replace('\n', '\r\n')

with open(input_file, 'w', encoding='utf-8', newline='') as f:
    f.write(new_content_crlf)

print("SUCCESS: Pillar section replaced!")
print(f"Old length: {len(content)}, New length: {len(new_content_crlf)}")
