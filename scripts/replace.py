with open("bill-breaker.html", "r", encoding="utf-8") as f:
    content = f.read()

import re
# mark
start = content.find('<div class="mark">')
if start != -1:
    end = content.find('</div>', start)
    if end != -1:
        content = content[:start] + '<div class="mark"><img src="logo.png" alt="Bill Breaker Logo"></div>' + content[end+6:]

# brand
start = content.find('<div class="brand">')
if start != -1:
    end = content.find('</div>', start)
    if end != -1:
        content = content[:start] + '<div class="brand"><img src="logo.png" alt="Bill Breaker Logo"></div>' + content[end+6:]

with open("bill-breaker.html", "w", encoding="utf-8") as f:
    f.write(content)
