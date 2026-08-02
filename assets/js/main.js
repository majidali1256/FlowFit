/**
 * FLOW WEAR — APPAREL STOREFRONT ENGINE
 * Global Event Delegation, Dynamic Catalog Renderer, Modals & Cart System.
 */

// Default Base Apparel Catalog
const DEFAULT_CATALOG_PRODUCTS = [
  {
    id: 'oversized-tee-01',
    name: 'Heavyweight Oversized Tee',
    category: 'shirts',
    gender: 'Men / Women / Kids',
    price: 65,
    image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuAJXctBq6dGKXdU_xb_MyTNETARrPJQH2oh_wRRJP3DTeNr3wxHOTplkB1eje3uue0zd1tG9jjggeefz6BDRs0kOQR2kdYsIg93SgBRor6738jygyI0VtcDiI6LdrJPRw6mBkuPvA91wLrUazCZCvevN0N3pGXZJLBpdiRyqcg4NbqqiH68b6379JrLZcMjFbc050L2nPRPm2KMnzJNKCqxfrSR_oBAdkp7a3vbFYYGmPJzHWf9CoL3Xw',
    colorway: 'Washed Black & Sand',
    description: '300 GSM combed organic cotton with relaxed drop-shoulder tailoring and reinforced crew collar.',
    sizes: ['S', 'M', 'L', 'XL']
  },
  {
    id: 'puffer-jacket-04',
    name: 'Insulated Urban Puffer Jacket',
    category: 'jackets',
    gender: 'All / Unisex',
    price: 220,
    image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuAJXctBq6dGKXdU_xb_MyTNETARrPJQH2oh_wRRJP3DTeNr3wxHOTplkB1eje3uue0zd1tG9jjggeefz6BDRs0kOQR2kdYsIg93SgBRor6738jygyI0VtcDiI6LdrJPRw6mBkuPvA91wLrUazCZCvevN0N3pGXZJLBpdiRyqcg4NbqqiH68b6379JrLZcMjFbc050L2nPRPm2KMnzJNKCqxfrSR_oBAdkp7a3vbFYYGmPJzHWf9CoL3Xw',
    colorway: 'Matte Obsidian Navy',
    description: 'Water-repellent ripstop shell with recycled thermal insulation and adjustable storm hood.',
    sizes: ['S', 'M', 'L', 'XL', 'XXL']
  },
  {
    id: 'utility-cargo-03',
    name: 'Tactical Utility Cargo Pants',
    category: 'pants',
    gender: 'Men / Women',
    price: 140,
    image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuAJXctBq6dGKXdU_xb_MyTNETARrPJQH2oh_wRRJP3DTeNr3wxHOTplkB1eje3uue0zd1tG9jjggeefz6BDRs0kOQR2kdYsIg93SgBRor6738jygyI0VtcDiI6LdrJPRw6mBkuPvA91wLrUazCZCvevN0N3pGXZJLBpdiRyqcg4NbqqiH68b6379JrLZcMjFbc050L2nPRPm2KMnzJNKCqxfrSR_oBAdkp7a3vbFYYGmPJzHWf9CoL3Xw',
    colorway: 'Olive Drab & Charcoal',
    description: 'Ergonomic stretch-cotton twill with 6 multi-functional storage pockets and ankle drawcords.',
    sizes: ['XS', 'S', 'M', 'L', 'XL']
  },
  {
    id: 'streetwear-cap-05',
    name: 'Embroidered Strapback Cap',
    category: 'caps',
    gender: 'All / Boys & Girls',
    price: 45,
    image: 'https://lh3.googleusercontent.com/aida/AP1WRLvKZ5LDIRYOddqxqKBSi5T3dK2VVK8SFnBB6R4rmAsZeXAvfdw5Znd8cEJQpu_Nf8CI23V6qUNkIQGwQ0r5bTfI_6ZhmpxHF4L1kbDpwVKZZ0XXS8JrDAaO6f86ZHojw-p3UvYiIJg2cu8-15YEsf_WJgyGyXqQshPe5ysOpuef_WUuY9uWdgFk6prsI8wXbdhwG1P-1oJU9mC4UPq6-I7sU4bJ5MP78g6yrihWMVzPjt41Jt3sadD21wU',
    colorway: 'Vintage Beige & Navy',
    description: '100% heavy cotton canvas 6-panel hat with brass buckle closure and subtle tonal logo embroidery.',
    sizes: ['One Size']
  },
  {
    id: 'oxford-shirt-07',
    name: 'Relaxed Oxford Cotton Shirt',
    category: 'shirts',
    gender: 'Men / Women',
    price: 95,
    image: 'https://lh3.googleusercontent.com/aida/AP1WRLvKZ5LDIRYOddqxqKBSi5T3dK2VVK8SFnBB6R4rmAsZeXAvfdw5Znd8cEJQpu_Nf8CI23V6qUNkIQGwQ0r5bTfI_6ZhmpxHF4L1kbDpwVKZZ0XXS8JrDAaO6f86ZHojw-p3UvYiIJg2cu8-15YEsf_WJgyGyXqQshPe5ysOpuef_WUuY9uWdgFk6prsI8wXbdhwG1P-1oJU9mC4UPq6-I7sU4bJ5MP78g6yrihWMVzPjt41Jt3sadD21wU',
    colorway: 'Classic White & Stripe',
    description: 'Breathable pin-point Oxford cloth tailored for effortless casual and semi-formal wear.',
    sizes: ['S', 'M', 'L', 'XL']
  },
  {
    id: 'chino-trousers-08',
    name: 'Pleated Tapered Trousers',
    category: 'pants',
    gender: 'Men / Women',
    price: 120,
    image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuAJXctBq6dGKXdU_xb_MyTNETARrPJQH2oh_wRRJP3DTeNr3wxHOTplkB1eje3uue0zd1tG9jjggeefz6BDRs0kOQR2kdYsIg93SgBRor6738jygyI0VtcDiI6LdrJPRw6mBkuPvA91wLrUazCZCvevN0N3pGXZJLBpdiRyqcg4NbqqiH68b6379JrLZcMjFbc050L2nPRPm2KMnzJNKCqxfrSR_oBAdkp7a3vbFYYGmPJzHWf9CoL3Xw',
    colorway: 'Camel & Off-White',
    description: 'Double-pleated waist with a clean tapered hem, engineered for modern movement and comfort.',
    sizes: ['S', 'M', 'L', 'XL']
  },
  {
    id: 'youth-hoodie-06',
    name: 'Kids Essential Fleece Hoodie',
    category: 'kids',
    gender: 'Boys & Girls',
    price: 55,
    image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuAJXctBq6dGKXdU_xb_MyTNETARrPJQH2oh_wRRJP3DTeNr3wxHOTplkB1eje3uue0zd1tG9jjggeefz6BDRs0kOQR2kdYsIg93SgBRor6738jygyI0VtcDiI6LdrJPRw6mBkuPvA91wLrUazCZCvevN0N3pGXZJLBpdiRyqcg4NbqqiH68b6379JrLZcMjFbc050L2nPRPm2KMnzJNKCqxfrSR_oBAdkp7a3vbFYYGmPJzHWf9CoL3Xw',
    colorway: 'Soft Blush & Heather Grey',
    description: 'Ultra-soft brushed fleece pullover hoodie designed for active kids and everyday comfort.',
    sizes: ['YS', 'YM', 'YL']
  }
];

