/**
 * FOUR FIT — SHOPIFY THEME STOREFRONT JAVASCRIPT ENGINE
 * Integrates WebGL Liquid Shader, High-Fidelity Three.js 3D Architectural Sculptures,
 * Shopify Ajax Cart System, & Smooth Scroll Reveal Animations.
 */

document.addEventListener('DOMContentLoaded', () => {
  initScrollReveal();
  initShopifyDrawers();
  initShopifyAjaxCart();
});

/* ==========================================================================
   1. SMOOTH SCROLL REVEAL ANIMATIONS
   ========================================================================== */
function initScrollReveal() {
  const revealElements = document.querySelectorAll('.reveal');
  if (!revealElements.length) return;

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -30px 0px'
  });

  revealElements.forEach(el => revealObserver.observe(el));

  setTimeout(() => {
    revealElements.forEach(el => {
      const rect = el.getBoundingClientRect();
      if (rect.top < window.innerHeight - 30) {
        el.classList.add('active');
      }
    });
  }, 80);
}

/* ==========================================================================
   2. SHOPIFY DRAWER NAVIGATION & CART
   ========================================================================== */
function initShopifyDrawers() {
  const navDrawer = document.getElementById('side-drawer');
  const navContent = document.getElementById('drawer-content');
  const cartDrawer = document.getElementById('cart-drawer');
  const cartContent = document.getElementById('cart-drawer-content');

  document.querySelectorAll('#drawer-toggle').forEach(btn => {
    btn.addEventListener('click', () => {
      navDrawer?.classList.remove('pointer-events-none', 'opacity-0');
      navContent?.classList.remove('-translate-x-full');
      document.body.style.overflow = 'hidden';
    });
  });

  document.querySelectorAll('#drawer-close, #drawer-overlay').forEach(btn => {
    btn.addEventListener('click', () => {
      navDrawer?.classList.add('pointer-events-none', 'opacity-0');
      navContent?.classList.add('-translate-x-full');
      document.body.style.overflow = '';
    });
  });

  document.querySelectorAll('.cart-toggle-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      cartDrawer?.classList.remove('pointer-events-none', 'opacity-0');
      cartContent?.classList.remove('translate-x-full');
      document.body.style.overflow = 'hidden';
      fetchShopifyCart();
    });
  });

  document.querySelectorAll('#cart-close, #cart-overlay').forEach(btn => {
    btn.addEventListener('click', () => {
      cartDrawer?.classList.add('pointer-events-none', 'opacity-0');
      cartContent?.classList.add('translate-x-full');
      document.body.style.overflow = '';
    });
  });
}

function initShopifyAjaxCart() {
  document.querySelectorAll('form[action^="/cart/add"]').forEach(form => {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const formData = new FormData(form);
      try {
        const res = await fetch('/cart/add.js', {
          method: 'POST',
          body: formData
        });
        const item = await res.json();
        fetchShopifyCart();
        const cartDrawer = document.getElementById('cart-drawer');
        const cartContent = document.getElementById('cart-drawer-content');
        cartDrawer?.classList.remove('pointer-events-none', 'opacity-0');
        cartContent?.classList.remove('translate-x-full');
      } catch (err) {
        form.submit();
      }
    });
  });
}

async function fetchShopifyCart() {
  const container = document.getElementById('cart-items-container');
  const subtotalEl = document.getElementById('cart-subtotal-price');
  if (!container || !subtotalEl) return;

  try {
    const res = await fetch('/cart.js');
    const cart = await res.json();

    document.querySelectorAll('.cart-count-badge').forEach(b => {
      b.textContent = cart.item_count;
      b.style.display = cart.item_count > 0 ? 'inline-flex' : 'none';
    });

    subtotalEl.textContent = `${(cart.total_price / 100).toLocaleString('en-US', { style: 'currency', currency: 'USD' })}`;

    if (cart.items.length === 0) {
      container.innerHTML = `
        <div class="py-16 text-center">
          <p class="font-headline-md text-lg text-primary">Your bag is empty</p>
        </div>
      `;
      return;
    }

    container.innerHTML = '';
    cart.items.forEach(item => {
      const el = document.createElement('div');
      el.className = 'flex items-center gap-4 py-4 border-b border-primary/10';
      el.innerHTML = `
        <img src="${item.image}" alt="${item.title}" class="w-16 h-16 object-contain rounded-lg bg-surface-container-low p-1" />
        <div class="flex-1">
          <h4 class="font-headline-md text-sm font-semibold text-primary">${item.product_title}</h4>
          <p class="text-xs text-on-surface-variant">${item.variant_title || ''}</p>
          <p class="text-sm font-semibold text-primary mt-1">$${(item.price / 100).toFixed(2)}</p>
        </div>
        <span class="text-sm font-semibold">Qty: ${item.quantity}</span>
      `;
      container.appendChild(el);
    });
  } catch (e) {
    // Fallback if local preview outside Shopify
  }
}

