import os

files = ['index.html', 'collections.html', 'product.html', 'new-arrivals.html']

old_cart = """      <div class="p-6 border-b border-slate-100 flex justify-between items-center bg-white/50 backdrop-blur-md">
        <h2 class="font-headline-md text-2xl font-bold text-slate-900 flex items-center gap-2">
          Your Bag
          <span class="cart-count-badge bg-slate-900 text-white text-xs px-2 py-0.5 rounded-full">0</span>
        </h2>
        <button id="cart-close" class="text-slate-900 hover:text-slate-600 transition-colors cursor-pointer">
          <span class="material-symbols-outlined">close</span>
        </button>
      </div>

      <div id="cart-items-container" class="flex-1 overflow-y-auto p-6 space-y-6">
        <!-- Cart Items Injected Here -->
      </div>

      <div class="p-6 bg-slate-50 border-t border-slate-200/80">
        <div class="flex justify-between items-center mb-6">
          <span class="text-sm font-semibold text-slate-500 uppercase tracking-wider">Subtotal</span>
          <span id="cart-subtotal" class="font-headline-md text-2xl font-bold text-slate-900">$0.00</span>
        </div>
        <button id="checkout-btn" class="w-full bg-slate-900 text-white font-semibold text-sm py-4 rounded-xl uppercase tracking-widest hover:bg-slate-800 transition-colors cursor-pointer shadow-lg shadow-slate-900/20">
          Proceed to Checkout
        </button>
      </div>"""

new_cart = """      <div class="p-6 border-b border-slate-100 bg-white/50 backdrop-blur-md flex flex-col gap-4">
        <div class="flex justify-between items-center">
          <h2 class="font-headline-md text-2xl font-bold text-slate-900 flex items-center gap-2">
            Your Bag
            <span class="cart-count-badge bg-slate-900 text-white text-xs px-2 py-0.5 rounded-full">0</span>
          </h2>
          <button id="cart-close" class="text-slate-900 hover:text-slate-600 transition-colors cursor-pointer">
            <span class="material-symbols-outlined">close</span>
          </button>
        </div>
        
        <!-- Shipping Progress Bar -->
        <div class="w-full">
          <div class="flex justify-between text-xs font-semibold text-slate-700 mb-2">
            <span id="shipping-message">You are $75 away from free shipping!</span>
            <span class="material-symbols-outlined text-sm text-emerald-500 hidden" id="shipping-success-icon">local_shipping</span>
          </div>
          <div class="w-full bg-slate-200 h-2 rounded-full overflow-hidden">
            <div id="shipping-progress-bar" class="bg-emerald-500 h-full transition-all duration-500" style="width: 0%"></div>
          </div>
        </div>
      </div>

      <div id="cart-items-container" class="flex-1 overflow-y-auto p-6 space-y-6">
        <!-- Cart Items Injected Here -->
      </div>

      <div class="p-6 bg-slate-50 border-t border-slate-200/80 space-y-4">
        <!-- Promo Code -->
        <div class="flex gap-2">
          <input type="text" id="promo-code-input" placeholder="Promo Code (e.g., FLOW10)" class="w-full bg-white border border-slate-200 rounded-lg px-3 py-2 text-sm outline-none focus:border-slate-900" />
          <button id="apply-promo-btn" class="bg-slate-200 text-slate-900 px-4 py-2 rounded-lg text-xs font-bold uppercase hover:bg-slate-300 transition-colors cursor-pointer">Apply</button>
        </div>

        <div class="space-y-2 text-sm">
          <div class="flex justify-between text-slate-500">
            <span>Subtotal</span>
            <span id="cart-subtotal-raw">$0.00</span>
          </div>
          <div id="discount-row" class="flex justify-between text-emerald-600 hidden">
            <span>Discount</span>
            <span id="cart-discount">-$0.00</span>
          </div>
          <div class="flex justify-between text-slate-500">
            <span>Shipping</span>
            <span id="cart-shipping">Calculated at checkout</span>
          </div>
          <div class="flex justify-between items-center pt-2 border-t border-slate-200">
            <span class="font-bold text-slate-900 uppercase tracking-wider">Total</span>
            <span id="cart-subtotal" class="font-headline-md text-2xl font-bold text-slate-900">$0.00</span>
          </div>
        </div>
        
        <button id="checkout-btn" class="w-full bg-slate-900 text-white font-semibold text-sm py-4 rounded-xl uppercase tracking-widest hover:bg-slate-800 transition-colors cursor-pointer shadow-lg shadow-slate-900/20">
          Checkout Now &rarr;
        </button>
      </div>"""

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    content = content.replace(old_cart, new_cart)
    with open(f, 'w') as file:
        file.write(content)

