# **HabitFlow Mobile App Design Document**

## **1. Visual Design System**

### **Color Palette**

#### Primary Colors
- **Primary Blue**: #2563EB (Main brand color - trustworthy, professional)
- **Primary Dark**: #1E40AF (For emphasis and CTAs)
- **Primary Light**: #60A5FA (For highlights and accents)

#### Neutral Colors
- **Pure White**: #FFFFFF (Primary background)
- **Off White**: #FAFAFA (Secondary backgrounds)
- **Light Gray**: #F3F4F6 (Borders, dividers)
- **Medium Gray**: #9CA3AF (Inactive elements, placeholder text)
- **Dark Gray**: #4B5563 (Secondary text)
- **Near Black**: #111827 (Primary text)

#### Semantic Colors
- **Success Green**: #10B981 (Completed habits, streaks)
- **Warning Amber**: #F59E0B (Reminders, alerts)
- **Error Red**: #EF4444 (Missed habits, errors)
- **Info Blue**: #3B82F6 (Tips, information)

#### Dark Mode Palette
- **Background**: #0F172A
- **Surface**: #1E293B
- **Surface Elevated**: #334155
- **Text Primary**: #F1F5F9
- **Text Secondary**: #CBD5E1

### **Typography**

#### Font Family
- **Primary**: SF Pro Display (iOS) / Roboto (Android)
- **Fallback**: System default sans-serif

#### Type Scale
- **Heading 1**: 32px/40px - Bold (Main screens titles)
- **Heading 2**: 24px/32px - Semibold (Section headers)
- **Heading 3**: 20px/28px - Medium (Card titles)
- **Body Large**: 18px/28px - Regular (Primary content)
- **Body Regular**: 16px/24px - Regular (Standard text)
- **Body Small**: 14px/20px - Regular (Secondary information)
- **Caption**: 12px/16px - Regular (Timestamps, labels)

### **Spacing System**
- **Base unit**: 4px
- **Spacing scale**: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80px
- **Standard padding**: 16px (mobile screens)
- **Card padding**: 20px
- **Section spacing**: 24px

### **Layout Grid**
- **Columns**: 4 column grid on mobile
- **Gutter**: 16px
- **Margins**: 16px (left and right)
- **Safe area**: Respect device safe areas for notches and home indicators

### **Elevation & Shadows**

#### Shadow Levels
- **Level 0**: No shadow (flat elements)
- **Level 1**: 0px 1px 3px rgba(0,0,0,0.12) (Cards on surface)
- **Level 2**: 0px 4px 6px rgba(0,0,0,0.16) (Floating buttons)
- **Level 3**: 0px 10px 20px rgba(0,0,0,0.19) (Modals, dropdowns)

### **Border Radius**
- **Small**: 4px (Chips, tags)
- **Medium**: 8px (Buttons, input fields)
- **Large**: 12px (Cards, containers)
- **Extra Large**: 16px (Modals, sheets)
- **Full**: 9999px (Pills, avatars)

## **2. Component Design**

### **Buttons**

#### Primary Button
- **Background**: #2563EB
- **Text**: #FFFFFF, 16px Semibold
- **Height**: 48px
- **Border Radius**: 8px
- **Padding**: 16px horizontal
- **Pressed State**: #1E40AF with scale(0.98)
- **Disabled State**: #9CA3AF background, #E5E7EB text

#### Secondary Button
- **Background**: Transparent
- **Border**: 2px solid #2563EB
- **Text**: #2563EB, 16px Semibold
- **Height**: 48px
- **Border Radius**: 8px
- **Pressed State**: #EFF6FF background

#### Text Button
- **Background**: Transparent
- **Text**: #2563EB, 16px Medium
- **Height**: 40px
- **Pressed State**: #F3F4F6 background

#### Floating Action Button (FAB)
- **Size**: 56px diameter
- **Background**: #2563EB
- **Icon**: 24px, #FFFFFF
- **Shadow**: Level 2
- **Position**: Bottom right, 16px margins

### **Input Fields**

#### Text Input
- **Height**: 48px
- **Border**: 1px solid #E5E7EB
- **Border Radius**: 8px
- **Padding**: 12px horizontal
- **Focus State**: 2px solid #2563EB
- **Error State**: 2px solid #EF4444
- **Label**: 14px Medium, #4B5563, positioned above

#### Checkbox
- **Size**: 24px square
- **Border**: 2px solid #9CA3AF
- **Border Radius**: 4px
- **Checked**: #2563EB background with white checkmark
- **Animation**: Spring animation on check

### **Cards**

#### Habit Card
- **Background**: #FFFFFF
- **Border Radius**: 12px
- **Padding**: 20px
- **Shadow**: Level 1
- **Height**: Auto (content-based)
- **Margin**: 8px vertical spacing

