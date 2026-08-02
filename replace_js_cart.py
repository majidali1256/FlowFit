import os

with open('assets/js/main.js', 'r') as f:
    content = f.read()

import re

# We will replace the entire renderCartDrawer function.
# Let's just use string slicing based on indexOf.

start_func = 'function renderCartDrawer() {'
end_func = 'function showCartToast'

start_idx = content.find(start_func)
end_idx = content.find(end_func)

new_func = """function renderCartDrawer() {
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

"""

new_content = content[:start_idx] + new_func + content[end_idx:]

with open('assets/js/main.js', 'w') as f:
    f.write(new_content)

