# GameHub Mobile App — UX/UI Design Document

---

## Overview

This document provides a complete UX/UI design specification for **GameHub**, a one-stop offline puzzle gaming platform. It covers visual design, layout structure, interaction patterns, transitions, and screen-by-screen breakdowns for the Home, Login, Profile, and Settings screens. This document is intended to guide the mobile developer through the full implementation of the app's front-end experience.

---

## 1. VISUALS

### 1.1 Color Palette

GameHub's visual identity is built around a **dark, immersive gaming aesthetic** with vivid accent colors that evoke intelligence, energy, and fun — while remaining accessible and easy on the eyes during extended play sessions.

| Role | Color Name | Hex Code | Usage |
|---|---|---|---|
| **Primary Background** | Deep Space Navy | `#0D1117` | Main app background |
| **Secondary Background** | Midnight Slate | `#161B22` | Cards, modals, bottom sheets |
| **Surface / Card** | Graphite Ash | `#21262D` | Puzzle cards, list items, containers |
| **Primary Accent** | Electric Violet | `#7C3AED` | CTAs, active states, highlights |
| **Secondary Accent** | Neon Cyan | `#22D3EE` | Streaks, badges, progress bars |
| **Tertiary Accent** | Amber Glow | `#F59E0B` | XP indicators, daily challenge highlights |
| **Success** | Emerald Pulse | `#10B981` | Completion states, correct answers |
| **Error / Destructive** | Crimson Alert | `#EF4444` | Errors, delete actions, wrong answers |
| **Text Primary** | Snow White | `#F0F6FC` | Headings, primary body text |
| **Text Secondary** | Silver Mist | `#8B949E` | Subtitles, labels, hints |
| **Divider / Border** | Steel Edge | `#30363D` | Card borders, separators |
| **Overlay / Scrim** | Black Veil | `#000000` at 60% opacity | Modal backgrounds, bottom sheets |

#### Gradient Definitions

- **Hero Gradient:** `linear-gradient(135deg, #7C3AED 0%, #22D3EE 100%)` — Used on featured cards, onboarding screens, and premium CTAs.
- **XP Bar Gradient:** `linear-gradient(90deg, #7C3AED 0%, #F59E0B 100%)` — Used on the experience progress bar in the profile.
- **Daily Challenge Gradient:** `linear-gradient(135deg, #F59E0B 0%, #EF4444 100%)` — Used on the daily challenge card.
- **Streak Gradient:** `linear-gradient(135deg, #22D3EE 0%, #10B981 100%)` — Used on streak indicators and badges.

#### Colorblind-Friendly Mode

When enabled in Settings, the app replaces red/green states with:
- **Success:** `#0077BB` (Blue) replacing Emerald Pulse
- **Error:** `#EE7733` (Orange) replacing Crimson Alert
- All iconography is paired with text labels to avoid color-only communication.

---

### 1.2 Typography

GameHub uses a dual-font system — one for display/branding and one for body readability.

| Role | Font Family | Weight | Size | Line Height |
|---|---|---|---|---|
| **App Logo / Brand** | Orbitron | 700 (Bold) | 28sp | 36sp |
| **Screen Title (H1)** | Orbitron | 600 (SemiBold) | 24sp | 32sp |
| **Section Header (H2)** | Orbitron | 600 (SemiBold) | 18sp | 26sp |
| **Card Title (H3)** | Inter | 600 (SemiBold) | 16sp | 22sp |
| **Body Text** | Inter | 400 (Regular) | 14sp | 20sp |
| **Caption / Label** | Inter | 400 (Regular) | 12sp | 16sp |
| **Button Text** | Inter | 600 (SemiBold) | 15sp | 20sp |
| **Badge / Chip Text** | Inter | 700 (Bold) | 11sp | 14sp |

- **Minimum font size:** 12sp (never below, for accessibility)
- **Adjustable font scale:** Users can set 1x, 1.25x, or 1.5x scale in Settings, which multiplies all `sp` values proportionally.

---

### 1.3 Iconography

- **Icon Library:** Material Symbols (Rounded style) for system icons, supplemented by custom SVG icons for puzzle categories.
- **Icon Size:** 24dp standard; 20dp in dense lists; 32dp for feature highlights.
- **Icon Color:** Defaults to Text Secondary (`#8B949E`); active/selected state switches to Primary Accent (`#7C3AED`).
- **Puzzle Category Icons:** Custom-illustrated SVG icons per puzzle type (sudoku grid, crossword, jigsaw piece, maze path, etc.) rendered with `flutter_svg`.

---

### 1.4 Spacing & Layout Grid

- **Base Spacing Unit:** 8dp
- **Horizontal Screen Padding:** 16dp (left and right)
- **Card Internal Padding:** 16dp all sides
- **Section Vertical Spacing:** 24dp between major sections
- **Component Vertical Spacing:** 12dp between items in a list
- **Border Radius:**
  - Small (chips, badges): 8dp
  - Medium (cards, inputs): 12dp
  - Large (bottom sheets, featured cards): 20dp
  - Full (buttons, pills, avatars): 50dp (fully rounded)

