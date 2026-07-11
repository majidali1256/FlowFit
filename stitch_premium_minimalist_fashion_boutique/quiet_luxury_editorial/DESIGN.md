---
name: Quiet Luxury Editorial
colors:
  surface: '#fbf8fc'
  surface-dim: '#dbd9dc'
  surface-bright: '#fbf8fc'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f6'
  surface-container: '#efedf0'
  surface-container-high: '#e9e7eb'
  surface-container-highest: '#e4e2e5'
  on-surface: '#1b1b1e'
  on-surface-variant: '#44474e'
  inverse-surface: '#303033'
  inverse-on-surface: '#f2f0f3'
  outline: '#75777f'
  outline-variant: '#c5c6cf'
  surface-tint: '#4e5e81'
  primary: '#031635'
  on-primary: '#ffffff'
  primary-container: '#1a2b4b'
  on-primary-container: '#8293b8'
  inverse-primary: '#b6c6ef'
  secondary: '#70585b'
  on-secondary: '#ffffff'
  secondary-container: '#f8d8db'
  on-secondary-container: '#755d5f'
  tertiary: '#231400'
  on-tertiary: '#ffffff'
  tertiary-container: '#3e2700'
  on-tertiary-container: '#b08d5b'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#b6c6ef'
  on-primary-fixed: '#081b3a'
  on-primary-fixed-variant: '#364768'
  secondary-fixed: '#fbdbde'
  secondary-fixed-dim: '#debfc2'
  on-secondary-fixed: '#281719'
  on-secondary-fixed-variant: '#574144'
  tertiary-fixed: '#ffddb1'
  tertiary-fixed-dim: '#e8c08a'
  on-tertiary-fixed: '#291800'
  on-tertiary-fixed-variant: '#5d4217'
  background: '#fbf8fc'
  on-background: '#1b1b1e'
  surface-variant: '#e4e2e5'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 28px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 20px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style
The brand personality is authoritative yet approachable, blending the timeless sophistication of high-end editorial fashion with the precision of contemporary technology. It targets an audience that values "Four Fit" for its curation, quality, and seamless digital experience.

The design style is a hybrid of **Modern Minimalism** and **Soft 3D Glassmorphism**. It utilizes expansive white space and high-quality imagery to evoke a sense of calm and exclusivity. The "tech-forward edge" is achieved through subtle 3D depth, ultra-smooth transitions, and a crisp, structured layout that feels both architectural and fluid.

## Colors
The palette is rooted in a "Deep Professional Blue," providing a foundation of trust and permanence. This is softened by "Soft Blush Pink," used as a sophisticated accent for highlights, calls-to-action, and subtle background washes. 

The primary surface is a "Crisp White," ensuring the interface feels airy and premium. Use the primary blue for all structural typography and high-emphasis elements. The blush pink should be used sparingly to guide the eye without overwhelming the minimalist aesthetic.

## Typography
The typography strategy creates a high-contrast dialogue between tradition and modernity. **Playfair Display** serves as the editorial voice, used for headlines and display text to convey luxury and heritage. **Inter** provides the functional, tech-forward counterpoint, offering exceptional legibility for body copy and UI controls.

All labels should utilize a slight letter-spacing increase and uppercase styling when used for navigation or category tags to maintain the "Quiet Luxury" look.

## Layout & Spacing
The layout follows a **Fixed Grid** model on desktop to maintain editorial control over line lengths and image proportions, transitioning to a fluid model on mobile. A 12-column grid is used for desktop (1280px max-width) with generous 64px outer margins to create "breathing room."

Spacing follows an 8px rhythmic scale. Vertical rhythm is intentionally loose (using `stack-lg`) between major sections to emphasize the minimalist, premium feel. Content should be center-aligned or asymmetrically balanced to mimic high-end magazine layouts.

## Elevation & Depth
This design system uses **Tonal Layers** combined with **Ambient Shadows** to create a 3D-oriented feel. Depth is not communicated through heavy shadows, but through subtle shifts in surface color and "Soft Blush" tinted glows.

Higher elevation levels (like modals or floating menus) should use a backdrop blur (20px-30px) and a very thin (1px) semi-transparent stroke in the Primary Blue at 10% opacity. This creates a "glass" effect that feels modern and lightweight.

## Shapes
Following the "ROUND_EIGHT" directive, the design system utilizes a **Rounded** shape language. Standard UI elements (buttons, inputs) use a 0.5rem (8px) radius. Larger cards and containers scale up to 1rem (16px) or 1.5rem (24px) to maintain visual harmony. This softening of the grid prevents the minimalist aesthetic from feeling too cold or clinical.

## Components
- **Buttons:** Primary buttons are solid Deep Professional Blue with white Inter typography. Secondary buttons use a Soft Blush Pink fill with Primary Blue text. All buttons have a subtle 3D lift on hover rather than a color change.
- **Input Fields:** Use a 1px border of the Primary Blue at 20% opacity. Upon focus, the border becomes 100% opacity with a soft Blush Pink outer glow (4px spread).
- **Cards:** Cards are Crisp White with a very soft, diffused shadow (0px 10px 30px rgba(26, 43, 75, 0.05)). They should feature ample internal padding (32px).
- **Chips/Badges:** Use the Soft Blush Pink background with Primary Blue text, utilizing fully rounded (pill) corners to contrast against the 8px corners of primary buttons.
- **Lists:** Clean, borderless rows separated by subtle 1px Blush Pink dividers.
- **Navigation:** A persistent, high-blur glassmorphic header that stays fixed at the top of the viewport.