const STORE_CUSTOM_PRODUCTS_KEY = 'flow_wear_custom_products';
const STORE_CART_KEY = 'flow_wear_clothing_cart';

function getCustomProducts() {
  try {
    return JSON.parse(localStorage.getItem(STORE_CUSTOM_PRODUCTS_KEY)) || [];
  } catch (e) {
    return [];
  }
}

function saveCustomProducts(products) {
  localStorage.setItem(STORE_CUSTOM_PRODUCTS_KEY, JSON.stringify(products));
}

function getCombinedCatalog() {
  return [...DEFAULT_CATALOG_PRODUCTS, ...getCustomProducts()];
}

document.addEventListener('DOMContentLoaded', () => {
  initAdminMode();
  renderFeaturedProducts();
  renderCollectionsProducts('all');
  renderCartDrawer();
  updateCartBadge();
  initAddProductFormSubmit();
  initCheckoutConfirm();
  initWebGLBackgroundShader();
});

/* ==========================================================================
   1. BULLETPROOF MODAL TOGGLE ENGINE
   ========================================================================== */
function toggleModal(modalId, show) {
  const modal = document.getElementById(modalId);
  if (!modal) return;

  if (show) {
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  } else {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }
}

/* ==========================================================================
   2. GLOBAL CLICK EVENT DELEGATION (100% GUARANTEED RELIABLE CLICK HANDLERS)
   ========================================================================== */
