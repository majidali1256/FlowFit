import os

files = ['index.html', 'collections.html', 'product.html', 'new-arrivals.html']

old_nav = """      <nav class="flex flex-col gap-4">
        <a href="index.html" class="text-lg font-bold text-slate-900 hover:text-slate-600 transition-colors mb-2">Home</a>
        
        <div class="text-xs font-bold text-slate-400 uppercase tracking-widest mt-2 mb-1">Categories</div>
        <a href="collections.html" class="text-lg font-medium text-slate-700 hover:text-slate-900 transition-colors">All Collections</a>
        <a href="collections.html?category=Shirts" class="text-lg font-medium text-slate-700 hover:text-slate-900 transition-colors">Shirts</a>
        <a href="collections.html?category=Pants" class="text-lg font-medium text-slate-700 hover:text-slate-900 transition-colors">Pants</a>
        <a href="collections.html?category=Trousers" class="text-lg font-medium text-slate-700 hover:text-slate-900 transition-colors">Trousers</a>
        <a href="collections.html?category=Jackets" class="text-lg font-medium text-slate-700 hover:text-slate-900 transition-colors">Jackets</a>
        <a href="collections.html?category=Caps" class="text-lg font-medium text-slate-700 hover:text-slate-900 transition-colors">Caps</a>
        <a href="collections.html?category=Boys+%26+Girls" class="text-lg font-medium text-slate-700 hover:text-slate-900 transition-colors">Boys & Girls</a>
        
        <div class="text-xs font-bold text-slate-400 uppercase tracking-widest mt-4 mb-1">Discover</div>
        <a href="new-arrivals.html" class="text-lg font-medium text-slate-700 hover:text-slate-900 transition-colors">New Arrivals</a>
        
        <button class="add-product-toggle-btn text-left text-sm font-semibold text-slate-500 hover:text-slate-900 transition-colors flex items-center gap-2 cursor-pointer mt-6">
          <span class="material-symbols-outlined text-sm">add_circle</span> + Add New Product
        </button>
      </nav>"""

new_nav = """      <nav class="flex flex-col gap-4">
        <a href="index.html" class="text-lg font-bold text-slate-900 hover:text-slate-600 transition-colors mb-2">Home</a>
        
        <div class="text-xs font-bold text-slate-400 uppercase tracking-widest mt-2 mb-1">Discover</div>
        <a href="new-arrivals.html" class="text-lg font-medium text-slate-700 hover:text-slate-900 transition-colors">New Arrivals</a>
        
        <div class="text-xs font-bold text-slate-400 uppercase tracking-widest mt-4 mb-1">Categories</div>
        <a href="collections.html" class="text-lg font-medium text-slate-700 hover:text-slate-900 transition-colors">All Collections</a>
        <a href="collections.html?category=Shirts" class="text-lg font-medium text-slate-700 hover:text-slate-900 transition-colors">Shirts</a>
        <a href="collections.html?category=Pants" class="text-lg font-medium text-slate-700 hover:text-slate-900 transition-colors">Pants</a>
        <a href="collections.html?category=Trousers" class="text-lg font-medium text-slate-700 hover:text-slate-900 transition-colors">Trousers</a>
        <a href="collections.html?category=Jackets" class="text-lg font-medium text-slate-700 hover:text-slate-900 transition-colors">Jackets</a>
        <a href="collections.html?category=Caps" class="text-lg font-medium text-slate-700 hover:text-slate-900 transition-colors">Caps</a>
        <a href="collections.html?category=Boys+%26+Girls" class="text-lg font-medium text-slate-700 hover:text-slate-900 transition-colors">Boys & Girls</a>
        
        <button class="add-product-toggle-btn text-left text-sm font-semibold text-slate-500 hover:text-slate-900 transition-colors flex items-center gap-2 cursor-pointer mt-6">
          <span class="material-symbols-outlined text-sm">add_circle</span> + Add New Product
        </button>
      </nav>"""

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    # 1. Update side nav
    content = content.replace(old_nav, new_nav)
    
    # 2. Ensure header nav has New Arrivals before Collections
    old_header = """      <div class="hidden md:flex items-center gap-8">
        <a href="index.html" class="text-sm font-semibold text-slate-900 hover:text-slate-600 transition-colors">Home</a>
        <a href="collections.html" class="text-sm font-semibold text-slate-900 hover:text-slate-600 transition-colors">Collections</a>
        <a href="new-arrivals.html" class="text-sm font-semibold text-slate-900 hover:text-slate-600 transition-colors">New Arrivals</a>
      </div>"""
      
    new_header = """      <div class="hidden md:flex items-center gap-8">
        <a href="index.html" class="text-sm font-semibold text-slate-900 hover:text-slate-600 transition-colors">Home</a>
        <a href="new-arrivals.html" class="text-sm font-semibold text-slate-900 hover:text-slate-600 transition-colors">New Arrivals</a>
        <a href="collections.html" class="text-sm font-semibold text-slate-900 hover:text-slate-600 transition-colors">Collections</a>
      </div>"""
      
    content = content.replace(old_header, new_header)
    
    with open(f, 'w') as file:
        file.write(content)

