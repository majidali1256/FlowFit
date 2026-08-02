import re

with open('old_main.js', 'r') as f:
    old_content = f.read()

# We need everything from initAddProductFormSubmit down to the end of updateCartBadge, and showCartToast.
# Wait, let's just find the start of initAddProductFormSubmit and the end of updateCartBadge.
start_idx = old_content.find('function initAddProductFormSubmit() {')
end_idx = old_content.find('function renderCartDrawer() {')

if start_idx != -1 and end_idx != -1:
    funcs = old_content[start_idx:end_idx].strip()
    with open('assets/js/main.js', 'a') as f:
        f.write('\n\n/* ==========================================================================\n   RESTORED FUNCTIONS\n   ========================================================================== */\n')
        f.write(funcs)
        f.write('\n')
