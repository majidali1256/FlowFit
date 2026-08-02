import os

file = 'index.html'

old_cats = """        <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
          <a href="collections.html" class="glass-panel p-6 rounded-2xl text-center hover-lift group border border-slate-200/80 flex flex-col items-center">
            <span class="material-symbols-outlined text-4xl text-slate-900 mb-3 group-hover:scale-110 transition-transform">dry_cleaning</span>
            <h3 class="font-headline-md text-lg font-bold text-slate-900">Shirts &amp; Tops</h3>
            <p class="text-xs text-slate-500 mt-1">Tees, Hoodies, Oxfords</p>
          </a>
          <a href="collections.html" class="glass-panel p-6 rounded-2xl text-center hover-lift group border border-slate-200/80 flex flex-col items-center">
            <span class="material-symbols-outlined text-4xl text-slate-900 mb-3 group-hover:scale-110 transition-transform">strikethrough_s</span>
            <h3 class="font-headline-md text-lg font-bold text-slate-900">Pants &amp; Trousers</h3>
            <p class="text-xs text-slate-500 mt-1">Cargos, Chinos, Denim</p>
          </a>
          <a href="collections.html" class="glass-panel p-6 rounded-2xl text-center hover-lift group border border-slate-200/80 flex flex-col items-center">
            <span class="material-symbols-outlined text-4xl text-slate-900 mb-3 group-hover:scale-110 transition-transform">steps</span>
            <h3 class="font-headline-md text-lg font-bold text-slate-900">Jackets &amp; Coats</h3>
            <p class="text-xs text-slate-500 mt-1">Puffers, Bombers, Denim</p>
          </a>
          <a href="collections.html" class="glass-panel p-6 rounded-2xl text-center hover-lift group border border-slate-200/80 flex flex-col items-center">
            <span class="material-symbols-outlined text-4xl text-slate-900 mb-3 group-hover:scale-110 transition-transform">style</span>
            <h3 class="font-headline-md text-lg font-bold text-slate-900">Caps &amp; Gear</h3>
            <p class="text-xs text-slate-500 mt-1">Strapback Caps, Beanies</p>
          </a>
        </div>"""

new_cats = """        <div class="grid grid-cols-2 lg:grid-cols-5 gap-6">
          <a href="collections.html" class="glass-panel p-6 rounded-2xl text-center hover-lift group border border-slate-200/80 flex flex-col items-center">
            <span class="material-symbols-outlined text-4xl text-slate-900 mb-3 group-hover:scale-110 transition-transform">dry_cleaning</span>
            <h3 class="font-headline-md text-lg font-bold text-slate-900">Shirts</h3>
            <p class="text-xs text-slate-500 mt-1">Tees &amp; Tops</p>
          </a>
          <a href="collections.html" class="glass-panel p-6 rounded-2xl text-center hover-lift group border border-slate-200/80 flex flex-col items-center">
            <span class="material-symbols-outlined text-4xl text-slate-900 mb-3 group-hover:scale-110 transition-transform">strikethrough_s</span>
            <h3 class="font-headline-md text-lg font-bold text-slate-900">Pants</h3>
            <p class="text-xs text-slate-500 mt-1">Denim &amp; Cargos</p>
          </a>
          <a href="collections.html" class="glass-panel p-6 rounded-2xl text-center hover-lift group border border-slate-200/80 flex flex-col items-center">
            <span class="material-symbols-outlined text-4xl text-slate-900 mb-3 group-hover:scale-110 transition-transform">straighten</span>
            <h3 class="font-headline-md text-lg font-bold text-slate-900">Trousers</h3>
            <p class="text-xs text-slate-500 mt-1">Pleated &amp; Chinos</p>
          </a>
          <a href="collections.html" class="glass-panel p-6 rounded-2xl text-center hover-lift group border border-slate-200/80 flex flex-col items-center">
            <span class="material-symbols-outlined text-4xl text-slate-900 mb-3 group-hover:scale-110 transition-transform">steps</span>
            <h3 class="font-headline-md text-lg font-bold text-slate-900">Jackets</h3>
            <p class="text-xs text-slate-500 mt-1">Coats &amp; Outerwear</p>
          </a>
          <a href="collections.html" class="glass-panel p-6 rounded-2xl text-center hover-lift group border border-slate-200/80 flex flex-col items-center">
            <span class="material-symbols-outlined text-4xl text-slate-900 mb-3 group-hover:scale-110 transition-transform">style</span>
            <h3 class="font-headline-md text-lg font-bold text-slate-900">Caps</h3>
            <p class="text-xs text-slate-500 mt-1">Hats &amp; Accessories</p>
          </a>
        </div>"""

with open(file, 'r') as f:
    content = f.read()
content = content.replace(old_cats, new_cats)
with open(file, 'w') as f:
    f.write(content)

