import os

files = ['index.html', 'collections.html', 'product.html', 'new-arrivals.html']

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    # Update HTML links
    content = content.replace('lookbook.html', 'new-arrivals.html')
    content = content.replace('Outfit Lookbook', 'New Arrivals')
    content = content.replace('>Lookbook<', '>New Arrivals<')
    content = content.replace('Style Guide &amp; Lookbook', 'New Arrivals')
    content = content.replace('Discover seasonal outfit inspirations curated by Flow Wear designers for Men, Women, Boys, and Girls.', 'Shop our newest drops and latest seasonal additions for Men, Women, Boys, and Girls.')
    content = content.replace('<title>Flow Wear — Outfit Lookbook (Men, Women, Kids)</title>', '<title>Flow Wear — New Arrivals</title>')
    
    with open(f, 'w') as file:
        file.write(content)
