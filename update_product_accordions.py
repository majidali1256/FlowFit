import os

with open('product.html', 'r') as f:
    content = f.read()

old_blocks = """          <div class="grid grid-cols-2 gap-4 pt-4">
            <div class="bg-slate-50 p-4 rounded-2xl border border-slate-100 flex flex-col gap-1">
              <span class="material-symbols-outlined text-slate-700 text-xl">eco</span>
              <span class="text-xs font-semibold text-slate-900 uppercase tracking-wider mt-1">Fabric</span>
              <span class="text-sm text-slate-500">300 GSM Organic Cotton</span>
            </div>
            <div class="bg-slate-50 p-4 rounded-2xl border border-slate-100 flex flex-col gap-1">
              <span class="material-symbols-outlined text-slate-700 text-xl">local_shipping</span>
              <span class="text-xs font-semibold text-slate-900 uppercase tracking-wider mt-1">Shipping</span>
              <span class="text-sm text-slate-500">Free over $75.00</span>
            </div>
          </div>"""

new_blocks = """          <!-- Accordions -->
          <div class="border-t border-slate-200 divide-y divide-slate-200 mt-6">
            <details class="group py-4 cursor-pointer" open>
              <summary class="flex justify-between items-center font-bold text-sm text-slate-900 uppercase tracking-wider list-none">
                <span class="flex items-center gap-2"><span class="material-symbols-outlined text-lg">straighten</span> Fit & Details</span>
                <span class="material-symbols-outlined group-open:rotate-180 transition-transform">expand_more</span>
              </summary>
              <div class="text-sm text-slate-600 mt-4 leading-relaxed pl-7">
                <ul class="list-disc pl-4 space-y-1">
                  <li>Oversized drop-shoulder fit</li>
                  <li>300 GSM heavy combed cotton</li>
                  <li>Pre-shrunk and vintage washed</li>
                  <li>Ribbed collar designed to hold shape</li>
                </ul>
              </div>
            </details>
            <details class="group py-4 cursor-pointer">
              <summary class="flex justify-between items-center font-bold text-sm text-slate-900 uppercase tracking-wider list-none">
                <span class="flex items-center gap-2"><span class="material-symbols-outlined text-lg">eco</span> Sustainability</span>
                <span class="material-symbols-outlined group-open:rotate-180 transition-transform">expand_more</span>
              </summary>
              <div class="text-sm text-slate-600 mt-4 leading-relaxed pl-7">
                Crafted entirely from 100% GOTS certified organic cotton, grown without toxic chemicals. Packaged in recycled and biodegradable materials.
              </div>
            </details>
            <details class="group py-4 cursor-pointer">
              <summary class="flex justify-between items-center font-bold text-sm text-slate-900 uppercase tracking-wider list-none">
                <span class="flex items-center gap-2"><span class="material-symbols-outlined text-lg">local_shipping</span> Shipping & Returns</span>
                <span class="material-symbols-outlined group-open:rotate-180 transition-transform">expand_more</span>
              </summary>
              <div class="text-sm text-slate-600 mt-4 leading-relaxed pl-7">
                Free worldwide shipping on orders over $75. Easy 30-day returns for any unworn items. Returns are fully carbon-offset.
              </div>
            </details>
          </div>"""

content = content.replace(old_blocks, new_blocks)

old_buttons = """        <div class="space-y-3 pt-6 border-t border-slate-200">
          <div class="flex items-center gap-4 mb-4">"""

new_buttons = """        <div class="space-y-3 pt-6 border-t border-slate-200">
          <div class="flex items-center gap-4 mb-4">"""

# Trust badges under the Buy with Shop Pay button
old_shop_pay = """          <button class="w-full bg-[#5a31f4] hover:bg-[#4a21e4] text-white font-semibold text-sm h-14 rounded-xl uppercase tracking-widest btn-hover-lift shadow-md flex items-center justify-center gap-2 cursor-pointer transition-all">
            Buy with Shop Pay
          </button>
        </div>"""

new_shop_pay = """          <button class="w-full bg-[#5a31f4] hover:bg-[#4a21e4] text-white font-semibold text-sm h-14 rounded-xl uppercase tracking-widest btn-hover-lift shadow-md flex items-center justify-center gap-2 cursor-pointer transition-all">
            Buy with Shop Pay
          </button>
          
          <!-- Trust Badges -->
          <div class="flex justify-center gap-6 pt-4 text-slate-400">
            <div class="flex flex-col items-center gap-1">
              <span class="material-symbols-outlined text-2xl">verified_user</span>
              <span class="text-[9px] uppercase tracking-wider font-bold">Secure</span>
            </div>
            <div class="flex flex-col items-center gap-1">
              <span class="material-symbols-outlined text-2xl">published_with_changes</span>
              <span class="text-[9px] uppercase tracking-wider font-bold">30 Days</span>
            </div>
            <div class="flex flex-col items-center gap-1">
              <span class="material-symbols-outlined text-2xl">volunteer_activism</span>
              <span class="text-[9px] uppercase tracking-wider font-bold">Ethical</span>
            </div>
          </div>
        </div>"""

content = content.replace(old_shop_pay, new_shop_pay)

with open('product.html', 'w') as f:
    f.write(content)

