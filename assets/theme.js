/**
 * FOUR FIT — SHOPIFY THEME STOREFRONT JAVASCRIPT ENGINE
 * Integrates WebGL Liquid Shader, High-Fidelity Three.js 3D Architectural Sculptures,
 * Shopify Ajax Cart System, & Smooth Scroll Reveal Animations.
 */

document.addEventListener('DOMContentLoaded', () => {
  initScrollReveal();
  initShopifyDrawers();
  initShopifyAjaxCart();
  initWebGLBackgroundShader();
  initThreeJSSpatialArtifacts();
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
   2. SHOPIFY DRAWER NAVIGATION & CART
   ========================================================================== */
function initShopifyDrawers() {
  const navDrawer = document.getElementById('side-drawer');
  const navContent = document.getElementById('drawer-content');
  const cartDrawer = document.getElementById('cart-drawer');
  const cartContent = document.getElementById('cart-drawer-content');

  document.querySelectorAll('#drawer-toggle').forEach(btn => {
    btn.addEventListener('click', () => {
      navDrawer?.classList.remove('pointer-events-none', 'opacity-0');
      navContent?.classList.remove('-translate-x-full');
      document.body.style.overflow = 'hidden';
    });
  });

  document.querySelectorAll('#drawer-close, #drawer-overlay').forEach(btn => {
    btn.addEventListener('click', () => {
      navDrawer?.classList.add('pointer-events-none', 'opacity-0');
      navContent?.classList.add('-translate-x-full');
      document.body.style.overflow = '';
    });
  });

  document.querySelectorAll('.cart-toggle-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      cartDrawer?.classList.remove('pointer-events-none', 'opacity-0');
      cartContent?.classList.remove('translate-x-full');
      document.body.style.overflow = 'hidden';
      fetchShopifyCart();
    });
  });

  document.querySelectorAll('#cart-close, #cart-overlay').forEach(btn => {
    btn.addEventListener('click', () => {
      cartDrawer?.classList.add('pointer-events-none', 'opacity-0');
      cartContent?.classList.add('translate-x-full');
      document.body.style.overflow = '';
    });
  });
}

function initShopifyAjaxCart() {
  document.querySelectorAll('form[action^="/cart/add"]').forEach(form => {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const formData = new FormData(form);
      try {
        const res = await fetch('/cart/add.js', {
          method: 'POST',
          body: formData
        });
        const item = await res.json();
        fetchShopifyCart();
        const cartDrawer = document.getElementById('cart-drawer');
        const cartContent = document.getElementById('cart-drawer-content');
        cartDrawer?.classList.remove('pointer-events-none', 'opacity-0');
        cartContent?.classList.remove('translate-x-full');
      } catch (err) {
        form.submit();
      }
    });
  });
}

async function fetchShopifyCart() {
  const container = document.getElementById('cart-items-container');
  const subtotalEl = document.getElementById('cart-subtotal-price');
  if (!container || !subtotalEl) return;

  try {
    const res = await fetch('/cart.js');
    const cart = await res.json();

    document.querySelectorAll('.cart-count-badge').forEach(b => {
      b.textContent = cart.item_count;
      b.style.display = cart.item_count > 0 ? 'inline-flex' : 'none';
    });

    subtotalEl.textContent = `${(cart.total_price / 100).toLocaleString('en-US', { style: 'currency', currency: 'USD' })}`;

    if (cart.items.length === 0) {
      container.innerHTML = `
        <div class="py-16 text-center">
          <p class="font-headline-md text-lg text-primary">Your bag is empty</p>
        </div>
      `;
      return;
    }

    container.innerHTML = '';
    cart.items.forEach(item => {
      const el = document.createElement('div');
      el.className = 'flex items-center gap-4 py-4 border-b border-primary/10';
      el.innerHTML = `
        <img src="${item.image}" alt="${item.title}" class="w-16 h-16 object-contain rounded-lg bg-surface-container-low p-1" />
        <div class="flex-1">
          <h4 class="font-headline-md text-sm font-semibold text-primary">${item.product_title}</h4>
          <p class="text-xs text-on-surface-variant">${item.variant_title || ''}</p>
          <p class="text-sm font-semibold text-primary mt-1">$${(item.price / 100).toFixed(2)}</p>
        </div>
        <span class="text-sm font-semibold">Qty: ${item.quantity}</span>
      `;
      container.appendChild(el);
    });
  } catch (e) {
    // Fallback if local preview outside Shopify
  }
}

/* ==========================================================================
   3. WEBGL LIQUID FLOW BACKGROUND SHADER
   ========================================================================== */
function initWebGLBackgroundShader() {
  const canvas = document.getElementById('global-shader-canvas');
  if (!canvas) return;

  function syncSize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
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
   4. HIGH-FIDELITY THREE.JS ARCHITECTURAL 3D SCULPTURE
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

    const ambientLight = new THREE.AmbientLight(0xffffff, 0.9);
    scene.add(ambientLight);

    const mainLight = new THREE.DirectionalLight(0xffffff, 1.4);
    mainLight.position.set(5, 8, 7);
    scene.add(mainLight);

    const rimLight = new THREE.DirectionalLight(0x1a2b4b, 1.1);
    rimLight.position.set(-6, -4, -5);
    scene.add(rimLight);

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

    window.addEventListener('resize', () => {
      const w = container.clientWidth || 420;
      const h = container.clientHeight || 420;
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
      renderer.setSize(w, h);
    });
  });
}
