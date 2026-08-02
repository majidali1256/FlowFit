import os

files = ['index.html', 'collections.html', 'product.html', 'new-arrivals.html']

quick_view_html = """
  <!-- Quick View Modal -->
  <div id="quick-view-modal" class="modal-overlay items-center justify-center p-4">
    <div id="qv-backdrop" class="absolute inset-0 bg-slate-900/40 backdrop-blur-sm cursor-pointer"></div>
    <div class="glass-panel w-full max-w-4xl max-h-[90vh] overflow-y-auto rounded-3xl shadow-2xl relative flex flex-col md:flex-row bg-white z-10">
      <button id="qv-close" class="absolute top-4 right-4 text-slate-400 hover:text-slate-900 transition-colors z-20 cursor-pointer">
        <span class="material-symbols-outlined bg-white rounded-full shadow p-1">close</span>
      </button>
      
      <div class="w-full md:w-1/2 bg-slate-50 flex items-center justify-center p-8">
        <img id="qv-image" src="" class="max-h-[400px] object-contain mix-blend-multiply" />
      </div>
      
      <div class="w-full md:w-1/2 p-8 flex flex-col justify-center">
        <h2 id="qv-title" class="font-headline-md text-3xl font-bold text-slate-900 mb-2"></h2>
        <p id="qv-price" class="text-xl font-bold text-slate-700 mb-6"></p>
        
        <div class="space-y-4 mb-8">
          <div>
            <span class="text-xs font-bold text-slate-900 uppercase tracking-wider block mb-2">Size</span>
            <div class="flex gap-2">
              <button class="w-10 h-10 rounded border border-slate-200 text-sm font-semibold hover:border-slate-900">S</button>
              <button class="w-10 h-10 rounded border border-slate-900 bg-slate-900 text-white text-sm font-semibold">M</button>
              <button class="w-10 h-10 rounded border border-slate-200 text-sm font-semibold hover:border-slate-900">L</button>
              <button class="w-10 h-10 rounded border border-slate-200 text-sm font-semibold hover:border-slate-900">XL</button>
            </div>
          </div>
        </div>
        
        <button id="qv-add-to-cart" class="w-full bg-slate-900 text-white font-semibold py-4 rounded-xl hover:bg-slate-800 transition-colors cursor-pointer shadow-lg shadow-slate-900/20 uppercase tracking-widest text-sm mb-3">
          Add To Cart
        </button>
        <a href="product.html" class="text-center text-sm font-semibold text-slate-500 hover:text-slate-900 underline">View Full Details</a>
      </div>
    </div>
  </div>
"""

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    # Insert right before <script src="assets/js/main.js
    content = content.replace('<script src="assets/js/main.js', quick_view_html + '\n  <script src="assets/js/main.js')
    
    with open(f, 'w') as file:
        file.write(content)

