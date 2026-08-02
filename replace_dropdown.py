import os

files = ['index.html', 'collections.html', 'product.html', 'lookbook.html']

old_dropdown = """            <select id="prod-category" required class="w-full px-4 py-3 rounded-xl bg-slate-50 border border-slate-200 text-sm outline-none focus:border-slate-900">
              <option value="shirts">Shirts &amp; Tops</option>
              <option value="pants">Pants &amp; Trousers</option>
              <option value="jackets">Jackets &amp; Outerwear</option>
              <option value="caps">Caps &amp; Accessories</option>
              <option value="kids">Boys &amp; Girls (Kids)</option>
            </select>"""

new_dropdown = """            <select id="prod-category" required class="w-full px-4 py-3 rounded-xl bg-slate-50 border border-slate-200 text-sm outline-none focus:border-slate-900">
              <option value="shirts">Shirts</option>
              <option value="pants">Pants</option>
              <option value="trousers">Trousers</option>
              <option value="jackets">Jackets</option>
              <option value="caps">Caps</option>
              <option value="kids">Boys &amp; Girls</option>
            </select>"""

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    content = content.replace(old_dropdown, new_dropdown)
    with open(f, 'w') as file:
        file.write(content)

