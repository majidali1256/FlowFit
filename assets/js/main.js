/**
 * FOUR FIT — QUIET LUXURY DIGITAL FLAGSHIP
 * Core Storefront Javascript Engine
 * Integrates WebGL Liquid Shader, High-Fidelity Three.js 3D Architectural Sculptures,
 * Interactive Cart Drawer, & Smooth Scroll Reveal Animations.
 */

document.addEventListener('DOMContentLoaded', () => {
  initScrollReveal();
  initNavigationDrawer();
  initCartSystem();
  initWebGLBackgroundShader();
  initThreeJSSpatialArtifacts();
  initCollectionFilters();
});

/* ==========================================================================
   1. SMOOTH SCROLL REVEAL ANIMATIONS
   ========================================================================== */
function initScrollReveal() {
  const revealElements = document.querySelectorAll('.reveal');
  if (!revealElements.length) return;

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -30px 0px'
  });

  revealElements.forEach(el => revealObserver.observe(el));

  setTimeout(() => {
    revealElements.forEach(el => {
      const rect = el.getBoundingClientRect();
      if (rect.top < window.innerHeight - 30) {
        el.classList.add('active');
      }
    });
  }, 80);
}

/* ==========================================================================
   2. NAVIGATION DRAWER
   ========================================================================== */
function initNavigationDrawer() {
  const drawer = document.getElementById('side-drawer');
  const drawerContent = document.getElementById('drawer-content');
  const openBtns = document.querySelectorAll('#drawer-toggle');
  const closeBtns = document.querySelectorAll('#drawer-close, #drawer-overlay');

  if (!drawer || !drawerContent) return;

  const openDrawer = () => {
    drawer.classList.remove('pointer-events-none', 'opacity-0');
    drawerContent.classList.remove('-translate-x-full');
    document.body.style.overflow = 'hidden';
  };

  const closeDrawer = () => {
    drawer.classList.add('pointer-events-none', 'opacity-0');
    drawerContent.classList.add('-translate-x-full');
    document.body.style.overflow = '';
  };

  openBtns.forEach(btn => btn.addEventListener('click', openDrawer));
  closeBtns.forEach(btn => btn.addEventListener('click', closeDrawer));
}

/* ==========================================================================
   3. PERSISTENT CART & SHOPPING BAG DRAWER
   ========================================================================== */
const STORE_CART_KEY = 'four_fit_cart_items';

function getCartItems() {
  try {
    return JSON.parse(localStorage.getItem(STORE_CART_KEY)) || [
      {
        id: 'aurum-onda-01',
        name: 'The Aurum Wave Bag',
        price: 1250,
        image: 'https://lh3.googleusercontent.com/aida/AP1WRLvKZ5LDIRYOddqxqKBSi5T3dK2VVK8SFnBB6R4rmAsZeXAvfdw5Znd8cEJQpu_Nf8CI23V6qUNkIQGwQ0r5bTfI_6ZhmpxHF4L1kbDpwVKZZ0XXS8JrDAaO6f86ZHojw-p3UvYiIJg2cu8-15YEsf_WJgyGyXqQshPe5ysOpuef_WUuY9uWdgFk6prsI8wXbdhwG1P-1oJU9mC4UPq6-I7sU4bJ5MP78g6yrihWMVzPjt41Jt3sadD21wU',
        quantity: 1,
        colorway: 'Soft Blush & Deep Blue'
      }
    ];
  } catch (e) {
    return [];
  }
}

function saveCartItems(items) {
  localStorage.setItem(STORE_CART_KEY, JSON.stringify(items));
  renderCartDrawer();
  updateCartBadge();
}

