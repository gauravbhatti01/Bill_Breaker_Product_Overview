import re

with open('d:/Product/bill-breaker.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all base64 img tags with White_logo.png
new_content = re.sub(r'<img[^>]*src="data:image/png;base64[^"]*"[^>]*>', '<img src="White_logo.png" />', content)

with open('d:/Product/bill-breaker.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Done')
