# MindfulBreath Mobile App - UX/UI Design Document

## Executive Summary

This comprehensive design document outlines the complete user experience and interface specifications for the MindfulBreath mobile application. The design philosophy centers on creating a calming, intuitive, and scientifically-backed mental wellness experience that leverages AI technology while maintaining human warmth and accessibility.

## Design Philosophy

### Core Principles
- **Calm First**: Every design decision prioritizes reducing cognitive load and promoting tranquility
- **Accessibility**: Inclusive design supporting users across all anxiety levels and technical abilities
- **Scientific Credibility**: Visual language that conveys trustworthiness and medical validity
- **Personalized Experience**: Adaptive interfaces that evolve with user preferences and needs
- **Seamless Flow**: Frictionless navigation that never interrupts the wellness journey

## Visual Design System

### Color Palette

**Primary Colors**
- **Tranquil Blue**: #4A90E2 - Primary brand color, used for main CTAs and active states
- **Deep Calm**: #2C5282 - Secondary blue for headers and emphasis
- **Soft Sky**: #E6F2FF - Light blue for backgrounds and cards

**Secondary Colors**
- **Lavender Mist**: #9B88FF - Accent color for premium features and achievements
- **Sage Green**: #68D391 - Success states and positive feedback
- **Warm Coral**: #FC8181 - Gentle alerts and reminders (never harsh red)
- **Moonlight Gray**: #F7FAFC - Primary background color

**Neutral Palette**
- **Charcoal**: #2D3748 - Primary text color
- **Stone**: #718096 - Secondary text and icons
- **Pearl**: #E2E8F0 - Dividers and borders
- **Pure White**: #FFFFFF - Card backgrounds and input fields

**Gradient System**
- **Morning Breath**: Linear gradient from #4A90E2 to #9B88FF (120°)
- **Evening Calm**: Linear gradient from #2C5282 to #4A90E2 (180°)
- **Premium Glow**: Radial gradient from #9B88FF to #4A90E2

### Typography

**Font Family**
- **Primary**: SF Pro Display (iOS) / Google Sans (Android)
- **Secondary**: Inter for body text
- **Monospace**: SF Mono for timers and metrics

**Type Scale**
- **H1**: 32px/40px - Bold (Screen titles)
- **H2**: 24px/32px - Semibold (Section headers)
- **H3**: 20px/28px - Medium (Card titles)
- **Body Large**: 17px/24px - Regular (Primary content)
- **Body**: 15px/22px - Regular (Standard text)
- **Caption**: 13px/18px - Regular (Supporting text)
- **Micro**: 11px/14px - Medium (Labels and badges)

### Spacing System
- **Base unit**: 4px
- **Spacing scale**: 4, 8, 12, 16, 24, 32, 48, 64, 96px
- **Screen padding**: 16px horizontal, 24px vertical
- **Card padding**: 16px all sides
- **Component spacing**: 12px between related, 24px between sections

### Elevation & Shadows
- **Level 0**: No shadow (flat elements)
- **Level 1**: 0 2px 4px rgba(0,0,0,0.08) - Cards and buttons
- **Level 2**: 0 4px 12px rgba(0,0,0,0.12) - Floating elements
- **Level 3**: 0 8px 24px rgba(0,0,0,0.16) - Modals and overlays

### Border Radius
- **Small**: 8px - Buttons and inputs
- **Medium**: 12px - Cards and containers
- **Large**: 16px - Modals and sheets
- **Full**: 50% - Circular elements and avatars

## Component Library

### Buttons

**Primary Button**
- Background: #4A90E2
- Text: White, 16px semibold
- Height: 48px
- Border radius: 8px
- Shadow: Level 1
- Pressed state: Darken 10%, scale 0.98
- Disabled: 40% opacity

**Secondary Button**
- Background: White
- Border: 1px solid #E2E8F0
- Text: #4A90E2, 16px medium
- Height: 48px
- Border radius: 8px
- Shadow: None
- Hover: Background #F7FAFC

**Text Button**
- Background: Transparent
- Text: #4A90E2, 15px medium
- Padding: 8px 12px
- Underline on hover

**Floating Action Button**
- Size: 56px diameter
- Background: Morning Breath gradient
- Icon: White, 24px
- Shadow: Level 2
- Position: Bottom right, 16px margin

### Input Fields

**Standard Input**
- Height: 48px
- Background: White
- Border: 1px solid #E2E8F0
- Border radius: 8px
- Padding: 12px 16px
- Focus: Border #4A90E2, shadow 0 0 0 3px rgba(74,144,226,0.1)
- Error: Border #FC8181, helper text below

**Text Area**
- Min height: 96px
- Same styling as standard input
- Auto-expanding with max height 200px

### Cards

**Content Card**
- Background: White
- Border radius: 12px
- Shadow: Level 1
- Padding: 16px
- Margin bottom: 12px