---

### 1.5 Elevation & Shadows

Since the app uses a dark theme, elevation is communicated through **surface color lightening** rather than drop shadows:

| Elevation Level | Surface Color | Usage |
|---|---|---|
| Level 0 | `#0D1117` | Base background |
| Level 1 | `#161B22` | Sheets, drawers |
| Level 2 | `#21262D` | Cards, list items |
| Level 3 | `#2D333B` | Floating buttons, dropdowns |
| Level 4 | `#373E47` | Tooltips, snackbars |

Subtle `box-shadow: 0px 4px 12px rgba(0,0,0,0.4)` is applied to floating elements like the FAB and bottom navigation bar.

---

### 1.6 Buttons

#### Primary Button (CTA)
- **Background:** Electric Violet `#7C3AED`
- **Text:** Snow White `#F0F6FC`, Inter SemiBold 15sp
- **Border Radius:** 50dp (pill shape)
- **Height:** 52dp
- **Padding:** 16dp horizontal
- **Pressed State:** Background darkens to `#6D28D9`, scale animates to 0.97
- **Disabled State:** Background `#30363D`, text `#8B949E`
- **Shadow:** `0px 4px 16px rgba(124, 58, 237, 0.4)` (violet glow)

#### Secondary Button (Outlined)
- **Background:** Transparent
- **Border:** 1.5dp stroke, Electric Violet `#7C3AED`
- **Text:** Electric Violet `#7C3AED`, Inter SemiBold 15sp
- **Border Radius:** 50dp
- **Height:** 52dp
- **Pressed State:** Background fills to `rgba(124, 58, 237, 0.12)`

#### Ghost / Text Button
- **Background:** Transparent
- **Text:** Silver Mist `#8B949E`, Inter SemiBold 14sp
- **Pressed State:** Text brightens to Snow White, subtle underline appears

#### Icon Button (Circular)
- **Size:** 44dp × 44dp
- **Background:** Graphite Ash `#21262D`
- **Icon:** 22dp, Silver Mist `#8B949E`
- **Active State:** Background Electric Violet `#7C3AED`, icon Snow White
- **Border Radius:** 50dp

#### Danger Button (Destructive)
- **Background:** Crimson Alert `#EF4444`
- **Text:** Snow White, Inter SemiBold 15sp
- **Border Radius:** 50dp
- **Height:** 52dp
- **Pressed State:** Background darkens to `#DC2626`

---

### 1.7 Input Fields

- **Background:** Graphite Ash `#21262D`
- **Border:** 1dp Steel Edge `#30363D` at rest; 2dp Electric Violet `#7C3AED` on focus
- **Border Radius:** 12dp
- **Height:** 56dp
- **Text Color:** Snow White `#F0F6FC`, Inter Regular 14sp
- **Placeholder Color:** Silver Mist `#8B949E`
- **Label (floating):** Inter SemiBold 12sp, Electric Violet `#7C3AED` when focused
- **Error State:** Border Crimson Alert `#EF4444`, error message in 12sp below field
- **Leading Icon:** 20dp, Silver Mist (e.g., lock icon for password, envelope for email)
- **Trailing Icon:** Visibility toggle for password fields (eye icon)

---

### 1.8 Cards

#### Standard Puzzle Card
- **Size:** Full-width minus 32dp horizontal padding; height 100dp
- **Background:** Graphite Ash `#21262D`
- **Border Radius:** 12dp
- **Layout:** Horizontal — 56dp×56dp puzzle category icon on left (with gradient background circle), title + subtitle in center, difficulty badge on right
- **Difficulty Badge:** Pill-shaped chip; Beginner = Emerald Pulse, Intermediate = Amber Glow, Expert = Crimson Alert, Master = Electric Violet
- **Pressed State:** Background lightens to `#2D333B`, scale animates to 0.98

#### Featured / Hero Card
- **Size:** Full-width minus 32dp; height 180dp
- **Background:** Hero Gradient overlay on a blurred puzzle screenshot
- **Border Radius:** 20dp
- **Content:** Large title, subtitle, "Play Now" pill button at bottom-left
- **Badge:** "FEATURED" or "DAILY PICK" label at top-left, Amber Glow background

#### Stat Card (Profile)
- **Size:** (Screen width − 48dp) / 2 (two-column grid)
- **Height:** 100dp
- **Background:** Graphite Ash `#21262D`
- **Border Radius:** 12dp
- **Content:** Large number (H2 Orbitron), label caption below, small icon top-right

---

### 1.9 Bottom Navigation Bar

