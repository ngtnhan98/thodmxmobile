import re

file_path = "/Users/nguyentrongnhan/Downloads/tho/thodienmayxanh_mobile/thodmxmobile/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove Accordion toggle button
content = re.sub(
    r'<button class="accordion-toggle-btn"[^>]*>[\s\S]*?</button>',
    '',
    content
)

# 2. Change class name in HTML
content = content.replace('item-accordion-content', 'item-periodic-content')

# 3. Update CSS
# Replace old accordion CSS with new permanent periodic content CSS
old_css_pattern = r'/\* Accordion styles \*/[\s\S]*?(?=\n  </style>)'
new_css = """/* Periodic Check styles */
    .item-periodic-content {
      grid-column: 1 / -1;
      padding-top: 12px;
      margin-top: 4px;
      border-top: 1px dashed #cbd5e1;
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
    }"""
content = re.sub(old_css_pattern, new_css, content)

# 4. Remove JS function
js_pattern = r'    function toggleAccordion\(btn\) \{[\s\S]*?\}\n'
content = re.sub(js_pattern, '', content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done")
