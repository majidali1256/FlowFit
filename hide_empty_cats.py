import os

with open('assets/js/main.js', 'r') as f:
    content = f.read()

start_block = """document.addEventListener('DOMContentLoaded', () => {
  initAdminMode();
  renderFeaturedProducts();"""

new_block = """document.addEventListener('DOMContentLoaded', () => {
  initAdminMode();
  renderFeaturedProducts();

  const catalog = getCombinedCatalog();
  const availableCategories = new Set(catalog.map(p => p.category));
  
  // Hide empty categories in side drawer
  document.querySelectorAll('#side-drawer nav a').forEach(a => {
    const href = a.getAttribute('href');
    if (href && href.includes('collections.html?category=')) {
      const cat = new URLSearchParams(href.split('?')[1]).get('category');
      if (cat && !availableCategories.has(cat)) {
        a.style.display = 'none';
      }
    }
  });

  // Hide empty categories in filter chips
  document.querySelectorAll('.filter-chip-btn').forEach(btn => {
    const cat = btn.getAttribute('data-filter');
    if (cat !== 'all' && !availableCategories.has(cat)) {
      btn.style.display = 'none';
    }
  });"""

content = content.replace(start_block, new_block)

with open('assets/js/main.js', 'w') as f:
    f.write(content)

