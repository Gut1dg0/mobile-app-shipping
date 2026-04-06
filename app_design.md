The image generation tool has failed twice. I will now proceed to deliver the complete written design document as the final answer, since the core deliverable is the written UX/UI design document and the tool is unavailable.

---

# PuzzlePal – UX/UI Design Document

**Prepared by:** Senior UX/UI Designer
**App:** PuzzlePal – A Comprehensive Puzzle Game Mobile App
**Platform:** iOS & Android (Flutter)
**Version:** 1.0 – MVP Design Spec

---

## Table of Contents

1. [Design Philosophy](#design-philosophy)
2. [Visuals](#visuals)
   - Color Palette
   - Typography
   - Iconography
   - Layout System
   - Component Library (Buttons, Cards, Inputs, Navigation)
   - Animations & Transitions
3. [Screen Designs](#screen-designs)
   - Login Screen
   - Home Screen
   - Profile Screen
   - Settings Screen
4. [Features & Interaction Design](#features--interaction-design)
   - Navigation Flow
   - Login & Onboarding Flow
   - Puzzle Interaction Flow
   - Removing / Managing Elements
   - Notifications & Feedback

---

## 1. Design Philosophy

PuzzlePal is designed around three core UX principles:

- **Playful Clarity** – The interface should feel fun and engaging without sacrificing readability or ease of use. Every screen should be immediately understandable to a 10-year-old and a 55-year-old alike.
- **Offline-First Confidence** – The UI must clearly communicate what is available offline versus online, so users always feel in control, especially in low-connectivity environments.
- **Progressive Depth** – Casual users should feel welcomed by a simple surface layer, while puzzle enthusiasts can discover deeper features (stats, custom puzzles, leaderboards) through natural exploration.

The visual language draws from **modern mobile gaming aesthetics** combined with **clean productivity app principles** — vibrant enough to feel like a game, structured enough to feel trustworthy and easy to navigate.

---

## 2. Visuals

### 2.1 Color Palette

The PuzzlePal color system uses a **dark-first design** with a rich, jewel-toned palette that evokes intelligence, creativity, and playfulness. A light mode alternative is fully supported.

#### Primary Colors

| Role | Color Name | Hex Code | Usage |
|---|---|---|---|
| Primary Brand | Deep Indigo | `#3D2B8E` | Primary buttons, headers, brand elements |
| Primary Accent | Electric Violet | `#7B4FD4` | Highlighted cards, active states, gradients |
| Secondary Accent | Teal Glow | `#00C9B1` | Success states, streak indicators, CTA highlights |
| Warm Accent | Amber Spark | `#FFB830` | Achievement badges, hints, premium indicators |

#### Background Colors (Dark Mode)

| Role | Color Name | Hex Code | Usage |
|---|---|---|---|
| App Background | Deep Space | `#0F0E1A` | Main screen background |
| Surface / Card | Midnight Card | `#1C1A2E` | Cards, bottom sheets, modals |
| Elevated Surface | Soft Slate | `#252340` | Input fields, secondary cards |
| Divider / Border | Ghost Line | `#2E2B4A` | Separators, borders |

#### Background Colors (Light Mode)

| Role | Color Name | Hex Code | Usage |
|---|---|---|---|
| App Background | Soft Lavender White | `#F4F2FF` | Main screen background |
| Surface / Card | Pure White | `#FFFFFF` | Cards, modals |
| Elevated Surface | Light Gray | `#EDEBF8` | Input fields, secondary cards |
| Divider / Border | Pale Violet | `#D5D0F0` | Separators, borders |

#### Semantic Colors

| Role | Hex Code | Usage |
|---|---|---|
| Success | `#00C9B1` | Puzzle complete, correct answers |
| Warning | `#FFB830` | Hint usage, time running low |
| Error / Danger | `#FF4F6E` | Wrong answer feedback, error states |
| Info | `#5BB8FF` | Tooltips, informational banners |
| Premium Gold | `#F5C518` | Premium badge, subscription CTA |

#### Gradient Definitions

- **Hero Gradient (used on splash, login header):** `linear-gradient(135deg, #3D2B8E → #7B4FD4 → #00C9B1)`
- **Card Accent Gradient:** `linear-gradient(120deg, #3D2B8E → #5C3DBF)`
- **Premium CTA Gradient:** `linear-gradient(135deg, #F5C518 → #FFB830)`

---

### 2.2 Typography

PuzzlePal uses a dual-typeface system: one for display/headings and one for body/UI text.

#### Typefaces

| Role | Font | Weight | Notes |
|---|---|---|---|
| Display / Headings | **Nunito** | 700, 800 (ExtraBold) | Rounded, friendly, highly legible |
| Body / UI Text | **Inter** | 400, 500, 600 | Clean, neutral, excellent screen rendering |
| Monospace (Scores/Stats) | **Roboto Mono** | 500 | Used for timers, scores, puzzle numbers |

#### Type Scale

| Level | Font | Size | Weight | Line Height | Usage |
|---|---|---|---|---|---|
| H1 | Nunito | 32sp | 800 | 40sp | Screen titles (Login, Profile) |
| H2 | Nunito | 24sp | 700 | 32sp | Section headers |
| H3 | Nunito | 20sp | 700 | 28sp | Card titles |
| Body Large | Inter | 16sp | 400 | 24sp | Main body text |
| Body Medium | Inter | 14sp | 400 | 22sp | Secondary descriptions |
| Caption | Inter | 12sp | 400 | 18sp | Labels, timestamps, hints |
| Button | Inter | 15sp | 600 | 20sp | All button labels |
| Score/Timer | Roboto Mono | 18sp | 500 | 24sp | In-game timers, scores |

---

### 2.3 Iconography

- **Icon Library:** Phosphor Icons (rounded variant) — chosen for their playful, consistent weight and excellent legibility at small sizes.
- **Icon Size Standards:**
  - Navigation bar icons: 24×24dp
  - In-card action icons: 20×20dp
  - Feature/category icons: 40×40dp (with colored background pill)
  - Achievement badge icons: 48×48dp
- **Icon Color:** Icons inherit the color of their context (white on dark backgrounds, `#3D2B8E` on light backgrounds, `#00C9B1` for active/success states).
- **Custom Puzzle Category Icons:** Each puzzle category (Car, Photo, Classic, Logic, Brain, Sliding, Color) has a custom illustrated icon in a rounded-square container with a unique gradient background per category.

#### Category Icon Color Codes

| Category | Background Gradient | Icon Color |
|---|---|---|
| Car Puzzles | `#FF6B35 → #FF4F6E` | White |
| Photo Puzzles | `#5BB8FF → #3D2B8E` | White |
| Classic Puzzles | `#7B4FD4 → #3D2B8E` | White |
| Logic Puzzles | `#00C9B1 → #0097A7` | White |
| Brain Teasers | `#FFB830 → #FF6B35` | White |
| Sliding Puzzles | `#F5C518 → #FFB830` | Deep Indigo |
| Color Puzzles | `#FF4F6E → #C2185B` | White |
| Daily Challenge | `#3D2B8E → #7B4FD4` | Amber Spark |

---

### 2.4 Layout System

- **Grid:** 4-column grid on mobile (375dp base width), 8dp base spacing unit.
- **Margins:** 16dp horizontal screen margins.
- **Gutter:** 12dp between grid columns.
- **Card Radius:** 16dp (standard cards), 24dp (hero cards, modal sheets), 12dp (small chips/badges), 100dp (pills/buttons).
- **Safe Areas:** All content respects iOS safe area insets (top notch, bottom home indicator) and Android status bar/navigation bar.
- **Bottom Navigation Bar Height:** 64dp (plus bottom safe area).
- **Top App Bar Height:** 56dp.
- **Touch Target Minimum:** 48×48dp for all interactive elements (WCAG AA compliance).

#### Elevation & Shadow System (Dark Mode)

| Level | Shadow | Usage |
|---|---|---|
| Level 0 | None | Flat backgrounds |
| Level 1 | `0 2px 8px rgba(0,0,0,0.4)` | Standard cards |
| Level 2 | `0 4px 16px rgba(61,43,142,0.35)` | Elevated cards, active states |
| Level 3 | `0 8px 32px rgba(61,43,142,0.5)` | Modals, bottom sheets |
| Glow (Accent) | `0 0 20px rgba(123,79,212,0.6)` | Active puzzle tile, CTA buttons |

---

### 2.5 Component Library

#### Buttons

**Primary Button (Filled)**
- Background: Electric Violet `#7B4FD4` (default) or Hero Gradient on key CTAs
- Text: White, Inter 600, 15sp
- Height: 52dp
- Corner Radius: 100dp (fully rounded pill)
- Padding: 16dp horizontal
- Shadow: Level 2 with violet glow
- Pressed State: Scale down to 96%, darken background by 10%, haptic feedback (medium impact)
- Disabled State: Background `#2E2B4A`, text `#6B6880`, no shadow

**Secondary Button (Outlined)**
- Background: Transparent
- Border: 1.5dp, Electric Violet `#7B4FD4`
- Text: Electric Violet `#7B4FD4`, Inter 600, 15sp
- Height: 52dp
- Corner Radius: 100dp
- Pressed State: Background fills to `rgba(123,79,212,0.12)`, scale 96%

**Ghost / Text Button**
- Background: Transparent, no border
- Text: Teal Glow `#00C9B1`, Inter 600, 14sp
- Used for: "Skip", "Cancel", "See All" links
- Pressed State: Opacity drops to 60%

**Premium CTA Button**
- Background: Premium Gold Gradient `#F5C518 → #FFB830`
- Text: Deep Indigo `#3D2B8E`, Inter 700, 15sp
- Height: 52dp
- Corner Radius: 100dp
- Shadow: `0 4px 20px rgba(245,197,24,0.5)`
- Has a small crown icon (👑) to the left of the label

**Icon Button (Circular)**
- Size: 44×44dp
- Background: Midnight Card `#1C1A2E` (dark mode) / White (light mode)
- Border: 1dp Ghost Line
- Icon: 20×20dp
- Corner Radius: 100dp
- Used for: Back navigation, favorite/bookmark, share

**Floating Action Button (FAB)**
- Size: 56×56dp
- Background: Hero Gradient
- Icon: 24×24dp white
- Shadow: Level 3 with violet glow
- Used on: Home screen (Create Custom Puzzle shortcut)

---

#### Cards

**Standard Puzzle Card**
- Size: Full width (minus 32dp margins) or 2-column grid (half width minus 20dp)
- Background: Midnight Card `#1C1A2E` with subtle gradient overlay
- Corner Radius: 16dp
- Padding: 16dp
- Contains: Category icon (40dp), puzzle title (H3), difficulty badge, completion percentage bar, offline indicator dot
- Shadow: Level 1
- Active/Pressed: Scale 97%, Level 2 shadow with glow

**Hero Feature Card**
- Size: Full width, height 180dp
- Background: Category gradient as full bleed background image with dark overlay `rgba(0,0,0,0.45)`
- Corner Radius: 24dp
- Contains: Large category icon, puzzle pack title (H2 white), subtitle, CTA button

**Daily Challenge Card**
- Size: Full width, height 120dp
- Background: `linear-gradient(135deg, #3D2B8E → #7B4FD4)`
- Animated: Subtle pulsing glow border in Amber Spark
- Contains: Flame streak icon, "Day X Streak" label, puzzle title, "Play Now" button

**Achievement Badge Card**
- Size: 80×80dp
- Shape: Hexagonal clip (using custom path) with gradient background
- Contains: Icon (32dp), locked state shows grayscale with lock icon overlay

---

#### Input Fields

- Height: 56dp
- Background: Soft Slate `#252340` (dark) / `#EDEBF8` (light)
- Border: 1dp Ghost Line (default), 2dp Electric Violet (focused), 2dp Error Red (error)
- Corner Radius: 12dp
- Label: Floating label animation (moves up on focus, Inter 12sp caption)
- Text: Inter 400, 16sp, white (dark) / Deep Indigo (light)
- Placeholder: 50% opacity of text color
- Trailing icons: Eye toggle (password), clear button (X), validation checkmark

---

#### Bottom Navigation Bar

- Height: 64dp + safe area
- Background: Midnight Card `#1C1A2E` with top border `1dp Ghost Line`
- Blur Effect: `backdrop-filter: blur(20px)` with slight transparency
- 5 tabs: Home, Explore, Daily, Leaderboard, Profile
- Active Tab: Icon in Electric Violet + Teal Glow dot indicator below + label visible
- Inactive Tab: Icon in `#6B6880`, no label
- Transition: Icon scales from 1.0 to 1.2 with spring animation on selection

#### Tab Icons
| Tab | Icon (Phosphor) |
|---|---|
| Home | `House` |
| Explore | `MagnifyingGlass` |
| Daily | `Lightning` |
| Leaderboard | `Trophy` |
| Profile | `UserCircle` |

---

#### Chips & Badges

**Difficulty Badge**
- Height: 24dp, auto width
- Corner Radius: 100dp
- Padding: 6dp × 12dp
- Colors: Easy `#00C9B1`, Medium `#FFB830`, Hard `#FF6B35`, Expert `#FF4F6E`
- Text: Inter 600, 11sp, white

**Offline Available Badge**
- Small green dot (8dp) + "Offline" label in Inter 11sp `#00C9B1`
- Appears on puzzle cards when pack is downloaded

**Premium Badge**
- Small crown icon + "PRO" text in Amber Spark
- Appears on locked premium content

**New Badge**
- Bright Electric Violet pill with "NEW" text
- Animated: subtle scale pulse for 3 days after content launch

---

### 2.6 Animations & Transitions

#### Screen Transitions

| Transition Type | Animation | Duration | Easing |
|---|---|---|---|
| Push (navigate forward) | Slide in from right + fade | 280ms | `cubic-bezier(0.4, 0, 0.2, 1)` |
| Pop (navigate back) | Slide out to right + fade | 250ms | `cubic-bezier(0.4, 0, 0.2, 1)` |
| Modal / Bottom Sheet | Slide up from bottom | 320ms | Spring (damping 0.8) |
| Tab Switch | Crossfade + icon spring | 200ms | Spring |
| Splash → Login | Zoom out + fade | 400ms | `ease-out` |

#### Micro-interactions

- **Button Press:** Scale 96% + haptic (medium) — 100ms spring return
- **Card Press:** Scale 97% + glow elevation increase —