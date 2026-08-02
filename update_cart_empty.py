import os

with open('assets/js/main.js', 'r') as f:
    content = f.read()

start_block = """  if (items.length === 0) {
    container.innerHTML = `
      <div class="flex flex-col items-center justify-center py-16 text-center">
        <span class="material-symbols-outlined text-4xl text-slate-300 mb-3">checkroom</span>
        <p class="font-headline-md text-lg text-slate-900 mb-1">Your bag is empty</p>
        <a href="collections.html" class="mt-6 bg-slate-900 text-white text-xs font-semibold uppercase tracking-wider px-6 py-3 rounded-lg btn-hover-lift inline-block cursor-pointer">Shop Now</a>
      </div>
    `;"""

new_block = """  if (items.length === 0) {
    const catalog = getCombinedCatalog();
    const trending = catalog.slice(0, 2);
    const trendingHtml = trending.map(p => `
      <div class="flex gap-4 items-center p-3 border border-slate-100 rounded-2xl bg-white hover:border-slate-300 transition-colors cursor-pointer group" onclick="openQuickView('${p.id}')">
        <img src="${p.image}" class="w-16 h-16 object-contain bg-slate-50 rounded-xl group-hover:scale-105 transition-transform" />
        <div class="flex-1 text-left">
          <p class="text-xs font-bold text-slate-900 truncate">${p.name}</p>
          <p class="text-xs text-slate-500">$${p.price.toLocaleString()}</p>
        </div>
        <span class="material-symbols-outlined text-slate-300 group-hover:text-slate-900 transition-colors">add_circle</span>
      </div>
    `).join('');

    container.innerHTML = `
      <div class="flex flex-col items-center justify-center py-8 text-center border-b border-slate-100 mb-6">
        <span class="material-symbols-outlined text-4xl text-slate-300 mb-3">checkroom</span>
        <p class="font-headline-md text-lg text-slate-900 mb-1">Your bag is empty</p>
        <a href="collections.html" class="mt-4 bg-slate-900 text-white text-[10px] font-semibold uppercase tracking-wider px-5 py-2.5 rounded-lg btn-hover-lift inline-block cursor-pointer">Shop Now</a>
      </div>
      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-slate-500 mb-3 text-center">Trending Right Now</p>
        <div class="space-y-3">
          ${trendingHtml}
        </div>
      </div>
    `;"""

content = content.replace(start_block, new_block)

with open('assets/js/main.js', 'w') as f:
    f.write(content)

