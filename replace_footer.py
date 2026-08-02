import os

files = ['index.html', 'collections.html', 'product.html', 'new-arrivals.html']

old_footer = """  <footer class="w-full py-12 bg-white border-t border-slate-200/80">
    <div class="max-w-[1280px] mx-auto px-6 md:px-16 flex flex-col md:flex-row justify-between items-center gap-6">
      <div class="font-headline-md text-2xl font-bold text-slate-900">Flow Wear</div>
      <div class="flex flex-wrap justify-center gap-8">
        <a href="index.html" class="text-xs font-semibold uppercase tracking-wider text-slate-600 hover:text-slate-900 transition-colors">Home</a>
        <a href="collections.html" class="text-xs font-semibold uppercase tracking-wider text-slate-600 hover:text-slate-900 transition-colors">Collections</a>
        <a href="new-arrivals.html" class="text-xs font-semibold uppercase tracking-wider text-slate-600 hover:text-slate-900 transition-colors">New Arrivals</a>
      </div>
      <div class="text-xs text-slate-500">© 2026 Flow Wear Clothing. All rights reserved.</div>
    </div>
  </footer>"""

new_footer = """  <footer class="w-full py-16 bg-white border-t border-slate-200/80 mt-auto">
    <div class="max-w-[1280px] mx-auto px-6 md:px-16 grid grid-cols-1 md:grid-cols-4 gap-12 mb-12">
      <!-- Brand & Newsletter -->
      <div class="md:col-span-1">
        <div class="font-headline-md text-3xl font-bold text-slate-900 mb-4">Flow Wear</div>
        <p class="text-sm text-slate-500 mb-6">Redefining modern essentials for everyone. Premium quality, sustainable materials.</p>
        <form class="flex flex-col gap-2" onsubmit="event.preventDefault(); alert('Subscribed to newsletter!');">
          <label class="text-xs font-bold text-slate-900 uppercase tracking-wider">Join The Club</label>
          <div class="flex">
            <input type="email" placeholder="Email Address" required class="w-full px-4 py-2 bg-slate-50 border border-slate-200 rounded-l-lg outline-none text-sm focus:border-slate-900" />
            <button type="submit" class="bg-slate-900 text-white px-4 py-2 rounded-r-lg text-sm font-semibold hover:bg-slate-800 transition-colors">&rarr;</button>
          </div>
        </form>
      </div>

      <!-- Shop Links -->
      <div>
        <h4 class="text-xs font-bold text-slate-900 uppercase tracking-wider mb-4">Shop</h4>
        <ul class="space-y-3">
          <li><a href="new-arrivals.html" class="text-sm text-slate-500 hover:text-slate-900 transition-colors">New Arrivals</a></li>
          <li><a href="collections.html" class="text-sm text-slate-500 hover:text-slate-900 transition-colors">All Clothing</a></li>
          <li><a href="collections.html" class="text-sm text-slate-500 hover:text-slate-900 transition-colors">Best Sellers</a></li>
          <li><a href="collections.html" class="text-sm text-slate-500 hover:text-slate-900 transition-colors">Sale</a></li>
        </ul>
      </div>

      <!-- Customer Care -->
      <div>
        <h4 class="text-xs font-bold text-slate-900 uppercase tracking-wider mb-4">Customer Care</h4>
        <ul class="space-y-3">
          <li><a href="#" class="text-sm text-slate-500 hover:text-slate-900 transition-colors">Contact Us</a></li>
          <li><a href="#" class="text-sm text-slate-500 hover:text-slate-900 transition-colors">FAQs</a></li>
          <li><a href="#" class="text-sm text-slate-500 hover:text-slate-900 transition-colors">Shipping &amp; Delivery</a></li>
          <li><a href="#" class="text-sm text-slate-500 hover:text-slate-900 transition-colors">Returns &amp; Exchanges</a></li>
          <li><a href="#" class="text-sm text-slate-500 hover:text-slate-900 transition-colors">Size Guide</a></li>
        </ul>
      </div>

      <!-- Legal & Socials -->
      <div>
        <h4 class="text-xs font-bold text-slate-900 uppercase tracking-wider mb-4">Legal</h4>
        <ul class="space-y-3 mb-6">
          <li><a href="#" class="text-sm text-slate-500 hover:text-slate-900 transition-colors">Privacy Policy</a></li>
          <li><a href="#" class="text-sm text-slate-500 hover:text-slate-900 transition-colors">Terms of Service</a></li>
        </ul>
        <h4 class="text-xs font-bold text-slate-900 uppercase tracking-wider mb-4">Follow Us</h4>
        <div class="flex gap-4">
          <a href="#" class="text-slate-400 hover:text-slate-900 transition-colors" title="Instagram"><span class="material-symbols-outlined">photo_camera</span></a>
          <a href="#" class="text-slate-400 hover:text-slate-900 transition-colors" title="Twitter"><span class="material-symbols-outlined">chat_bubble</span></a>
          <a href="#" class="text-slate-400 hover:text-slate-900 transition-colors" title="Facebook"><span class="material-symbols-outlined">public</span></a>
        </div>
      </div>
    </div>
    
    <div class="max-w-[1280px] mx-auto px-6 md:px-16 pt-8 border-t border-slate-100 flex flex-col md:flex-row justify-between items-center gap-4">
      <div class="text-xs text-slate-500">&copy; 2026 Flow Wear Clothing. All rights reserved.</div>
      <div class="flex gap-2">
        <span class="material-symbols-outlined text-slate-300" title="Credit Card">credit_card</span>
        <span class="material-symbols-outlined text-slate-300" title="PayPal">account_balance_wallet</span>
        <span class="material-symbols-outlined text-slate-300" title="Apple Pay">phone_iphone</span>
      </div>
    </div>
  </footer>"""

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    content = content.replace(old_footer, new_footer)
    with open(f, 'w') as file:
        file.write(content)

