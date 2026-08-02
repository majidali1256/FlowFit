import os

files = ['index.html', 'collections.html', 'product.html', 'lookbook.html']

old_form = """        <form id="account-login-form" class="space-y-4">
          <div>
            <label class="text-xs font-semibold text-slate-900 block mb-1">Email Address</label>
            <input id="login-email" type="email" placeholder="client@flowwear.com" required class="w-full px-4 py-3 rounded-lg bg-slate-50 border border-slate-200 text-sm outline-none focus:border-slate-900" />
          </div>
          <div>
            <label class="text-xs font-semibold text-slate-900 block mb-1">Password</label>
            <input id="login-password" type="password" placeholder="••••••••" required class="w-full px-4 py-3 rounded-lg bg-slate-50 border border-slate-200 text-sm outline-none focus:border-slate-900" />
          </div>
          <button type="submit" class="w-full bg-slate-900 text-white font-semibold text-xs py-4 rounded-lg uppercase tracking-widest btn-hover-lift cursor-pointer">
            Sign In To Account
          </button>
        </form>"""

new_form = """        <form id="account-login-form" class="space-y-4">
          <p class="text-xs text-slate-500 pb-2">Prototype Mode: Instantly unlock product management controls.</p>
          <button type="submit" class="w-full bg-slate-900 text-white font-semibold text-xs py-4 rounded-lg uppercase tracking-widest btn-hover-lift cursor-pointer flex items-center justify-center gap-2">
            <span class="material-symbols-outlined text-sm">lock_open</span> Enable Owner Mode
          </button>
        </form>"""

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    content = content.replace(old_form, new_form)
    with open(f, 'w') as file:
        file.write(content)