**Feature Card**
- Background: Linear gradient overlay on white
- Border radius: 16px
- Shadow: Level 2
- Padding: 24px
- Premium badge: Top right corner

### Navigation Components

**Tab Bar**
- Height: 56px
- Background: White with top border
- 5 tabs maximum
- Active: Icon #4A90E2, label visible
- Inactive: Icon #718096, label hidden on scroll

**Navigation Bar**
- Height: 64px
- Background: Blur effect over content
- Title: Center aligned, 20px semibold
- Actions: Icon buttons 44x44px touch target

### Feedback Elements

**Progress Indicators**
- Circular: 4px stroke, animated gradient
- Linear: 4px height, rounded ends
- Skeleton screens for loading states

**Toasts & Alerts**
- Position: Top of screen, below nav bar
- Background: White with colored left border
- Auto-dismiss: 3 seconds
- Swipe to dismiss gesture

## Screen Specifications

### 1. Login Screen

**Layout Structure**
- Status bar: System default
- Logo placement: Center, 120px from top
- Welcome message: 24px below logo
- Form container: 48px below message
- Social login: Bottom of screen

**Components**
- Logo: 80x80px, with app name below (24px semibold)
- Welcome text: "Welcome to your calm space" (H2, #2D3748)
- Email input: Standard input with email icon
- Password input: Standard input with eye toggle
- "Forgot Password?": Text button, right aligned
- Login button: Primary button, full width
- Divider: "Or continue with" (Caption, centered)
- Social buttons: Google, Apple, Facebook (48px height, outlined)
- Sign up prompt: "New here? Create account" (bottom safe area)

**Animations**
- Logo: Gentle breathing animation (scale 1.0 to 1.05, 4s loop)
- Form: Slide up from bottom (0.3s ease-out)
- Keyboard: Push content up smoothly

**Validation**
- Real-time email format validation
- Password strength indicator
- Error messages: Below fields, #FC8181
- Success: Smooth transition to onboarding/home

### 2. Home Screen

**Layout Structure**
- Navigation bar: "MindfulBreath" title, profile avatar right
- Greeting section: Personalized message with time of day
- Quick action cards: 2x2 grid
- Current state widget: AI-detected mood/stress
- Recommended sessions: Horizontal scroll
- Daily affirmation: Expandable card
- Bottom tab bar: 5 tabs

**Components**

*Greeting Section* (24px from top)
- "Good [morning], [Name]" (H1, #2D3748)
- "How are you feeling?" (Body, #718096)
- Mood selector: 5 emoji options in a row

*Quick Actions Grid* (32px below greeting)
- Card size: (screen width - 48) / 2
- Icons: 32px, centered
- Labels: Caption, centered
- Actions: "Quick Breathe", "Check Anxiety", "Daily Affirmation", "Sleep Mode"

*Current State Widget* (24px below grid)
- Full width card with gradient background
- Heart rate visualization: Live waveform
- Stress level: Visual meter with color coding
- "Start Breathing" CTA: Secondary button

*Recommended Sessions* (24px below state)
- Section title: "Recommended for you" (H3)
- Card width: 280px, height: 160px
- Horizontal scroll with peek of next card
- Each card: Image background, title, duration, difficulty

*Daily Affirmation* (24px below sessions)
- Collapsed: Shows first line with expand arrow
- Expanded: Full text with share and save buttons
- Background: Soft gradient
- Typography: 18px medium, centered

**Animations**
- Mood selector: Bounce on selection
- Quick action cards: Subtle lift on press
- Heart rate: Continuous wave animation
- Session cards: Parallax on scroll

### 3. Profile Screen

**Layout Structure**
- Navigation bar: "Profile", edit button right
- Profile header: Avatar, name, stats
- Achievement section: Recent badges
- Statistics dashboard: Weekly/monthly views
- Subscription status: Current plan card
- Settings shortcuts: List format
- Bottom tab bar: Highlighted profile tab

**Components**

*Profile Header* (24px from top)
- Avatar: 96px circle, center aligned
- Edit overlay: Camera icon on avatar tap
- Name: H2, centered
- Member since: Caption, #718096
- Stats row: 3 columns (Sessions, Streak, Minutes)

*Achievements* (32px below header)
- Section title: "Recent Achievements" (H3)
- Badge size: 64px
- Horizontal scroll, 5 max visible
- Each badge: Icon, title below
- "View all" link: Text button, right aligned

*Statistics Dashboard* (24px below achievements)
- Toggle: "Week" / "Month" segmented control
- Chart: Line graph showing anxiety trends
- Key metrics: Cards below chart
  - Average anxiety level
  - Total breathing minutes
  - Improvement percentage
- Export button: "Share with therapist"

*Subscription Card* (24px below stats)
- Current plan: "Free" or "Premium"
- Benefits list: Checkmarks, 13px text
- Upgrade CTA: Primary button if free user
- Manage link: Text button if premium

*Settings List* (24px below subscription)
- Row height: 56px
- Icons: 24px, #718096
- Chevron: Right side, 16px
- Options: Reminders, Privacy, Help, About, Logout

**Interactions**
- Pull to refresh: Updates statistics
- Avatar tap: Photo picker
- Stats tap: Detailed view modal
- Achievement tap: Share modal

### 4. Settings Screen

**Layout Structure**
- Navigation bar: Back arrow, "Settings" title
- Grouped sections: Preferences, Account, Support, About
- Toggle switches: Right aligned
- Nested navigation: Chevrons for sub-screens

**Components**

*Preferences Section*
- Notifications: Toggle with sub-options
  - Breathing reminders
  - Daily affirmations
  - Achievement alerts
  - Marketing messages
- App appearance: Light/Dark/Auto selector
- Sounds: Toggle with volume slider
- Haptics: Toggle switch
- Language: Current selection with chevron

*Account Section*
- Profile information: Email, name (chevron to edit)
- Password: "Change password" with chevron
- Subscription: Current plan with manage option
- Connected devices: List of wearables
- Data & Privacy: Export, delete options

*Support Section*
- Help center: Chevron navigation
- Contact support: Email/chat options
- FAQ: Chevron navigation
- Community: Link to forums

*About Section*
- Version: App version number
- Terms of service: Chevron navigation
- Privacy policy: Chevron navigation
- Licenses: Open source attributions
- Rate app: Opens store rating

**Visual Treatment**
- Section headers: Caps, 11px, #718096, 24px padding top
- Row separators: 1px, #E2E8F0, inset 16px
- Toggle switches: #4A90E2 when on
- Destructive actions: #FC8181 text (logout, delete)

## User Flows

### Onboarding Flow (First-time users)

1. **Welcome Screen**
   - Logo animation
   - "Welcome to MindfulBreath" message
   - "Get Started" primary button

2. **Personal Goals**
   - "What brings you here?" question
   - Multi-select options: Reduce anxiety, Better sleep, Daily calm, Focus
   - Progress indicator: 1 of 4

3. **Experience Level**
   - "Have you practiced breathing exercises?"
   - Options: Beginner, Some experience, Regular practice
   - Progress indicator: 2 of 4

4. **Notification Preferences**
   - "When should we check in?"
   - Time picker for daily reminder
   - Skip option available
   - Progress indicator: 3 of 4

5. **AI Permissions**
   - Explain camera/microphone usage
   - Optional permissions with benefits explained
   - "Enable" or "Maybe later" options
   - Progress indicator: 4 of 4

6. **Completion**
   - Celebration animation
   - "You're all set!" message
   - "Start first session" CTA

### Daily Session Flow

1. **Session Selection**
   - Choose from recommended or browse all
   - Filter by duration, difficulty, goal
   - Preview with description and reviews

2. **Pre-Session Check**
   - "How are you feeling?" (1-10 scale)
   - Optional: Camera-based heart rate check
   - Session customization based on input

3. **Active Session**
   - Full-screen breathing visualization
   - Timer and progress ring
   - Pause/stop controls (swipe down)
   - Haptic feedback on inhale/exhale

4. **Post-Session**
   - "How do you feel now?" (1-10 scale)
   - Session summary: Duration, technique, improvement
   - Save to favorites option
   - Share achievement option

5. **Insights**
   - AI-generated insights about progress
   - Recommendations for next session
   - Option to schedule reminder

### Premium Upgrade Flow

1. **Trigger Points**
   - Locked feature tap
   - Profile subscription card
   - Settings subscription menu

2. **Premium Benefits Screen**
   - Full-screen presentation
   - Feature comparison table
   - Testimonials carousel
   - Pricing: Monthly vs Annual toggle

3. **Payment**
   - Apple Pay / Google Pay primary
   - Credit card fallback
   - Promo code field (collapsible)
   - Terms and restore purchases links

4. **Confirmation**
   - Success animation
   - Welcome to Premium message
   - "Explore premium features" CTA

### Emergency Anxiety Flow

1. **Quick Access**
   - 3D touch / long press app icon
   - Home screen emergency button
   - Shake gesture activation

2. **Immediate Relief**
   - Skip all setup questions
   - Start with 4-7-8 breathing
   - Large, clear visual guide
   - Calming background animation

3. **Stabilization**
   - After 2 minutes, check-in prompt
   - Option to continue or try different technique
   - Access to crisis resources if needed

4. **Follow-up**
   - Log the episode (optional)
   - Schedule check-in reminder
   - Suggest preventive session for tomorrow

## Animations & Transitions

### Screen Transitions
- **Push navigation**: 0.3s ease-in-out, slide from right
- **Modal presentation**: 0.25s ease-out, slide from bottom
- **Tab switches**: 0.2s ease-in-out, fade transition
- **Pull to dismiss**: Interactive spring physics

### Micro-interactions
- **Button press**: Scale to 0.95, 0.1s
- **Toggle switch**: 0.2s spring animation
- **Card selection**: