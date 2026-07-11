# Flow Wear — Quiet Luxury Spatial Flagship (Shopify & Static Build)

We have codified and unified your Stitch designs into both:
1. **Interactive Static Storefront Pages** (ready to preview locally or deploy immediately to any static host).
2. **Shopify OS 2.0 Production Theme Package (`/shopify_theme/`)** (ready to upload directly to Shopify Admin or deploy via Shopify CLI).

---

## 1. Previewing & Testing Locally (HTML/JS Static Storefront)

All core interactive pages are located in the root directory and use unified assets in `/assets/css/theme.css` and `/assets/js/main.js`:
- `index.html` — **Digital Flagship Home** with WebGL background shader & Three.js 3D spatial hero artifact.
- `collections.html` — **Curated Collections** with category filtering chips & Add to Bag drawers.
- `product.html` — **Aurum & Onda Product Detail Page** with Bento Grid specs & colorway selection.
- `lookbook.html` — **Architectural Movement Editorial Lookbook**.
- `studio.html` — **Interactive 3D Spatial Form Consultation Studio**.

### How to Preview Locally:
You can open `index.html` directly in your browser or run a lightweight local server:
```bash
npx serve .
```
Open `http://localhost:3000` to browse the complete multi-page experience.

---

## 2. Installing to Shopify (Shopify OS 2.0 Theme Package)

The complete Shopify production theme structure is built inside `/shopify_theme/`:
```
shopify_theme/
├── assets/
│   ├── theme.css     # Unified Quiet Luxury Glassmorphism CSS
│   └── theme.js      # Core storefront engine (Ajax Cart, Three.js, WebGL Shader)
├── config/
│   └── settings_schema.json
├── layout/
│   └── theme.liquid  # Master Shopify OS 2.0 layout wrapper
├── sections/
│   ├── header.liquid
│   ├── footer.liquid
│   ├── hero-digital-flagship.liquid
│   ├── spatial-artifacts-featured.liquid
│   ├── main-collection-grid.liquid
│   ├── main-product.liquid
│   ├── lookbook-editorial.liquid
│   └── interactive-3d-experience.liquid
└── templates/
    ├── index.json
    ├── collection.json
    ├── product.json
    ├── page.lookbook.json
    └── page.studio.json
```

### Option A: Upload via Shopify Admin (ZIP Upload)
1. Zip the contents of the `shopify_theme/` folder:
   ```bash
   cd shopify_theme && zip -r ../flow-wear-shopify-theme.zip .
   ```
2. Go to your **Shopify Admin** → **Online Store** → **Themes**.
3. Click **Add theme** → **Upload zip file** and select `flow-wear-shopify-theme.zip`.
4. Click **Customize** to arrange sections using the Shopify OS 2.0 Theme Editor.

### Option B: Deploy via Shopify CLI
1. Make sure you have the Shopify CLI installed (`npm install -g @shopify/cli`).
2. Run theme push from the `shopify_theme/` folder:
   ```bash
   shopify theme push --path shopify_theme
   ```
3. Follow the CLI prompt to select your Shopify store and publish or preview your theme!

---

## Key Features Included
- **Persistent Slide-Out Shopping Bag Drawer**: Uses Shopify OS 2.0 Ajax Cart (`/cart/add.js` and `/cart.js`) with instant toast notification feedback.
- **Global WebGL Flow Shader**: Adaptive soft pink / deep blue liquid flow shader running smoothly in the background.
- **Three.js Spatial 3D Artifact Viewer**: Touch & drag interactive 3D icosahedron spatial weave rendering with custom specular lighting.
- **Quiet Luxury Glassmorphism System**: Harmonious HSL colors, responsive container queries, and Material Symbols icons.
