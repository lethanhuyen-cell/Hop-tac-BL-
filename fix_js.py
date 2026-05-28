import os

os.environ['PYTHONIOENCODING'] = 'utf-8'
input_file = r"C:\Users\Admin\Documents\Work_Folders\4_Hoat_Dong_Ca_Nhan\WEB-DU AN CA NHAN\index.html"

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    "mediaKitForm.addEventListener('submit', (e) => {",
    "if (mediaKitForm) mediaKitForm.addEventListener('submit', (e) => {"
)

content = content.replace(
    "contactForm.addEventListener('submit', (e) => {",
    "if (contactForm) contactForm.addEventListener('submit', (e) => {"
)

with open(input_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Fixed JS errors")
