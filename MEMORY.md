# Memory - Flow Fit (Flow Wear Clothing Store)

## Project Overview
- **Brand**: Flow Wear (Clothing Brand for Everyone — Men, Women, Boys, Girls).
- **Products**: Shirts & Tops, Pants & Trousers, Jackets & Outerwear, Caps & Accessories, Kids Clothing.
- **Tech Stack**: HTML5, Vanilla JavaScript (ES6+), Vanilla CSS + Design Tokens in [assets/css/theme.css](file:///Users/macbookair/VS%20CODE%20PROJECTS/FlowFit/assets/css/theme.css), Tailwind CSS CDN.
- **Local Dev Server**: `http://localhost:8085`

## Key Architecture & Features
1. **Live "+ Add Product" Manager**:
   - Interactive Modal Form available across all pages.
   - Saves new apparel products directly to browser `localStorage` (`flow_wear_custom_products`).
   - Dynamic catalog renderer automatically updates Homepage & Collections grids without page refreshes.
   - Persistent LocalStorage Cart (`flow_wear_clothing_cart`).

2. **Clean UI & Modal Engine**:
   - Soft, light slate borders (`border-slate-200`) eliminate any harsh black lines.
   - All modals (`#add-product-modal`, `#cart-drawer`, `#search-overlay`, `#account-drawer`, `#side-drawer`, `#checkout-modal`) use explicit `hidden` class state management to guarantee 100% clickability on all underlying page elements when closed.
   - WebGL Ambient Background Shader produces a soft pearl-white liquid mesh glow.

3. **Sitemap**:
   - [index.html](file:///Users/macbookair/VS%20CODE%20PROJECTS/FlowFit/index.html) — Apparel Homepage, Category Showcase, Featured Products Grid.
   - [collections.html](file:///Users/macbookair/VS%20CODE%20PROJECTS/FlowFit/collections.html) — Apparel Catalog with Category Filter Chips.
   - [product.html](file:///Users/macbookair/VS%20CODE%20PROJECTS/FlowFit/product.html) — Apparel Detail Page with Size Selection.
   - [lookbook.html](file:///Users/macbookair/VS%20CODE%20PROJECTS/FlowFit/lookbook.html) — Seasonal Outfit Lookbook.