function initCartSystem() {
  const cartDrawer = document.getElementById('cart-drawer');
  const cartContent = document.getElementById('cart-drawer-content');
  const openCartBtns = document.querySelectorAll('.cart-toggle-btn');
  const closeCartBtns = document.querySelectorAll('#cart-close, #cart-overlay');

  if (cartDrawer && cartContent) {
    const openCart = () => {
      cartDrawer.classList.remove('pointer-events-none', 'opacity-0');
      cartContent.classList.remove('translate-x-full');
      document.body.style.overflow = 'hidden';
      renderCartDrawer();
    };

    const closeCart = () => {
      cartDrawer.classList.add('pointer-events-none', 'opacity-0');
      cartContent.classList.add('translate-x-full');
      document.body.style.overflow = '';
    };

    openCartBtns.forEach(btn => btn.addEventListener('click', openCart));
    closeCartBtns.forEach(btn => btn.addEventListener('click', closeCart));
  }

  document.querySelectorAll('.add-to-bag-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const id = btn.getAttribute('data-id') || 'aurum-onda-01';
      const name = btn.getAttribute('data-name') || 'Aurum Wave Bag';
      const price = parseFloat(btn.getAttribute('data-price')) || 1250;
      const image = btn.getAttribute('data-image') || 'https://lh3.googleusercontent.com/aida/AP1WRLvKZ5LDIRYOddqxqKBSi5T3dK2VVK8SFnBB6R4rmAsZeXAvfdw5Znd8cEJQpu_Nf8CI23V6qUNkIQGwQ0r5bTfI_6ZhmpxHF4L1kbDpwVKZZ0XXS8JrDAaO6f86ZHojw-p3UvYiIJg2cu8-15YEsf_WJgyGyXqQshPe5ysOpuef_WUuY9uWdgFk6prsI8wXbdhwG1P-1oJU9mC4UPq6-I7sU4bJ5MP78g6yrihWMVzPjt41Jt3sadD21wU';
      const colorway = btn.getAttribute('data-color') || 'Soft Blush & Deep Blue';

      const items = getCartItems();
      const existing = items.find(item => item.id === id);
      if (existing) {
        existing.quantity += 1;
      } else {
        items.push({ id, name, price, image, quantity: 1, colorway });
      }
      saveCartItems(items);
      showCartToast(name);

      if (cartDrawer && cartContent) {
        setTimeout(() => {
          cartDrawer.classList.remove('pointer-events-none', 'opacity-0');
          cartContent.classList.remove('translate-x-full');
        }, 180);
      }
    });
  });

  renderCartDrawer();
  updateCartBadge();
}

function updateCartBadge() {
  const items = getCartItems();
  const totalCount = items.reduce((sum, i) => sum + i.quantity, 0);
  document.querySelectorAll('.cart-count-badge').forEach(badge => {
    badge.textContent = totalCount;
    badge.style.display = totalCount > 0 ? 'inline-flex' : 'none';
  });
}

function renderCartDrawer() {
  const container = document.getElementById('cart-items-container');
  const subtotalEl = document.getElementById('cart-subtotal-price');
  if (!container || !subtotalEl) return;

  const items = getCartItems();
  container.innerHTML = '';

  if (items.length === 0) {
    container.innerHTML = `
      <div class="flex flex-col items-center justify-center py-16 text-center">
        <span class="material-symbols-outlined text-4xl text-outline mb-3">shopping_bag</span>
        <p class="font-headline-md text-lg text-primary mb-1">Your bag is empty</p>
        <p class="font-body-md text-sm text-on-surface-variant">Explore architectural forms tailored for modern luxury.</p>
      </div>
    `;
    subtotalEl.textContent = '$0.00';
    return;
  }

  let subtotal = 0;
  items.forEach(item => {
    subtotal += item.price * item.quantity;
    const itemEl = document.createElement('div');
    itemEl.className = 'flex items-center gap-4 py-4 border-b border-primary/10';
    itemEl.innerHTML = `
      <img src="${item.image}" alt="${item.name}" class="w-16 h-16 object-contain rounded-lg bg-surface-container-low p-1 border border-primary/5" />
      <div class="flex-1 min-w-0">
        <h4 class="font-headline-md text-sm font-semibold text-primary truncate">${item.name}</h4>
        <p class="text-xs text-on-surface-variant">${item.colorway}</p>
        <p class="text-sm font-semibold text-primary mt-1">$${item.price.toLocaleString()}</p>
      </div>
      <div class="flex items-center gap-2">
        <button class="cart-qty-btn w-7 h-7 rounded bg-surface-container hover:bg-secondary-fixed flex items-center justify-center text-primary text-xs font-bold" data-action="dec" data-id="${item.id}">-</button>
        <span class="text-sm font-semibold w-4 text-center">${item.quantity}</span>
        <button class="cart-qty-btn w-7 h-7 rounded bg-surface-container hover:bg-secondary-fixed flex items-center justify-center text-primary text-xs font-bold" data-action="inc" data-id="${item.id}">+</button>
      </div>
    `;
    container.appendChild(itemEl);
  });

  subtotalEl.textContent = `$${subtotal.toLocaleString()}.00`;

  container.querySelectorAll('.cart-qty-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const id = btn.getAttribute('data-id');
      const action = btn.getAttribute('data-action');
      let items = getCartItems();
      const index = items.findIndex(i => i.id === id);
      if (index > -1) {
        if (action === 'inc') items[index].quantity += 1;
        else if (action === 'dec') {
          items[index].quantity -= 1;
          if (items[index].quantity <= 0) items.splice(index, 1);
        }
        saveCartItems(items);
      }
    });
  });
}

