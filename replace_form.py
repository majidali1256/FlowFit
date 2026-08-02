import os

files = ['collections.html', 'product.html', 'lookbook.html']

old_form = """        <form class="space-y-4" onsubmit="event.preventDefault(); alert('Signed in successfully!');">
          <div>
            <label class="text-xs font-semibold text-slate-900 block mb-1">Email Address</label>
            <input type="email" placeholder="client@flowwear.com" required class="w-full px-4 py-3 rounded-lg bg-slate-50 border border-slate-200 text-sm outline-none focus:border-slate-900" />
          </div>
          <div>
            <label class="text-xs font-semibold text-slate-900 block mb-1">Password</label>
            <input type="password" placeholder="••••••••" required class="w-full px-4 py-3 rounded-lg bg-slate-50 border border-slate-200 text-sm outline-none focus:border-slate-900" />
          </div>
          <button type="submit" class="w-full bg-slate-900 text-white font-semibold text-xs py-4 rounded-lg uppercase tracking-widest btn-hover-lift cursor-pointer">
            Sign In To Account
          </button>
        </form>"""

new_form = """        <form id="account-login-form" class="space-y-4">
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
        </form>
        <div id="admin-logged-in-view" style="display: none;" class="text-center space-y-4">
          <span class="material-symbols-outlined text-4xl text-emerald-500">verified_user</span>
          <h3 class="font-headline-md text-xl font-bold text-slate-900">Owner Logged In</h3>
          <p class="text-sm text-slate-500">You have access to add products.</p>
          <button id="admin-logout-btn" class="w-full bg-rose-600 text-white font-semibold text-xs py-4 rounded-lg uppercase tracking-widest btn-hover-lift cursor-pointer">
            Log Out
          </button>
        </div>"""

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    content = content.replace(old_form, new_form)
    with open(f, 'w') as file:
        file.write(content)

