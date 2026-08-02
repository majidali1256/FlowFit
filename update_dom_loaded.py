import os

with open('assets/js/main.js', 'r') as f:
    content = f.read()

start_block = """document.addEventListener('DOMContentLoaded', () => {
  initAdminMode();
  renderFeaturedProducts();
  renderCollectionsProducts('all');
  renderCartDrawer();
  updateCartBadge();
  initAddProductFormSubmit();
  initCheckoutConfirm();
  initWebGLBackgroundShader();
});"""

new_block = """document.addEventListener('DOMContentLoaded', () => {
  initAdminMode();
  renderFeaturedProducts();
  
  const urlParams = new URLSearchParams(window.location.search);
  const catParam = urlParams.get('category');
  const initialCategory = catParam ? decodeURIComponent(catParam) : 'all';
  
  renderCollectionsProducts(initialCategory);
  
  if (catParam) {
    const allBtns = document.querySelectorAll('.filter-chip-btn');
    allBtns.forEach(btn => {
      if (btn.getAttribute('data-filter') === initialCategory) {
        btn.classList.remove('bg-slate-100', 'text-slate-700');
        btn.classList.add('bg-slate-900', 'text-white');
      } else {
        btn.classList.remove('bg-slate-900', 'text-white');
        btn.classList.add('bg-slate-100', 'text-slate-700');
      }
    });
  }

  renderCartDrawer();
  updateCartBadge();
  initAddProductFormSubmit();
  initCheckoutConfirm();
  initWebGLBackgroundShader();
  
  const promoBtn = document.getElementById('apply-promo-btn');
  if (promoBtn) {
    promoBtn.onclick = (e) => {
      e.preventDefault();
      const input = document.getElementById('promo-code-input');
      if (input && input.value.toUpperCase() === 'FLOW10') {
        localStorage.setItem('flow_wear_promo', 'FLOW10');
        renderCartDrawer();
      } else {
        alert('Invalid or expired promo code.');
      }
    };
  }
});"""

content = content.replace(start_block, new_block)

# Wait, the promo code block was added previously via `cat << EOF >> assets/js/main.js`. 
# So there's another DOMContentLoaded block at the bottom of the file! 
# Let me remove the last one and consolidate it.
