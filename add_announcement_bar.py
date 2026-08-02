import os

files = ['index.html', 'collections.html', 'product.html', 'new-arrivals.html']

nav_start_old = '<nav class="fixed top-0 w-full z-50 bg-white/85 backdrop-blur-xl border-b border-slate-200/80 shadow-sm transition-all duration-300">'

nav_start_new = """  <header class="fixed top-0 w-full z-50">
    <div class="bg-slate-900 text-white text-[10px] sm:text-xs font-semibold uppercase tracking-widest text-center py-2 px-4 shadow-md flex justify-center gap-2 items-center">
      <span class="material-symbols-outlined text-sm hidden sm:inline">local_shipping</span>
      Free Worldwide Shipping on orders over $75 &bull; <a href="collections.html" class="underline hover:text-slate-300 transition-colors">Shop Now</a>
    </div>
    <nav class="w-full bg-white/95 backdrop-blur-xl border-b border-slate-200/80 shadow-sm transition-all duration-300">"""

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    # Replace opening tag
    content = content.replace(nav_start_old, nav_start_new, 1)
    
    # We need to replace the FIRST </nav> with </nav>\n  </header>
    nav_end_idx = content.find('</nav>')
    if nav_end_idx != -1:
        content = content[:nav_end_idx] + '</nav>\n  </header>' + content[nav_end_idx+6:]
    
    with open(f, 'w') as file:
        file.write(content)

