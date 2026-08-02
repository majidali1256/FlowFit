import os

with open('product.html', 'r') as f:
    content = f.read()

start_tag = '<main class="w-full max-w-[1280px] mx-auto px-6 md:px-16 pt-32 pb-20 min-h-screen grid grid-cols-1 lg:grid-cols-12 gap-12">'
end_tag = '</main>'

start_idx = content.find(start_tag)
end_idx = content.find(end_tag) + len(end_tag)

new_main = """<main class="w-full max-w-[1280px] mx-auto px-6 md:px-16 pt-32 pb-20 min-h-screen">
    <!-- Breadcrumb -->
    <nav class="flex items-center gap-2 text-slate-500 text-xs font-semibold uppercase tracking-widest mb-8">
      <a href="collections.html" class="hover:text-slate-900 transition-colors">Shirts & Tops</a>
      <span class="material-symbols-outlined text-sm">chevron_right</span>
      <span class="text-slate-900">Heavyweight Oversized Tee</span>
    </nav>

    <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 mb-20">
      <!-- Image Gallery -->
      <div class="lg:col-span-7 flex flex-col gap-4">
        <div class="w-full aspect-[4/3] md:aspect-[1/1] bg-slate-50 rounded-3xl overflow-hidden relative shadow-sm border border-slate-200 p-8 flex items-center justify-center">
          <img id="main-product-image" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAJXctBq6dGKXdU_xb_MyTNETARrPJQH2oh_wRRJP3DTeNr3wxHOTplkB1eje3uue0zd1tG9jjggeefz6BDRs0kOQR2kdYsIg93SgBRor6738jygyI0VtcDiI6LdrJPRw6mBkuPvA91wLrUazCZCvevN0N3pGXZJLBpdiRyqcg4NbqqiH68b6379JrLZcMjFbc050L2nPRPm2KMnzJNKCqxfrSR_oBAdkp7a3vbFYYGmPJzHWf9CoL3Xw" alt="Heavyweight Tee" class="max-h-full w-auto object-contain mix-blend-multiply transition-transform duration-300" />
          <div class="absolute top-6 left-6 bg-slate-900 text-white text-xs font-semibold px-4 py-1.5 rounded-full uppercase tracking-widest shadow-sm">
            Best Seller
          </div>
        </div>
        <!-- Thumbnails -->
        <div class="grid grid-cols-4 gap-4">
          <button class="aspect-square bg-slate-50 rounded-xl border-2 border-slate-900 overflow-hidden p-2 flex items-center justify-center cursor-pointer">
            <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuAJXctBq6dGKXdU_xb_MyTNETARrPJQH2oh_wRRJP3DTeNr3wxHOTplkB1eje3uue0zd1tG9jjggeefz6BDRs0kOQR2kdYsIg93SgBRor6738jygyI0VtcDiI6LdrJPRw6mBkuPvA91wLrUazCZCvevN0N3pGXZJLBpdiRyqcg4NbqqiH68b6379JrLZcMjFbc050L2nPRPm2KMnzJNKCqxfrSR_oBAdkp7a3vbFYYGmPJzHWf9CoL3Xw" class="w-full h-full object-contain mix-blend-multiply" />
          </button>
          <button class="aspect-square bg-slate-50 rounded-xl border border-slate-200 hover:border-slate-400 overflow-hidden p-2 flex items-center justify-center cursor-pointer">
            <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuDQoM_YgZc12CtdoUuV-QcR2b1O8aA9mI-jMIf1rOXZr6l12b1R7jQ9rOqM5I-z-kF9jC_R5eNlD4T4QvN9x1M_l9v1Lq3f7A1X0h_2gC1L9oE" class="w-full h-full object-contain mix-blend-multiply" />
          </button>
          <button class="aspect-square bg-slate-50 rounded-xl border border-slate-200 hover:border-slate-400 overflow-hidden p-2 flex items-center justify-center cursor-pointer">
            <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuB3M8uV9d0Z6bM-vR1X9r8vN3bO9V1Z8m0u9nC1I-u8qM3f9zX9kX7cZ2tB3nK3c0aO-V9I6mI8m2jU6C8M1lV1yM8aL3f9jC0q8" class="w-full h-full object-contain mix-blend-multiply" />
          </button>
          <button class="aspect-square bg-slate-50 rounded-xl border border-slate-200 hover:border-slate-400 overflow-hidden p-2 flex items-center justify-center cursor-pointer">
            <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuAJXctBq6dGKXdU_xb_MyTNETARrPJQH2oh_wRRJP3DTeNr3wxHOTplkB1eje3uue0zd1tG9jjggeefz6BDRs0kOQR2kdYsIg93SgBRor6738jygyI0VtcDiI6LdrJPRw6mBkuPvA91wLrUazCZCvevN0N3pGXZJLBpdiRyqcg4NbqqiH68b6379JrLZcMjFbc050L2nPRPm2KMnzJNKCqxfrSR_oBAdkp7a3vbFYYGmPJzHWf9CoL3Xw" class="w-full h-full object-contain mix-blend-multiply grayscale opacity-50" />
          </button>
        </div>
      </div>

      <!-- Product Info -->
      <div class="lg:col-span-5 flex flex-col justify-between space-y-8">
        <div class="space-y-6">
          <div>
            <div class="flex items-center gap-2 mb-2">
              <span class="text-xs font-semibold uppercase tracking-widest text-slate-500">Shirts & Tops · Unisex</span>
              <div class="flex items-center text-amber-400 text-sm">
                <span class="material-symbols-outlined text-[16px] filled">star</span>
                <span class="material-symbols-outlined text-[16px] filled">star</span>
                <span class="material-symbols-outlined text-[16px] filled">star</span>
                <span class="material-symbols-outlined text-[16px] filled">star</span>
                <span class="material-symbols-outlined text-[16px] filled">star_half</span>
                <a href="#reviews" class="text-xs text-slate-500 ml-1 hover:underline cursor-pointer">(128 Reviews)</a>
              </div>
            </div>
            <h1 class="font-headline-md text-4xl md:text-5xl font-bold text-slate-900 leading-tight">Heavyweight Oversized Tee</h1>
            <p class="text-3xl font-bold text-slate-900 mt-3">$65.00</p>
          </div>

          <p class="text-sm text-slate-600 leading-relaxed">
            Cut from 300 GSM combed organic cotton with a soft vintage wash finish. Features a drop-shoulder drape and durable rib-knit collar designed for effortless daily wear.
          </p>

          <div class="space-y-3">
            <div class="flex justify-between items-center">
              <label class="text-xs font-bold uppercase tracking-wider text-slate-900 block">Select Size</label>
              <button onclick="alert('Size Guide: XS (Chest 34\"), S (36\"), M (38-40\"), L (42-44\"), XL (46\"), XXL (48\")')" class="text-xs font-semibold text-slate-500 hover:underline cursor-pointer flex items-center gap-1">
                <span class="material-symbols-outlined text-[14px]">straighten</span> Size Guide
              </button>
            </div>
            <div class="flex flex-wrap gap-2 size-selector-group">
              <button class="size-pill w-12 h-12 rounded-xl border border-slate-200 text-sm font-semibold text-slate-900 hover:border-slate-900 text-center flex items-center justify-center transition-colors">XS</button>
              <button class="size-pill w-12 h-12 rounded-xl border border-slate-200 text-sm font-semibold text-slate-900 hover:border-slate-900 text-center flex items-center justify-center transition-colors">S</button>
              <button class="size-pill active w-12 h-12 rounded-xl bg-slate-900 text-white border border-slate-900 text-sm font-semibold text-center flex items-center justify-center transition-colors shadow-md">M</button>
              <button class="size-pill w-12 h-12 rounded-xl border border-slate-200 text-sm font-semibold text-slate-900 hover:border-slate-900 text-center flex items-center justify-center transition-colors">L</button>
              <button class="size-pill w-12 h-12 rounded-xl border border-slate-200 text-sm font-semibold text-slate-900 hover:border-slate-900 text-center flex items-center justify-center transition-colors">XL</button>
              <button class="size-pill w-12 h-12 rounded-xl border border-slate-200 text-sm font-semibold text-slate-300 hover:border-slate-300 text-center flex items-center justify-center transition-colors cursor-not-allowed line-through relative" title="Out of Stock">
                XXL
              </button>
            </div>
          </div>

          <div class="space-y-3">
            <label class="text-xs font-bold uppercase tracking-wider text-slate-900 block">Color: <span class="font-normal text-slate-600">Washed Black</span></label>
            <div class="flex gap-3">
              <button class="w-10 h-10 rounded-full border-2 border-slate-900 bg-[#2d2d2d] cursor-pointer shadow-sm relative" title="Washed Black"></button>
              <button class="w-10 h-10 rounded-full border-2 border-transparent hover:border-slate-400 bg-[#dccbb7] cursor-pointer shadow-sm transition-colors" title="Sand Beige"></button>
              <button class="w-10 h-10 rounded-full border-2 border-transparent hover:border-slate-400 bg-[#9ca3af] cursor-pointer shadow-sm transition-colors" title="Heather Grey"></button>
              <button class="w-10 h-10 rounded-full border-2 border-transparent hover:border-slate-400 bg-[#244535] cursor-pointer shadow-sm transition-colors" title="Forest Green"></button>
            </div>
          </div>

          <div class="grid grid-cols-2 gap-4 pt-4">
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
          </div>
        </div>

        <div class="space-y-3 pt-6 border-t border-slate-200">
          <div class="flex items-center gap-4 mb-4">
            <div class="flex border border-slate-200 rounded-xl bg-white overflow-hidden w-32 h-14">
              <button class="flex-1 flex items-center justify-center text-slate-500 hover:bg-slate-50">-</button>
              <div class="flex-1 flex items-center justify-center font-bold text-slate-900 border-x border-slate-200">1</div>
              <button class="flex-1 flex items-center justify-center text-slate-500 hover:bg-slate-50">+</button>
            </div>
            <button class="add-to-bag-btn flex-1 bg-slate-900 hover:bg-slate-800 text-white font-semibold text-sm h-14 rounded-xl uppercase tracking-widest btn-hover-lift shadow-lg flex items-center justify-center gap-2 cursor-pointer transition-all"
              data-id="oversized-tee-01"
              data-name="Heavyweight Oversized Tee"
              data-price="65"
              data-size="M"
              data-image="https://lh3.googleusercontent.com/aida-public/AB6AXuAJXctBq6dGKXdU_xb_MyTNETARrPJQH2oh_wRRJP3DTeNr3wxHOTplkB1eje3uue0zd1tG9jjggeefz6BDRs0kOQR2kdYsIg93SgBRor6738jygyI0VtcDiI6LdrJPRw6mBkuPvA91wLrUazCZCvevN0N3pGXZJLBpdiRyqcg4NbqqiH68b6379JrLZcMjFbc050L2nPRPm2KMnzJNKCqxfrSR_oBAdkp7a3vbFYYGmPJzHWf9CoL3Xw"
              data-color="Washed Black">
              Add to Bag
            </button>
          </div>
          <button class="w-full bg-[#5a31f4] hover:bg-[#4a21e4] text-white font-semibold text-sm h-14 rounded-xl uppercase tracking-widest btn-hover-lift shadow-md flex items-center justify-center gap-2 cursor-pointer transition-all">
            Buy with Shop Pay
          </button>
        </div>
      </div>
    </div>

    <!-- Customer Reviews -->
    <div id="reviews" class="mt-24 pt-20 border-t border-slate-200">
      <h2 class="font-headline-md text-3xl font-bold text-slate-900 mb-10 text-center">Customer Reviews</h2>
      
      <div class="grid grid-cols-1 md:grid-cols-3 gap-12 mb-12">
        <div class="text-center md:text-left flex flex-col md:items-start items-center">
          <p class="text-6xl font-bold text-slate-900 mb-2">4.8</p>
          <div class="flex text-amber-400 text-xl mb-2">
            <span class="material-symbols-outlined filled">star</span>
            <span class="material-symbols-outlined filled">star</span>
            <span class="material-symbols-outlined filled">star</span>
            <span class="material-symbols-outlined filled">star</span>
            <span class="material-symbols-outlined filled">star_half</span>
          </div>
          <p class="text-sm text-slate-500">Based on 128 reviews</p>
          <button class="mt-6 border border-slate-900 text-slate-900 font-semibold text-xs px-6 py-3 rounded-lg uppercase tracking-wider hover:bg-slate-900 hover:text-white transition-colors cursor-pointer">
            Write a Review
          </button>
        </div>
        
        <div class="md:col-span-2 space-y-8">
          <div class="border-b border-slate-100 pb-8">
            <div class="flex justify-between items-start mb-2">
              <div class="flex gap-2 items-center">
                <div class="flex text-amber-400 text-sm">
                  <span class="material-symbols-outlined filled">star</span>
                  <span class="material-symbols-outlined filled">star</span>
                  <span class="material-symbols-outlined filled">star</span>
                  <span class="material-symbols-outlined filled">star</span>
                  <span class="material-symbols-outlined filled">star</span>
                </div>
                <span class="font-bold text-slate-900 text-sm">Michael S.</span>
                <span class="text-emerald-500 text-[10px] uppercase font-bold flex items-center"><span class="material-symbols-outlined text-[12px] mr-1">verified</span>Verified Buyer</span>
              </div>
              <span class="text-xs text-slate-400">2 days ago</span>
            </div>
            <h4 class="font-bold text-slate-900 mb-1">Perfect Fit & Quality</h4>
            <p class="text-sm text-slate-600">The quality of the cotton is amazing. It's thick, heavy, but very breathable. The oversized fit is exactly what I was looking for, not just a regular shirt sized up.</p>
          </div>
          
          <div class="border-b border-slate-100 pb-8">
            <div class="flex justify-between items-start mb-2">
              <div class="flex gap-2 items-center">
                <div class="flex text-amber-400 text-sm">
                  <span class="material-symbols-outlined filled">star</span>
                  <span class="material-symbols-outlined filled">star</span>
                  <span class="material-symbols-outlined filled">star</span>
                  <span class="material-symbols-outlined filled">star</span>
                  <span class="material-symbols-outlined text-slate-300">star</span>
                </div>
                <span class="font-bold text-slate-900 text-sm">David L.</span>
                <span class="text-emerald-500 text-[10px] uppercase font-bold flex items-center"><span class="material-symbols-outlined text-[12px] mr-1">verified</span>Verified Buyer</span>
              </div>
              <span class="text-xs text-slate-400">1 week ago</span>
            </div>
            <h4 class="font-bold text-slate-900 mb-1">Great but order true to size</h4>
            <p class="text-sm text-slate-600">I sized up thinking I wanted it extra baggy, but it's already designed to be oversized. The material feels premium. Definitely buying another color.</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Related Products -->
    <div class="mt-24 pt-20 border-t border-slate-200">
      <div class="flex justify-between items-end mb-10">
        <h2 class="font-headline-md text-3xl font-bold text-slate-900">You May Also Like</h2>
        <a href="collections.html" class="text-sm font-semibold text-slate-900 hover:text-slate-600 underline">View Collection</a>
      </div>
      
      <div id="featured-products-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <!-- Rendered via JS -->
      </div>
    </div>
  </main>"""

new_content = content[:start_idx] + new_main + content[end_idx:]

with open('product.html', 'w') as f:
    f.write(new_content)