function showCartToast(itemName) {
  const toast = document.getElementById('cart-toast');
  const toastTitle = document.getElementById('cart-toast-title');
  if (!toast || !toastTitle) return;
  toastTitle.textContent = `${itemName} added to your bag`;
  toast.classList.remove('translate-y-24', 'opacity-0');
  setTimeout(() => {
    toast.classList.add('translate-y-24', 'opacity-0');
  }, 3000);
}

/* ==========================================================================
   4. WEBGL LIQUID FLOW BACKGROUND SHADER
   ========================================================================== */
function initWebGLBackgroundShader() {
  const canvas = document.getElementById('global-shader-canvas');
  if (!canvas) return;

  function syncSize() {
    const w = window.innerWidth;
    const h = window.innerHeight;
    if (canvas.width !== w || canvas.height !== h) {
      canvas.width = w;
      canvas.height = h;
    }
  }
  syncSize();
  window.addEventListener('resize', syncSize);

  const gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
  if (!gl) return;

  const vs = `
    attribute vec2 a_position;
    varying vec2 v_texCoord;
    void main() {
      v_texCoord = a_position * 0.5 + 0.5;
      gl_Position = vec4(a_position, 0.0, 1.0);
    }
  `;

  const fs = `
    precision highp float;
    uniform float u_time;
    uniform vec2 u_resolution;
    varying vec2 v_texCoord;

    void main() {
      vec2 uv = v_texCoord;
      float wave1 = sin(uv.x * 2.8 + u_time * 0.35) * 0.5 + 0.5;
      float wave2 = sin(uv.y * 2.2 - u_time * 0.25) * 0.5 + 0.5;

      vec3 pearlWhite = vec3(0.99, 0.98, 0.99);
      vec3 deepNavy = vec3(0.08, 0.14, 0.26);
      vec3 softBlush = vec3(0.98, 0.86, 0.88);

      vec3 base = mix(pearlWhite, softBlush, wave1 * 0.30);
      base = mix(base, deepNavy, wave2 * 0.07 * (1.0 - uv.y));

      gl_FragColor = vec4(base, 1.0);
    }
  `;

  function createShader(type, source) {
    const s = gl.createShader(type);
    gl.shaderSource(s, source);
    gl.compileShader(s);
    return s;
  }

  const prog = gl.createProgram();
  gl.attachShader(prog, createShader(gl.VERTEX_SHADER, vs));
  gl.attachShader(prog, createShader(gl.FRAGMENT_SHADER, fs));
  gl.linkProgram(prog);
  gl.useProgram(prog);

  const buf = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER, buf);
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 1, -1, -1, 1, 1, 1]), gl.STATIC_DRAW);

  const pos = gl.getAttribLocation(prog, 'a_position');
  gl.enableVertexAttribArray(pos);
  gl.vertexAttribPointer(pos, 2, gl.FLOAT, false, 0, 0);

  const uTime = gl.getUniformLocation(prog, 'u_time');
  const uRes = gl.getUniformLocation(prog, 'u_resolution');

  function render(time) {
    gl.viewport(0, 0, canvas.width, canvas.height);
    if (uTime) gl.uniform1f(uTime, time * 0.001);
    if (uRes) gl.uniform2f(uRes, canvas.width, canvas.height);
    gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
    requestAnimationFrame(render);
  }
  render(0);
}

/* ==========================================================================
   5. ARCHITECTURAL 3D SCULPTURE & SPATIAL FABRIC VIEWER
   ========================================================================== */
