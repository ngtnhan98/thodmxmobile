import re

file_path = "/Users/nguyentrongnhan/Downloads/tho/thodienmayxanh_mobile/thodmxmobile/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

item_2_marker = "<!-- Item 2: Air Conditioner -->"
btn_group_start = content.find('<div class="btn-group"', content.find(item_2_marker))
btn_group_end = content.find('</div>', content.find('</button>', btn_group_start)) + 6

existing_btn_html = content[btn_group_start:btn_group_end]

periodic_content = '''
              <div class="item-periodic-content">
                <p class="periodic-title">Vệ sinh định kỳ</p>
                <div class="periodic-scroll-container">
                  <div class="periodic-chip active">
                    <div class="chip-header">Lần 1</div>
                    <div class="chip-date">15/07/2026</div>
                  </div>
                  <div class="periodic-chip">
                    <div class="chip-header">Lần 2</div>
                    <div class="chip-date">15/01/2027</div>
                  </div>
                  <div class="periodic-chip">
                    <div class="chip-header">Lần 3</div>
                    <div class="chip-date">15/07/2027</div>
                  </div>
                  <div class="periodic-chip">
                    <div class="chip-header">Lần 4</div>
                    <div class="chip-date">15/01/2028</div>
                  </div>
                </div>
                <div class="periodic-legend">
                  <span class="legend-dot"></span> Lịch định kỳ sắp tới
                </div>
              </div>
'''

if "Vệ sinh định kỳ" not in content[btn_group_start:btn_group_end+1000]:
    replacement = existing_btn_html + periodic_content
    content = content[:btn_group_start] + replacement + content[btn_group_end:]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done")
