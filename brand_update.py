import os

files = ['index.html', 'collections.html', 'product.html', 'new-arrivals.html']

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    # 1. Header Logo
    old_logo = '<a href="index.html" class="font-headline-md text-2xl md:text-3xl font-bold tracking-tight text-slate-900">Flow Wear</a>'
    new_logo = '<a href="index.html" class="font-headline-md text-2xl md:text-3xl font-black italic tracking-tighter text-[#1A1A1A]">FLOWEAR</a>'
    content = content.replace(old_logo, new_logo)

    # 2. Announcement Bar
    old_ann = '<div class="bg-slate-900 text-white text-[10px] sm:text-xs font-semibold uppercase tracking-widest text-center py-2 px-4 shadow-md flex justify-center gap-2 items-center">'
    new_ann = '<div class="bg-[#1A1A1A] text-white text-[10px] sm:text-xs font-semibold uppercase tracking-widest text-center py-2 px-4 shadow-md flex justify-center gap-2 items-center">'
    content = content.replace(old_ann, new_ann)
    
    # 3. Footer
    old_footer = '<footer class="bg-slate-900 text-slate-50 pt-16 pb-8">'
    new_footer = '<footer class="bg-[#1A1A1A] text-[#F2F2F2] pt-16 pb-8 border-t-[6px] border-[#DDB24A]">'
    content = content.replace(old_footer, new_footer)
    
    # Footer Logo
    old_flogo = '<span class="font-headline-md text-2xl font-bold tracking-tight">Flow Wear</span>'
    new_flogo = '<span class="font-headline-md text-2xl font-black italic tracking-tighter">FLOWEAR</span><br><span class="text-xs uppercase tracking-widest text-[#DDB24A] font-semibold mt-1 block">Flow With Style</span>'
    content = content.replace(old_flogo, new_flogo)

    # 4. Primary Buttons (Shop Now, Explore, Checkout, etc.)
    # We will look for bg-slate-900 text-white on buttons and replace with bg-[#DDB24A] text-[#1A1A1A] hover:bg-[#c9a03f]
    content = content.replace('bg-slate-900 text-white', 'bg-[#DDB24A] text-[#1A1A1A] hover:bg-[#c49a37]')
    
    # Text mentions
    content = content.replace('Flow Wear', 'FLOWEAR')

    with open(f, 'w') as file:
        file.write(content)