function initThreeJSSpatialArtifacts() {
  const containers = document.querySelectorAll('[data-threejs="spatial-artifact"], #threejs-hero-container');
  if (!containers.length || typeof THREE === 'undefined') return;

  containers.forEach(container => {
    const width = container.clientWidth || 420;
    const height = container.clientHeight || 420;

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(55, width / height, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
    renderer.setSize(width, height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    container.innerHTML = '';
    container.appendChild(renderer.domElement);

    // Subtle ambient lighting + multi-point museum spotlighting
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.9);
    scene.add(ambientLight);

    const mainLight = new THREE.DirectionalLight(0xffffff, 1.4);
    mainLight.position.set(5, 8, 7);
    scene.add(mainLight);

    const rimLight = new THREE.DirectionalLight(0x1a2b4b, 1.1);
    rimLight.position.set(-6, -4, -5);
    scene.add(rimLight);

    // Architectural Core: Sculpted Organic Torus Knot representing tensioned memory alloy
    const coreGeometry = new THREE.TorusKnotGeometry(1.05, 0.32, 140, 24);
    const coreMaterial = new THREE.MeshStandardMaterial({
      color: 0xFADADD,
      roughness: 0.25,
      metalness: 0.65,
      emissive: 0x1A2B4B,
      emissiveIntensity: 0.08
    });
    const coreMesh = new THREE.Mesh(coreGeometry, coreMaterial);
    scene.add(coreMesh);

    // Spatial Lattice Wireframe Orbit
    const wireGeometry = new THREE.IcosahedronGeometry(1.85, 2);
    const wireMaterial = new THREE.MeshBasicMaterial({
      color: 0x031635,
      wireframe: true,
      transparent: true,
      opacity: 0.16
    });
    const wireMesh = new THREE.Mesh(wireGeometry, wireMaterial);
    scene.add(wireMesh);

    camera.position.z = 4.2;

    // Interactive Touch & Mouse Orbit Control
    let targetRotX = 0.3;
    let targetRotY = 0.5;
    let isDragging = false;
    let prevX = 0;
    let prevY = 0;

    const startDrag = (x, y) => {
      isDragging = true;
      prevX = x;
      prevY = y;
    };

    const moveDrag = (x, y) => {
      if (!isDragging) return;
      const dx = x - prevX;
      const dy = y - prevY;
      targetRotY += dx * 0.007;
      targetRotX += dy * 0.007;
      prevX = x;
      prevY = y;
    };

    const stopDrag = () => { isDragging = false; };

    container.addEventListener('mousedown', e => startDrag(e.clientX, e.clientY));
    window.addEventListener('mouseup', stopDrag);
    container.addEventListener('mousemove', e => moveDrag(e.clientX, e.clientY));

    container.addEventListener('touchstart', e => {
      if (e.touches.length === 1) startDrag(e.touches[0].clientX, e.touches[0].clientY);
    }, { passive: true });
    window.addEventListener('touchend', stopDrag);
    container.addEventListener('touchmove', e => {
      if (e.touches.length === 1) moveDrag(e.touches[0].clientX, e.touches[0].clientY);
    }, { passive: true });

    const animate = () => {
      requestAnimationFrame(animate);
      const time = Date.now() * 0.001;

      if (!isDragging) {
        targetRotY += 0.005;
        targetRotX = Math.sin(time * 0.5) * 0.2 + 0.2;
      }

      coreMesh.rotation.y += (targetRotY - coreMesh.rotation.y) * 0.12;
      coreMesh.rotation.x += (targetRotX - coreMesh.rotation.x) * 0.12;

      wireMesh.rotation.y = -coreMesh.rotation.y * 0.6;
      wireMesh.rotation.z = time * 0.15;

      coreMesh.position.y = Math.sin(time * 1.5) * 0.08;
      wireMesh.position.y = coreMesh.position.y;

      renderer.render(scene, camera);
    };
    animate();

    const handleResize = () => {
      const w = container.clientWidth || 420;
      const h = container.clientHeight || 420;
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
      renderer.setSize(w, h);
    };
    window.addEventListener('resize', handleResize);
  });
}

/* ==========================================================================
   6. COLLECTION FILTERING SYSTEM
   ========================================================================== */
function initCollectionFilters() {
  const filterButtons = document.querySelectorAll('.filter-chip-btn');
  const productCards = document.querySelectorAll('.product-card-item');

  if (!filterButtons.length || !productCards.length) return;

  filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      filterButtons.forEach(b => {
        b.classList.remove('bg-primary', 'text-on-primary');
        b.classList.add('bg-surface-container-low', 'text-on-surface-variant');
      });
      btn.classList.remove('bg-surface-container-low', 'text-on-surface-variant');
      btn.classList.add('bg-primary', 'text-on-primary');

      const category = btn.getAttribute('data-filter') || 'all';
      productCards.forEach(card => {
        const itemCat = card.getAttribute('data-category') || 'all';
        if (category === 'all' || itemCat === category) {
          card.style.display = 'flex';
          setTimeout(() => card.style.opacity = '1', 50);
        } else {
          card.style.opacity = '0';
          setTimeout(() => card.style.display = 'none', 280);
        }
      });
    });
  });
}