document.addEventListener('click', (e) => {
  // 1. Add Product Trigger
  const addProdBtn = e.target.closest('.add-product-toggle-btn');
  if (addProdBtn) {
    e.preventDefault();
    toggleModal('add-product-modal', true);
    return;
  }

  // 2. Navigation Side Drawer Toggle
  const navDrawerBtn = e.target.closest('#drawer-toggle, .drawer-toggle-btn');
  if (navDrawerBtn) {
    e.preventDefault();
    toggleModal('side-drawer', true);
    return;
  }
  if (e.target.closest('#drawer-close, #drawer-overlay')) {
    e.preventDefault();
    toggleModal('side-drawer', false);
    return;
  }
  if (e.target.closest('#account-drawer .drawer-panel')) {
    e.stopPropagation();
  }

  // 3. Cart Drawer Toggle
  const cartBtn = e.target.closest('.cart-toggle-btn');
  if (cartBtn) {
    e.preventDefault();
    renderCartDrawer();
    toggleModal('cart-drawer', true);
    return;
  }
  if (e.target.closest('#cart-close, #cart-overlay')) {
    e.preventDefault();
    toggleModal('cart-drawer', false);
    return;
  }

  // 4. Search Overlay Toggle
  const searchBtn = e.target.closest('.search-toggle-btn');
  if (searchBtn) {
    e.preventDefault();
    toggleModal('search-overlay', true);
    const searchInput = document.getElementById('search-input');
    if (searchInput) {
      searchInput.value = '';
      setTimeout(() => searchInput.focus(), 150);
    }
    renderSearchResults('');
    return;
  }
  if (e.target.closest('#search-close, #search-backdrop')) {
    e.preventDefault();
    toggleModal('search-overlay', false);
    return;
  }

  // 5. Account Drawer Toggle
  const accountBtn = e.target.closest('.account-toggle-btn');
  if (accountBtn) {
    e.preventDefault();
    toggleModal('account-drawer', true);
    return;
  }
  if (e.target.closest('#account-close, #account-overlay')) {
    e.preventDefault();
    toggleModal('account-drawer', false);
    return;
  }

  // 6. Add Product Modal Close
  if (e.target.closest('#add-product-close, #add-product-backdrop')) {
    e.preventDefault();
    toggleModal('add-product-modal', false);
    return;
  }

  // 7. Checkout Modal Toggle & Close
  const checkoutBtn = e.target.closest('.proceed-checkout-btn');
  if (checkoutBtn) {
    e.preventDefault();
    const items = getCartItems();
    if (items.length === 0) {
      alert('Your wardrobe bag is empty.');
      return;
    }
    toggleModal('cart-drawer', false);
    renderCheckoutSummary();
    toggleModal('checkout-modal', true);
    return;
  }
  if (e.target.closest('#checkout-close, #checkout-backdrop')) {
    e.preventDefault();
    toggleModal('checkout-modal', false);
    return;
  }

  // 8. Size Pill Selector Toggle
  const pill = e.target.closest('.size-pill');
  if (pill) {
    e.preventDefault();
    const group = pill.closest('.size-selector-group');
    if (group) {
      group.querySelectorAll('.size-pill').forEach(p => p.classList.remove('active', 'bg-slate-900', 'text-white'));
      pill.classList.add('active', 'bg-slate-900', 'text-white');
      const card = group.closest('article');
      const addBtn = card ? card.querySelector('.add-to-bag-btn') : null;
      if (addBtn) {
        addBtn.setAttribute('data-size', pill.textContent.trim());
      }
    }
    return;
  }

  // 9. Add to Bag Button Handler
  const addToBagBtn = e.target.closest('.add-to-bag-btn');
  if (addToBagBtn) {
    e.preventDefault();
    const id = addToBagBtn.getAttribute('data-id');
    const size = addToBagBtn.getAttribute('data-size') || 'M';
    const catalog = getCombinedCatalog();
    const prod = catalog.find(p => p.id === id) || {
      name: addToBagBtn.getAttribute('data-name') || 'Apparel Item',
      price: parseFloat(addToBagBtn.getAttribute('data-price')) || 65,
      image: addToBagBtn.getAttribute('data-image') || '',
      colorway: addToBagBtn.getAttribute('data-color') || 'Standard'
    };

    const items = getCartItems();
    const existing = items.find(item => item.id === id && item.size === size);
    if (existing) {
      existing.quantity += 1;
    } else {
      items.push({
        id: prod.id,
        name: prod.name,
        price: prod.price,
        size: size,
        image: prod.image,
        quantity: 1,
        colorway: prod.colorway
      });
    }
    saveCartItems(items);
    showCartToast(`${prod.name} (${size}) added to bag`);
    toggleModal('cart-drawer', true);
    return;
  }

  // 10. Filter Chips on Collections Page
  const filterBtn = e.target.closest('.filter-chip-btn');
  if (filterBtn) {
    e.preventDefault();
    document.querySelectorAll('.filter-chip-btn').forEach(b => {
      b.classList.remove('bg-slate-900', 'text-white');
      b.classList.add('bg-slate-100', 'text-slate-700');
    });
    filterBtn.classList.remove('bg-slate-100', 'text-slate-700');
    filterBtn.classList.add('bg-slate-900', 'text-white');
    const filterVal = filterBtn.getAttribute('data-filter');
    
    const sortSelect = document.getElementById('sort-by-select');
    const sortVal = sortSelect ? sortSelect.value : 'featured';

    renderCollectionsProducts(filterVal, sortVal);
    return;
  }
});

