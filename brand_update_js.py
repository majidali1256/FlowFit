import os

with open('assets/js/main.js', 'r') as file:
    content = file.read()

# Replace button classes
content = content.replace('bg-slate-900 text-white', 'bg-[#DDB24A] text-[#1A1A1A] hover:bg-[#c49a37]')
# Replace text mentions
content = content.replace('Flow Wear', 'FLOWEAR')

with open('assets/js/main.js', 'w') as file:
    file.write(content)
