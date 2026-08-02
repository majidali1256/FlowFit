import os

with open('assets/js/main.js', 'r') as f:
    content = f.read()

import re

# We will replace renderFeaturedProducts and renderCollectionsProducts with a refactored version
start_func = 'function renderFeaturedProducts() {'
end_func = 'function renderCartDrawer() {'

start_idx = content.find(start_func)
end_idx = content.find(end_func)

new_funcs = """function createProductCardHTML(p) {
  // Randomly assign badges for the prototype
  const badgeVal = Math.random();
  let badgeHtml = '';
  if (badgeVal > 0.8) {
    badgeHtml = `<span class="absolute top-4 left-4 bg-rose-500 text-white text-[10px] font-bold px-3 py-1 rounded-full uppercase tracking-wider">Sale</span>`;
  } else if (badgeVal > 0.6) {
    badgeHtml = `<span class="absolute top-4 left-4 bg-emerald-500 text-white text-[10px] font-bold px-3 py-1 rounded-full uppercase tracking-wider">New</span>`;
  } else {
    badgeHtml = `<span class="absolute top-4 left-4 bg-slate-100 text-slate-800 text-[10px] font-bold px-3 py-1 rounded-full uppercase tracking-wider">${p.gender || 'All'}</span>`;
  }

  return `
    <article class="glass-panel rounded-3xl overflow-hidden soft-shadow hover-lift flex flex-col justify-between group relative" data-category="${p.category}" data-id="${p.id}">
      <div class="aspect-[4/3] bg-slate-50 p-6 flex items-center justify-center relative">
        <img src="${p.image}" alt="${p.name}" class="max-h-[220px] object-contain mix-blend-multiply group-hover:scale-105 transition-transform duration-500" />
        ${badgeHtml}
        
        <!-- Quick View Overlay -->
        <div class="absolute inset-0 bg-slate-900/10 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center backdrop-blur-[2px]">
          <button class="quick-view-btn bg-white/90 text-slate-900 rounded-full w-12 h-12 flex items-center justify-center hover:bg-slate-900 hover:text-white transition-all shadow-xl hover:scale-110 cursor-pointer" aria-label="Quick View" onclick="openQuickView('${p.id}')">
            <span class="material-symbols-outlined">visibility</span>
          </button>
        </div>
      </div>
      <div class="p-6 flex-1 flex flex-col justify-between relative z-10 bg-white">
        <div>
          <span class="text-[10px] uppercase tracking-widest text-slate-500 font-bold">${p.category.toUpperCase()}</span>
          <h3 class="font-headline-md text-xl font-bold text-slate-900 mt-1">${p.name}</h3>
          <p class="text-xs text-slate-500 mt-1">${p.colorway || 'Standard Fit'}</p>
        </div>

        <div class="flex gap-2 mt-4 size-selector-group">
          <button class="size-pill px-2.5 py-1 rounded text-xs font-semibold text-slate-700 bg-slate-100">S</button>
          <button class="size-pill active px-2.5 py-1 rounded text-xs font-semibold bg-slate-900 text-white">M</button>
          <button class="size-pill px-2.5 py-1 rounded text-xs font-semibold text-slate-700 bg-slate-100">L</button>
          <button class="size-pill px-2.5 py-1 rounded text-xs font-semibold text-slate-700 bg-slate-100">XL</button>
        </div>

        <div class="flex justify-between items-center mt-6">
          <span class="font-bold text-lg text-slate-900">$${p.price.toLocaleString()}</span>
          <button class="add-to-cart-btn bg-slate-900 text-white text-xs font-semibold uppercase tracking-wider px-5 py-2.5 rounded-lg btn-hover-lift flex items-center gap-2 cursor-pointer shadow-md shadow-slate-900/10">
            <span class="material-symbols-outlined text-sm">shopping_bag</span> Add
          </button>
        </div>
      </div>
    </article>
  `;
}

function renderFeaturedProducts() {
  const container = document.getElementById('featured-products-grid');
  if (!container) return;

  const catalog = getCombinedCatalog();
  const featured = catalog.slice(0, 6);

  container.innerHTML = featured.map(createProductCardHTML).join('');
}

function renderCollectionsProducts(filter = 'all', sort = 'featured') {
  const container = document.getElementById('collections-products-grid');
  if (!container) return;

  const catalog = getCombinedCatalog();
  let filtered = filter === 'all' 
    ? catalog 
    : catalog.filter(p => p.category === filter || p.id.includes(filter));

  if (sort === 'price-asc') {
    filtered.sort((a, b) => parseFloat(a.price) - parseFloat(b.price));
  } else if (sort === 'price-desc') {
    filtered.sort((a, b) => parseFloat(b.price) - parseFloat(a.price));
  } else if (sort === 'name-asc') {
    filtered.sort((a, b) => a.name.localeCompare(b.name));
  }

  container.innerHTML = '';

  if (filtered.length === 0) {
    container.innerHTML = `
      <div class="col-span-full py-12 text-center text-slate-500">
        <span class="material-symbols-outlined text-4xl mb-2">inventory_2</span>
        <p class="font-headline-md text-base text-slate-900">No products found in this category.</p>
      </div>
    `;
    return;
  }

  container.innerHTML = filtered.map(createProductCardHTML).join('');
}

"""

new_content = content[:start_idx] + new_funcs + content[end_idx:]

with open('assets/js/main.js', 'w') as f:
    f.write(new_content)