// Search input listener
document.addEventListener('input', (e) => {
  if (e.target && e.target.id === 'search-input') {
    renderSearchResults(e.target.value);
  }
});

document.addEventListener('change', (e) => {
  if (e.target.id === 'sort-by-select') {
    const sortVal = e.target.value;
    const activeFilterBtn = document.querySelector('.filter-chip-btn.bg-slate-900');
    const filterVal = activeFilterBtn ? activeFilterBtn.getAttribute('data-filter') : 'all';
    renderCollectionsProducts(filterVal, sortVal);
  }
});

/* ==========================================================================
   3. DYNAMIC PRODUCT GRID RENDERERS
   ========================================================================== */
function createProductCardHTML(p) {
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

function renderCartDrawer() {
  const container = document.getElementById('cart-items-container');
  const subtotalRawEl = document.getElementById('cart-subtotal-raw');
  const subtotalFinalEl = document.getElementById('cart-subtotal');
  const discountRow = document.getElementById('discount-row');
  const discountEl = document.getElementById('cart-discount');
  const shippingMsg = document.getElementById('shipping-message');
  const shippingBar = document.getElementById('shipping-progress-bar');
  const shippingSuccess = document.getElementById('shipping-success-icon');
  
  if (!container) return;

  const items = getCartItems();
  container.innerHTML = '';

  if (items.length === 0) {
    container.innerHTML = `
      <div class="flex flex-col items-center justify-center py-16 text-center">
        <span class="material-symbols-outlined text-4xl text-slate-300 mb-3">checkroom</span>
        <p class="font-headline-md text-lg text-slate-900 mb-1">Your bag is empty</p>
        <a href="collections.html" class="mt-6 bg-slate-900 text-white text-xs font-semibold uppercase tracking-wider px-6 py-3 rounded-lg btn-hover-lift inline-block cursor-pointer">Shop Now</a>
      </div>
    `;
    if(subtotalFinalEl) subtotalFinalEl.textContent = '$0.00';
    if(subtotalRawEl) subtotalRawEl.textContent = '$0.00';
    if(discountRow) discountRow.style.display = 'none';
    if(shippingBar) shippingBar.style.width = '0%';
    if(shippingMsg) shippingMsg.textContent = 'Free shipping on orders over $75';
    return;
  }

  let rawSubtotal = 0;
  items.forEach(item => {
    rawSubtotal += item.price * item.quantity;
    const itemEl = document.createElement('div');
    itemEl.className = 'flex items-center gap-4 py-4 border-b border-slate-100';
    itemEl.innerHTML = `
      <img src="${item.image}" alt="${item.name}" class="w-16 h-16 object-contain rounded-lg bg-slate-50 p-1 border border-slate-100" />
      <div class="flex-1 min-w-0">
        <h4 class="font-headline-md text-sm font-semibold text-slate-900 truncate">${item.name}</h4>
        <p class="text-xs text-slate-500">Size <span class="font-bold text-slate-900">${item.size || 'M'}</span></p>
        <p class="text-sm font-semibold text-slate-900 mt-1">$${item.price.toLocaleString()}</p>
      </div>
      <div class="flex items-center gap-2">
        <button class="cart-qty-btn w-7 h-7 rounded bg-slate-100 hover:bg-slate-200 flex items-center justify-center text-slate-900 text-xs font-bold cursor-pointer" data-action="dec" data-id="${item.id}" data-size="${item.size}">-</button>
        <span class="text-sm font-semibold w-4 text-center">${item.quantity}</span>
        <button class="cart-qty-btn w-7 h-7 rounded bg-slate-100 hover:bg-slate-200 flex items-center justify-center text-slate-900 text-xs font-bold cursor-pointer" data-action="inc" data-id="${item.id}" data-size="${item.size}">+</button>
      </div>
    `;
    container.appendChild(itemEl);
  });

  // Calculate Discount
  let discount = 0;
  const activePromo = localStorage.getItem('flow_wear_promo');
  if (activePromo === 'FLOW10') {
    discount = rawSubtotal * 0.10;
    if(discountRow) {
      discountRow.style.display = 'flex';
      discountEl.textContent = `-$${discount.toFixed(2)}`;
    }
  } else {
    if(discountRow) discountRow.style.display = 'none';
  }

  const finalTotal = rawSubtotal - discount;

  if(subtotalRawEl) subtotalRawEl.textContent = `$${rawSubtotal.toFixed(2)}`;
  if(subtotalFinalEl) subtotalFinalEl.textContent = `$${finalTotal.toFixed(2)}`;

  // Calculate Shipping Threshold
  const threshold = 75.00;
  if(shippingBar && shippingMsg && shippingSuccess) {
    if (finalTotal >= threshold) {
      shippingBar.style.width = '100%';
      shippingBar.classList.remove('bg-emerald-500', 'bg-amber-400');
      shippingBar.classList.add('bg-emerald-500');
      shippingMsg.textContent = 'You have unlocked free shipping!';
      shippingSuccess.classList.remove('hidden');
    } else {
      const remaining = threshold - finalTotal;
      const pct = (finalTotal / threshold) * 100;
      shippingBar.style.width = `${pct}%`;
      shippingBar.classList.remove('bg-emerald-500');
      shippingBar.classList.add('bg-amber-400');
      shippingMsg.textContent = `You are $${remaining.toFixed(2)} away from free shipping!`;
      shippingSuccess.classList.add('hidden');
    }
  }

  container.querySelectorAll('.cart-qty-btn').forEach(btn => {
    btn.onclick = (e) => {
      e.preventDefault();
      const id = btn.getAttribute('data-id');
      const size = btn.getAttribute('data-size');
      const action = btn.getAttribute('data-action');
      let currentItems = getCartItems();
      const index = currentItems.findIndex(i => i.id === id && i.size === size);
      if (index > -1) {
        if (action === 'inc') currentItems[index].quantity += 1;
        else if (action === 'dec') {
          currentItems[index].quantity -= 1;
          if (currentItems[index].quantity <= 0) currentItems.splice(index, 1);
        }
        saveCartItems(currentItems);
      }
    };
  });
}

function showCartToast(itemName) {
  const toast = document.getElementById('cart-toast');
  const toastTitle = document.getElementById('cart-toast-title');
  if (!toast || !toastTitle) return;
  toastTitle.textContent = itemName;
  toast.classList.remove('translate-y-24', 'opacity-0');
  setTimeout(() => {
    toast.classList.add('translate-y-24', 'opacity-0');
  }, 2800);
}

function renderCheckoutSummary() {
  const summaryContainer = document.getElementById('checkout-summary-items');
  const totalEl = document.getElementById('checkout-final-total');
  if (!summaryContainer || !totalEl) return;

  const items = getCartItems();
  let total = 0;

  summaryContainer.innerHTML = items.map(item => {
    const itemTotal = item.price * item.quantity;
    total += itemTotal;
    return `
      <div class="flex justify-between items-center text-xs py-1">
        <span class="text-slate-900 font-semibold">${item.name} (${item.size || 'M'}) x${item.quantity}</span>
        <span class="text-slate-600">$${itemTotal.toLocaleString()}.00</span>
      </div>
    `;
  }).join('');

  totalEl.textContent = `$${total.toLocaleString()}.00`;
}

function renderSearchResults(query) {
  const container = document.getElementById('search-results');
  if (!container) return;

  const cleanQuery = query.trim().toLowerCase();
  const catalog = getCombinedCatalog();
  const matches = catalog.filter(p => 
    p.name.toLowerCase().includes(cleanQuery) || 
    p.category.toLowerCase().includes(cleanQuery) ||
    (p.gender && p.gender.toLowerCase().includes(cleanQuery))
  );

  if (matches.length === 0) {
    container.innerHTML = `
      <div class="py-12 text-center text-slate-500">
        <span class="material-symbols-outlined text-4xl mb-2">search_off</span>
        <p class="font-headline-md text-base text-slate-900">No apparel matching "${query}"</p>
      </div>
    `;
    return;
  }

  container.innerHTML = matches.map(p => `
    <div class="flex items-center justify-between p-3.5 rounded-2xl bg-white hover:bg-slate-50 border border-slate-100 transition-colors">
      <div class="flex items-center gap-3">
        <img src="${p.image}" alt="${p.name}" class="w-12 h-12 object-contain rounded-xl bg-slate-50 p-1" />
        <div>
          <a href="product.html" class="font-headline-md text-sm font-bold text-slate-900 hover:text-slate-700 block">
            ${p.name}
          </a>
          <p class="text-xs text-slate-500">${p.colorway || ''} · ${p.gender || 'All'}</p>
        </div>
      </div>
      <div class="flex items-center gap-3">
        <span class="text-sm font-bold text-slate-900">$${p.price}</span>
        <button class="add-to-bag-btn bg-slate-900 text-white text-xs font-semibold px-3 py-1.5 rounded-lg btn-hover-lift cursor-pointer"
          data-id="${p.id}" data-name="${p.name}" data-price="${p.price}" data-size="M" data-image="${p.image}" data-color="${p.colorway}">
          Add
        </button>
      </div>
    </div>
  `).join('');
}

/* ==========================================================================
   6. WEBGL AMBIENT BACKGROUND SHADER
   ========================================================================== */
function initWebGLBackgroundShader() {
  try {
    const canvas = document.getElementById('global-shader-canvas');
    if (!canvas) return;

    function syncSize() {
      const w = window.innerWidth;
      const h = window.innerHeight;
      if (canvas.width !== w || canvas.height !== h) {
        canvas.width = w;
        canvas.height = h;
      }
    }
    syncSize();
    window.addEventListener('resize', syncSize);

    const gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
    if (!gl) return;

    const vs = `
      attribute vec2 a_position;
      varying vec2 v_texCoord;
      void main() {
        v_texCoord = a_position * 0.5 + 0.5;
        gl_Position = vec4(a_position, 0.0, 1.0);
      }
    `;

    const fs = `
      precision mediump float;
      uniform float u_time;
      varying vec2 v_texCoord;

      void main() {
        vec2 uv = v_texCoord;
        float wave = sin(uv.x * 2.0 + u_time * 0.2) * 0.5 + 0.5;
        vec3 white = vec3(0.99, 0.99, 1.0);
        vec3 softBlue = vec3(0.95, 0.96, 0.98);
        vec3 color = mix(white, softBlue, wave * 0.3);
        gl_FragColor = vec4(color, 1.0);
      }
    `;

    function createShader(type, source) {
      const s = gl.createShader(type);
      gl.shaderSource(s, source);
      gl.compileShader(s);
      return s;
    }

    const prog = gl.createProgram();
    gl.attachShader(prog, createShader(gl.VERTEX_SHADER, vs));
    gl.attachShader(prog, createShader(gl.FRAGMENT_SHADER, fs));
    gl.linkProgram(prog);
    gl.useProgram(prog);

    const buf = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, buf);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 1, -1, -1, 1, 1, 1]), gl.STATIC_DRAW);

    const pos = gl.getAttribLocation(prog, 'a_position');
    gl.enableVertexAttribArray(pos);
    gl.vertexAttribPointer(pos, 2, gl.FLOAT, false, 0, 0);

    const uTime = gl.getUniformLocation(prog, 'u_time');

    function render(time) {
      gl.viewport(0, 0, canvas.width, canvas.height);
      if (uTime) gl.uniform1f(uTime, time * 0.001);
      gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
      requestAnimationFrame(render);
    }
    render(0);
  } catch (err) {
    console.warn('WebGL shader skipped:', err);
  }
}

