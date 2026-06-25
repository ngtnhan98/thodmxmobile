import re

file_path = "/Users/nguyentrongnhan/Downloads/tho/thodienmayxanh_mobile/thodmxmobile/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add CSS
css = """
    /* Accordion styles */
    .accordion-toggle-btn {
      background: #f1f5f9;
      border: none;
      border-radius: 8px;
      width: 32px;
      height: 32px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      color: #64748b;
      transition: transform 0.3s ease;
    }
    .accordion-toggle-btn.open {
      transform: rotate(180deg);
    }
    .item-accordion-content {
      grid-column: 1 / -1;
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.4s ease, padding 0.4s ease, margin 0.4s ease, opacity 0.4s ease;
      opacity: 0;
    }
    .item-accordion-content.open {
      max-height: 200px;
      padding-top: 12px;
      margin-top: 4px;
      border-top: 1px dashed #cbd5e1;
      opacity: 1;
    }
    .periodic-title {
      font-size: 13px;
      font-weight: 600;
      color: #334155;
      margin-bottom: 8px;
    }
    .periodic-scroll-container {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 4px;
      scrollbar-width: none;
    }
    .periodic-scroll-container::-webkit-scrollbar {
      display: none;
    }
    .periodic-chip {
      display: flex;
      flex-direction: column;
      align-items: center;
      background: #f1f5f9;
      border-radius: 6px;
      min-width: 76px;
      flex-shrink: 0;
      border: 1px solid #e2e8f0;
      overflow: hidden;
    }
    .periodic-chip.active {
      border-color: #2563eb;
    }
    .periodic-chip.active .chip-header {
      background: #2563eb;
      color: white;
    }
    .chip-header {
      width: 100%;
      text-align: center;
      padding: 4px 0;
      font-size: 11px;
      font-weight: 600;
      color: #475569;
      background: #e2e8f0;
    }
    .chip-date {
      padding: 6px 0;
      font-size: 11px;
      color: #64748b;
      font-weight: 500;
    }
    .periodic-legend {
      font-size: 11px;
      color: #64748b;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 4px;
      margin-top: 8px;
    }
    .legend-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #2563eb;
    }
"""

if "/* Accordion styles */" not in content:
    content = content.replace("  </style>", css + "\n  </style>")

# 2. Update Item 3 HTML
# Find the button group of item 3
item_3_marker = "<!-- Item 3: Water purifier -->"
btn_group_start = content.find('<div class="btn-group"', content.find(item_3_marker))
btn_group_end = content.find('</div>', content.find('</button>', btn_group_start)) + 6

# Extract the existing button
existing_btn_html = content[btn_group_start:btn_group_end]

if "accordion-toggle-btn" not in existing_btn_html:
    new_btn_html = existing_btn_html.replace('</div>', '''
  <button class="accordion-toggle-btn" onclick="event.stopPropagation(); toggleAccordion(this)">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
  </button>
</div>''')
    
    accordion_content = '''
              <!-- Accordion Content -->
              <div class="item-accordion-content">
                <p class="periodic-title">Kiểm tra định kỳ</p>
                <div class="periodic-scroll-container">
                  <div class="periodic-chip active">
                    <div class="chip-header">Lõi 1</div>
                    <div class="chip-date">11/03/2026</div>
                  </div>
                  <div class="periodic-chip active">
                    <div class="chip-header">Lõi 2</div>
                    <div class="chip-date">11/03/2026</div>
                  </div>
                  <div class="periodic-chip">
                    <div class="chip-header">Lõi 3</div>
                    <div class="chip-date">15/04/2026</div>
                  </div>
                  <div class="periodic-chip">
                    <div class="chip-header">Lõi 4</div>
                    <div class="chip-date">15/04/2027</div>
                  </div>
                  <div class="periodic-chip">
                    <div class="chip-header">Lõi 5</div>
                    <div class="chip-date">15/04/2027</div>
                  </div>
                </div>
                <div class="periodic-legend">
                  <span class="legend-dot"></span> Lịch định kỳ sắp tới
                </div>
              </div>
'''
    
    # We replace the button group and add the accordion content right after it
    replacement = new_btn_html + accordion_content
    content = content[:btn_group_start] + replacement + content[btn_group_end:]

# 3. Add JS
js_func = """
    function toggleAccordion(btn) {
      btn.classList.toggle('open');
      const item = btn.closest('.reminder-item');
      const content = item.querySelector('.item-accordion-content');
      if (content) {
        content.classList.toggle('open');
      }
    }
"""
if "toggleAccordion" not in content:
    content = content.replace("  </script>", js_func + "\n  </script>")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done")