- **Background:** Midnight Slate `#161B22`
- **Height:** 64dp + safe area inset
- **Border Top:** 1dp Steel Edge `#30363D`
- **Items:** 4 tabs — Home, Explore, Challenges, Profile
- **Active Tab:** Icon Electric Violet `#7C3AED` + label Electric Violet, subtle pill indicator above icon
- **Inactive Tab:** Icon and label Silver Mist `#8B949E`
- **Tab Icons:** Home (house), Explore (compass), Challenges (trophy), Profile (person)
- **Animation:** Active indicator slides horizontally between tabs with a spring animation (300ms)

---

### 1.10 Animations & Transitions

| Transition Type | Duration | Easing | Usage |
|---|---|---|---|
| **Screen Push (forward)** | 350ms | Cubic ease-out | Navigate to new screen, slides in from right |
| **Screen Pop (back)** | 300ms | Cubic ease-in | Back navigation, slides out to right |
| **Modal / Bottom Sheet** | 400ms | Spring (damping 0.8) | Settings, filter panels slide up from bottom |
| **Tab Switch** | 250ms | Ease-in-out | Switching bottom nav tabs, fade + slight slide |
| **Card Press** | 100ms | Ease-out | Scale down to 0.97 on press, spring back on release |
| **Button Press** | 80ms | Ease-out | Scale to 0.97, darken background |
| **Achievement Unlock** | 600ms | Spring bounce | Badge scales from 0 to 1.1 then settles at 1.0 |
| **Streak Counter** | 500ms | Ease-out | Number rolls up with a slot-machine animation |
| **Progress Bar Fill** | 800ms | Ease-out | Bar fills from current to new value on screen load |
| **Puzzle Complete** | 1200ms | Custom spring | Confetti Lottie animation + card expands then collapses |
| **Shimmer Loading** | Loop, 1500ms | Linear | Skeleton placeholders while content loads |
| **Page Hero Transition** | 400ms | Ease-in-out | Shared element transition from card to puzzle screen |

---

## 2. SCREEN DESIGNS

---

### 2.1 Login Screen

#### Layout Structure

The Login screen is the first screen new users see after the splash/onboarding. It follows a **single-scroll, centered layout** with a dark immersive background.

**Background:**
A subtle animated particle field (slow-moving geometric puzzle piece shapes in `rgba(124, 58, 237, 0.08)`) overlaid on the Deep Space Navy background. This is implemented using a lightweight canvas animation — not video — to preserve battery and offline capability.

**Top Section — Branding (from top, ~30% of screen height):**
- Centered GameHub logo: custom SVG puzzle-piece-shaped icon (interlocking G and H letters) in Electric Violet, 72dp × 72dp, with a soft violet glow effect (`box-shadow: 0 0 32px rgba(124,58,237,0.5)`)
- App name "GAMEHUB" in Orbitron Bold 28sp, Snow White, centered, 12dp below icon
- Tagline: "100+ Puzzles. Zero Internet Required." in Inter Regular 14sp, Silver Mist, centered, 8dp below app name

**Middle Section — Auth Form (~40% of screen height):**

Displayed in a card container with Midnight Slate `#161B22` background, 20dp border radius, 24dp internal padding, positioned 32dp below the tagline:

- **Email Input Field** (full-width)
  - Leading icon: envelope (20dp, Silver Mist)
  - Placeholder: "Enter your email"
  - Keyboard type: email

- **12dp gap**

- **Password Input Field** (full-width)
  - Leading icon: lock (20dp, Silver Mist)
  - Trailing icon: eye toggle for show/hide
  - Placeholder: "Enter your password"

- **"Forgot Password?" text button** — right-aligned, 8dp below password field, Ghost style, "Forgot Password?" in Silver Mist 13sp

- **16dp gap**

- **"Sign In" Primary Button** — full-width, Electric Violet, pill shape, "Sign In" in Snow White Inter SemiBold 15sp

- **16dp gap**

- **Divider with label:** Thin Steel Edge lines on each side of "OR" text in Silver Mist 12sp

- **16dp gap**

- **"Continue with Google" Secondary Button** — full-width, outlined, leading Google logo SVG 20dp, "Continue with Google" text in Snow White 15sp

- **12dp gap**

- **"Continue with Apple" Secondary Button** — same style, Apple logo SVG (Snow White), "Continue with Apple" text

**Bottom Section — Registration CTA (~10% of screen height):**
- Centered text: "New to GameHub? " + tappable "Create Account" in Electric Violet SemiBold 14sp
- 16dp above the bottom safe area

#### Interaction Behaviors

- **Form Validation:** Real-time validation triggers on field blur (when user leaves the field). Error messages appear with a subtle shake animation (3 oscillations, 300ms) below the field in Crimson Alert 12sp.
- **Sign In Loading State:** On tap of "Sign In", the button text is replaced by a small circular progress indicator (Snow White, 20dp) and the button is disabled. This lasts until the auth response returns.
- **Success