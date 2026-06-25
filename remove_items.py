import re

file_path = "/Users/nguyentrongnhan/Downloads/tho/thodienmayxanh_mobile/thodmxmobile/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

item_4_marker = "<!-- Item 4: Air Conditioner -->"
item_5_marker = "<!-- Item 5: Water purifier -->"

if item_4_marker in content:
    start_idx = content.find(item_4_marker)
    # find the end of item 5
    if item_5_marker in content:
        item_5_start = content.find(item_5_marker)
        # find the end of item 5's div
        # btn-group ends item 5
        btn_group_start = content.find('<div class="btn-group"', item_5_start)
        btn_group_end = content.find('</div>', content.find('</button>', btn_group_start)) + 6
        # there's a closing div for reminder-item
        item_5_end = content.find('</div>', btn_group_end) + 6
        
        # remove everything from start_idx to item_5_end
        content = content[:start_idx] + content[item_5_end:]
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Removed Item 4 and 5")
    else:
        print("Item 5 not found")
else:
    print("Item 4 not found")