#### Statistic Card
- **Background**: Linear gradient (#2563EB to #3B82F6)
- **Text**: #FFFFFF
- **Border Radius**: 16px
- **Padding**: 24px
- **Shadow**: Level 2

### **Navigation**

#### Bottom Navigation Bar
- **Height**: 64px + safe area
- **Background**: #FFFFFF with Level 1 shadow
- **Icons**: 24px, #9CA3AF (inactive), #2563EB (active)
- **Labels**: 12px, matching icon colors
- **Items**: 5 maximum

#### Top App Bar
- **Height**: 56px + status bar
- **Background**: #FFFFFF
- **Title**: 20px Semibold, centered or left-aligned
- **Icons**: 24px, #4B5563
- **Shadow**: Level 1 when scrolled

## **3. Screen Designs**

### **Splash Screen**
- **Duration**: 2 seconds
- **Background**: Gradient from #2563EB to #1E40AF
- **Logo**: Centered, white, 120px width
- **App Name**: Below logo, 24px white text
- **Loading Indicator**: White circular progress at bottom

### **Onboarding Flow**

#### Welcome Screen
- **Illustration**: Custom AI-themed illustration (240px height)
- **Title**: "Welcome to HabitFlow" - 32px Bold
- **Subtitle**: "Your AI-powered companion for daily success" - 18px Regular
- **Button**: "Get Started" - Primary button
- **Skip Link**: Top right, text button

#### Permission Screens
- **Notification Permission**: Icon + explanation + Allow/Skip buttons
- **AI Learning Opt-in**: Toggle with detailed explanation
- **Transition**: Slide left animation between screens

### **Authentication**

#### Sign Up Screen
- **Logo**: Top center, 80px
- **Form Fields**: Email, Password, Confirm Password
- **Terms Checkbox**: With links to terms and privacy
- **Social Sign Up**: Google and Apple buttons
- **Sign In Link**: Bottom center
- **Validation**: Real-time with inline error messages

#### Sign In Screen
- **Email/Password Fields**: With "Forgot Password?" link
- **Biometric Option**: Face ID/Touch ID button if available
- **Remember Me**: Checkbox option
- **Sign Up Link**: Bottom center

### **Main Dashboard**

#### Layout Structure
- **Header**: Greeting + Profile Avatar + Notification Bell
- **Today's Progress**: Circular progress chart (160px)
- **Quick Stats**: 3 cards showing streaks, completed, remaining
- **Habits List**: Scrollable list of today's habits
- **AI Insight Card**: Daily tip or suggestion
- **Bottom Navigation**: Home, Habits, Add, Analytics, Profile

#### Habit Item Design
- **Checkbox**: Left side, 32px
- **Habit Name**: 16px Semibold
- **Streak Badge**: If applicable, small pill with flame icon
- **Time**: Right side, if scheduled
- **Swipe Actions**: Edit (left), Delete (right)

### **Add/Edit Habit Screen**

#### Form Layout
- **Name Field**: Text input with 50 character limit
- **Icon Picker**: Grid of 40+ icons
- **Color Picker**: 12 preset colors
- **Frequency**: Daily/Weekly/Custom selector
- **Reminder**: Time picker with toggle
- **AI Suggestions**: Collapsible section with recommendations
- **Save Button**: Sticky bottom or floating

### **Analytics Screen**

#### Overview Section
- **Date Range Picker**: Week/Month/Year tabs
- **Completion Chart**: Line graph showing daily completion rate
- **Best Streak**: Card with number and date range
- **Total Completed**: Large number display

#### Habit Breakdown
- **List View**: Each habit with individual statistics
- **Heat Map**: Calendar view with intensity colors
- **AI Insights**: Personalized recommendations based on data

### **Profile Screen**

#### User Section
- **Avatar**: 80px circle with edit overlay
- **Name & Email**: Editable fields
- **Member Since**: Date display

#### Settings Sections
- **Subscription**: Current plan with upgrade button
- **Notifications**: Toggle list for different types
- **App Preferences**: Theme, language, units
- **Data & Privacy**: Export, delete account options
- **Support**: Help center, contact, FAQ
- **About**: Version, terms, privacy policy

## **4. Interactions & Animations**

### **Micro-Interactions**

#### Button Press
- **Scale**: 0.98 on press
- **Duration**: 100ms
- **Easing**: ease-out

#### Checkbox Toggle
- **Check Animation**: Path drawing, 300ms
- **Background Fill**: Fade in, 200ms
- **Haptic**: Light impact feedback

#### Card Selection
- **Elevation**: Increase to Level 2
- **Scale**: 1.02
- **Duration**: 200ms

### **Screen Transitions**

#### Navigation Transitions
- **Push**: Slide left, 300ms, ease-in-out
- **Pop**: Slide right, 300ms, ease-in-out
- **Modal**: Slide up from bottom, 400ms, spring damping
- **Tab Switch**: Fade, 200ms

#### Loading States
- **Skeleton Screens**: For content loading
- **Pull to Refresh**: Custom animation with logo
- **Infinite Scroll**: Bottom loader for lists

### **Gesture Controls**
- **Swipe to Delete**: Red background reveal, 300ms
- **Swipe to Edit**: Blue background reveal, 300ms
- **Pull to Refresh**: Elastic overscroll
- **Long Press**: Haptic feedback + context menu

## **5. Feature Specifications**

### **User Registration & Login**

#### Sign Up Flow
1. User taps "Get Started"
2. Enter email → Validate format in real-time
3. Create password → Show strength indicator
4. Confirm password → Match validation
5. Accept terms → Checkbox required
6. Tap "Create Account" → Loading state
7. Email verification → Send code
8. Enter code → 6-digit input
9. Success → Navigate to onboarding

#### Sign In Flow
1. Enter email/password
2. Optional: Enable biometric for future
3. Tap "Sign In" → Loading state
4. Success → Navigate to dashboard
5. Error → Show inline message

#### Password Reset
1. Tap "Forgot Password?"
2. Enter email → Send reset link
3. Check email → Deep link back to app
4. Enter new password
5. Success → Auto login

### **Habit Management**

#### Creating a Habit
1. Tap FAB (+) button
2. Enter habit name (required)
3. Select icon from grid
4. Choose color
5. Set frequency:
   - Daily (default)
   - Specific days of week
   - X times per week
6. Optional: Set reminder time
7. Optional: Add notes
8. Tap "Save" → Success animation
9. Return to dashboard

#### Completing a Habit
1. Tap checkbox → Fill animation
2. Streak counter updates
3. Progress ring animates
4. Optional: Add completion note
5. Undo option appears (5 seconds)

#### Editing a Habit
1. Long press or swipe left on habit
2. Tap "Edit" option
3. Modify fields
4. Tap "Update" → Save changes
5. Show success toast

#### Deleting a Habit
1. Swipe left fully or long press
2. Tap "Delete" option
3. Confirmation dialog appears
4. Tap "Delete" → Remove with animation
5. Show undo snackbar (5 seconds)

### **AI Features**

#### Routine Optimization
1. AI analyzes completion patterns
2. Suggests optimal times for habits
3. User reviews suggestions
4. Accept/Decline each suggestion
5. AI learns from decisions

#### Smart Notifications
1. AI determines best reminder times
2. Adapts based on completion history
3. Reduces notifications for consistent habits
4. Increases for struggling habits

#### Insights Generation
1. Weekly analysis runs automatically
2. Generates 3-5 insights
3. Display as cards on dashboard
4. Tap for detailed view
5. Option to dismiss or save

### **Analytics & Progress**

#### Viewing Statistics
1. Navigate to Analytics tab
2. Default shows current week
3. Swipe or tap to change time period
4. Tap any metric for details
5. Export option in top right

#### Streak Tracking
1. Automatic calculation
2. Display current and best streaks
3. Visual flame icon for active streaks
4. Freeze option for vacation mode
5. Share achievement option

### **Settings & Preferences**

#### Notification Management
1. Navigate to Profile → Notifications
2. Toggle master switch
3. Individual toggles for:
   - Daily reminders
   - Weekly summaries
   - Achievements
   - AI insights
4. Set quiet hours

#### Theme Selection
1. Profile → Appearance
2. Options: Light/Dark/Auto
3. Preview before applying
4. Saves automatically

#### Data Export
1. Profile → Data & Privacy
2. Tap "Export Data"
3. Choose format (CSV/PDF)
4. Select date range
5. Share or save to device

## **6. Accessibility**

### **Visual Accessibility**
- **Color Contrast**: Minimum 4.5:1 for normal text, 3:1 for large text
- **Text Scaling**: Support 85% to 200% system scaling
- **Color Blind Mode**: Alternative color schemes available
- **Focus Indicators**: Visible keyboard navigation indicators

### **Screen Reader Support**
- **Labels**: All interactive elements have descriptive labels
- **Hints**: Additional context for complex interactions
- **Announcements**: State changes announced
- **Grouping**: Logical content grouping

### **Motor Accessibility**
- **Touch Targets**: Minimum 44x44pt
- **Gesture Alternatives**: All gestures have tap alternatives
- **Time Limits**: Adjustable or removable
- **Confirmation**: Destructive actions require confirmation

## **7. Error States & Empty States**

### **Error States**

#### Network Error
- **Icon**: Wi-Fi off icon
- **Message**: "No internet connection"
- **Action**: "Retry" button
- **Offline Mode**: Limited functionality indicator

#### Loading Error
- **Icon**: Alert circle
- **Message**: Specific error description
- **Action**: "Try Again" button
- **Support Link**: "Get Help" option

### **Empty States**

#### No Habits
- **Illustration**: Custom friendly graphic
- **Message**: "Start your journey"
- **Description**: "Create your first habit to begin"
- **Action**: "Add Habit" button

#### No Data
- **Icon**: Chart icon
- **Message**: "No data yet"
- **Description**: "Complete habits to see analytics"

## **8. Platform-Specific Considerations**

### **iOS Specific**
- **Navigation**: iOS-style back swipe gesture
- **Haptics**: Use iOS Haptic Engine
- **Face ID**: Integrated authentication
- **Widgets**: iOS 14+ widget support
- **App Clips**: Quick habit check-in

###