import os

file = 'collections.html'

old_filters = """      <div class="flex flex-wrap items-center gap-2">
        <button class="filter-chip-btn bg-slate-900 text-white px-4 py-2 rounded-full text-xs font-semibold uppercase tracking-wider transition-colors cursor-pointer" data-filter="all">All Clothing</button>
        <button class="filter-chip-btn bg-slate-100 text-slate-700 hover:bg-slate-200 px-4 py-2 rounded-full text-xs font-semibold uppercase tracking-wider transition-colors cursor-pointer" data-filter="shirts">Shirts &amp; Tops</button>
        <button class="filter-chip-btn bg-slate-100 text-slate-700 hover:bg-slate-200 px-4 py-2 rounded-full text-xs font-semibold uppercase tracking-wider transition-colors cursor-pointer" data-filter="pants">Pants &amp; Trousers</button>
        <button class="filter-chip-btn bg-slate-100 text-slate-700 hover:bg-slate-200 px-4 py-2 rounded-full text-xs font-semibold uppercase tracking-wider transition-colors cursor-pointer" data-filter="jackets">Jackets</button>
        <button class="filter-chip-btn bg-slate-100 text-slate-700 hover:bg-slate-200 px-4 py-2 rounded-full text-xs font-semibold uppercase tracking-wider transition-colors cursor-pointer" data-filter="caps">Caps</button>
        <button class="filter-chip-btn bg-slate-100 text-slate-700 hover:bg-slate-200 px-4 py-2 rounded-full text-xs font-semibold uppercase tracking-wider transition-colors cursor-pointer" data-filter="kids">Boys &amp; Girls</button>
        <button class="add-product-toggle-btn bg-slate-900 text-white px-4 py-2 rounded-full text-xs font-bold uppercase tracking-wider hover:bg-slate-800 transition-opacity flex items-center gap-1 cursor-pointer">
          <span class="material-symbols-outlined text-sm">add</span> + Add Item
        </button>
      </div>"""

new_filters = """      <div class="flex flex-wrap items-center gap-2">
        <button class="filter-chip-btn bg-slate-900 text-white px-4 py-2 rounded-full text-xs font-semibold uppercase tracking-wider transition-colors cursor-pointer" data-filter="all">All</button>
        <button class="filter-chip-btn bg-slate-100 text-slate-700 hover:bg-slate-200 px-4 py-2 rounded-full text-xs font-semibold uppercase tracking-wider transition-colors cursor-pointer" data-filter="shirts">Shirts</button>
        <button class="filter-chip-btn bg-slate-100 text-slate-700 hover:bg-slate-200 px-4 py-2 rounded-full text-xs font-semibold uppercase tracking-wider transition-colors cursor-pointer" data-filter="pants">Pants</button>
        <button class="filter-chip-btn bg-slate-100 text-slate-700 hover:bg-slate-200 px-4 py-2 rounded-full text-xs font-semibold uppercase tracking-wider transition-colors cursor-pointer" data-filter="trousers">Trousers</button>
        <button class="filter-chip-btn bg-slate-100 text-slate-700 hover:bg-slate-200 px-4 py-2 rounded-full text-xs font-semibold uppercase tracking-wider transition-colors cursor-pointer" data-filter="jackets">Jackets</button>
        <button class="filter-chip-btn bg-slate-100 text-slate-700 hover:bg-slate-200 px-4 py-2 rounded-full text-xs font-semibold uppercase tracking-wider transition-colors cursor-pointer" data-filter="caps">Caps</button>
        <button class="filter-chip-btn bg-slate-100 text-slate-700 hover:bg-slate-200 px-4 py-2 rounded-full text-xs font-semibold uppercase tracking-wider transition-colors cursor-pointer" data-filter="kids">Boys &amp; Girls</button>
        <button class="add-product-toggle-btn bg-slate-900 text-white px-4 py-2 rounded-full text-xs font-bold uppercase tracking-wider hover:bg-slate-800 transition-opacity flex items-center gap-1 cursor-pointer">
          <span class="material-symbols-outlined text-sm">add</span> + Add Item
        </button>
      </div>"""

with open(file, 'r') as f:
    content = f.read()
content = content.replace(old_filters, new_filters)
with open(file, 'w') as f:
    f.write(content)