/* ==========================================================================
   ADMIN / OWNER MODE LOGIC
   ========================================================================== */
function initAdminMode() {
  const isAdmin = localStorage.getItem('flow_wear_admin_mode') === 'true';
  if (isAdmin) {
    document.body.classList.add('admin-mode');
    document.querySelectorAll('#account-login-form').forEach(f => f.style.display = 'none');
    document.querySelectorAll('#admin-logged-in-view').forEach(v => v.style.display = 'block');
  }

  // Handle Login
  document.querySelectorAll('#account-login-form').forEach(form => {
    form.onsubmit = (e) => {
      e.preventDefault();
      localStorage.setItem('flow_wear_admin_mode', 'true');
      window.location.reload();
    };
  });

  // Handle Logout
  document.querySelectorAll('#admin-logout-btn').forEach(btn => {
    btn.onclick = () => {
      localStorage.removeItem('flow_wear_admin_mode');
      alert('Logged out successfully.');
      window.location.reload();
    };
  });
}

document.addEventListener('DOMContentLoaded', () => {
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
});

/* ==========================================================================
   QUICK VIEW LOGIC
   ========================================================================== */
window.openQuickView = function(productId) {
  const catalog = getCombinedCatalog();
  const product = catalog.find(p => p.id === productId);
  if (!product) return;

  const titleEl = document.getElementById('qv-title');
  const priceEl = document.getElementById('qv-price');
  const imgEl = document.getElementById('qv-image');
  const addBtn = document.getElementById('qv-add-to-cart');
  
  if (titleEl) titleEl.textContent = product.name;
  if (priceEl) priceEl.textContent = `$${product.price.toLocaleString()}`;
  if (imgEl) imgEl.src = product.image;
  if (addBtn) {
    addBtn.onclick = () => {
      let items = getCartItems();
      const existing = items.find(i => i.id === product.id && i.size === 'M');
      if (existing) {
        existing.quantity += 1;
      } else {
        items.push({
          id: product.id,
          name: product.name,
          price: product.price,
          image: product.image,
          size: 'M',
          color: product.colorway || 'Standard',
          quantity: 1
        });
      }
      saveCartItems(items);
      toggleModal('quick-view-modal', false);
      showCartToast(product.name);
    };
  }

  toggleModal('quick-view-modal', true);
};

// Add quick view close listener
document.addEventListener('click', (e) => {
  if (e.target.closest('#qv-close, #qv-backdrop')) {
    e.preventDefault();
    toggleModal('quick-view-modal', false);
  }
});
