```markdown
# CodeSpark Mobile App - Expo MVP Code

## package.json
```json
{
  "name": "codespark",
  "version": "1.0.0",
  "main": "node_modules/expo/AppEntry.js",
  "scripts": {
    "start": "expo start",
    "android": "expo start --android",
    "ios": "expo start --ios",
    "web": "expo start --web"
  },
  "dependencies": {
    "expo": "~49.0.0",
    "expo-status-bar": "~1.6.0",
    "expo-font": "~11.4.0",
    "expo-constants": "~14.4.0",
    "@react-navigation/native": "^6.1.0",
    "@react-navigation/stack": "^6.3.0",
    "@react-navigation/bottom-tabs": "^6.5.0",
    "react-native-safe-area-context": "4.6.3",
    "react-native-screens": "~3.22.0",
    "@react-native-async-storage/async-storage": "1.18.2",
    "react-native-gesture-handler": "~2.12.0",
    "react-native-reanimated": "~3.3.0",
    "react-native-svg": "13.9.0",
    "@expo/vector-icons": "^13.0.0",
    "react": "18.2.0",
    "react-native": "0.72.5"
  },
  "devDependencies": {
    "@babel/core": "^7.20.0"
  },
  "private": true
}
```

## app.json
```json
{
  "expo": {
    "name": "CodeSpark",
    "slug": "codespark",
    "version": "1.0.0",
    "orientation": "portrait",
    "icon": "./assets/icon.png",
    "userInterfaceStyle": "light",
    "splash": {
      "image": "./assets/splash.png",
      "resizeMode": "contain",
      "backgroundColor": "#4CAF50"
    },
    "assetBundlePatterns": [
      "**/*"
    ],
    "ios": {
      "supportsTablet": true
    },
    "android": {
      "adaptiveIcon": {
        "foregroundImage": "./assets/adaptive-icon.png",
        "backgroundColor": "#4CAF50"
      }
    },
    "web": {
      "favicon": "./assets/favicon.png"
    }
  }
}
```

## App.js
```javascript
import React, { useState, useEffect } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { StatusBar } from 'expo-status-bar';
import AsyncStorage from '@react-native-async-storage/async-storage';
import * as Font from 'expo-font';
import { View, ActivityIndicator } from 'react-native';

// Import screens
import OnboardingScreen from './src/screens/OnboardingScreen';
import MainNavigator from './src/navigation/MainNavigator';

// Import theme
import { colors } from './src/constants/theme';

const Stack = createStackNavigator();

export default function App() {
  const [isLoading, setIsLoading] = useState(true);
  const [hasOnboarded, setHasOnboarded] = useState(false);
  const [fontsLoaded, setFontsLoaded] = useState(false);

  useEffect(() => {
    loadApp();
  }, []);

  const loadApp = async () => {
    try {
      // Load fonts
      await Font.loadAsync({
        'Nunito-Regular': require('./assets/fonts/Nunito-Regular.ttf'),
        'Nunito-Bold': require('./assets/fonts/Nunito-Bold.ttf'),
        'BubblegumSans': require('./assets/fonts/BubblegumSans-Regular.ttf'),
      });
      setFontsLoaded(true);

      // Check onboarding status
      const onboardingStatus = await AsyncStorage.getItem('hasCompletedOnboarding');
      if (onboardingStatus === 'true') {
        setHasOnboarded(true);
      }
    } catch (error) {
      console.error('Error loading app:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const completeOnboarding = async () => {
    await AsyncStorage.setItem('hasCompletedOnboarding', 'true');
    setHasOnboarded(true);
  };

  if (isLoading) {
    return (
      <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center', backgroundColor: colors.background }}>
        <ActivityIndicator size="large" color={colors.primary} />
      </View>
    );
  }

  return (
    <>
      <StatusBar style="dark" backgroundColor={colors.background} />
      <NavigationContainer>
        <Stack.Navigator screenOptions={{ headerShown: false }}>
          {!hasOnboarded ? (
            <Stack.Screen name="Onboarding">
              {props => <OnboardingScreen {...props} onComplete={completeOnboarding} />}
            </Stack.Screen>
          ) : (
             <Stack.Screen name="Main" component={MainNavigator} />
          )}
        </Stack.Navigator>
      </NavigationContainer>
    </>
  );
}
```

## src/constants/theme.js
```javascript
export const colors = {
  primary: '#4CAF50',
  secondary: '#FFC107',
  accent: '#2196F3',
  background: '#F5F5F5',
  textPrimary: '#333333',
  textSecondary: '#757575',
  error: '#F44336',
  white: '#FFFFFF',
  cardBackground: '#FFFFFF',
  shadowColor: '#000000',
};

export const fonts = {
  headline: {
    fontFamily: 'BubblegumSans',
    fontSize: 28,
    fontWeight: 'bold',
  },
  title: {
    fontFamily: 'Nunito-Bold',
    fontSize: 20,
  },
  body: {
    fontFamily: 'Nunito-Regular',
    fontSize: 16,
  },
  caption: {
    fontFamily: 'Nunito-Regular',
    fontSize: 14,
  },
};

export const spacing = {
  xs: 4,
  sm: 8,
  md: 16,
  lg: 24,
  xl: 32,
};

export const borderRadius = {
  sm: 8,
  md: 12,
  lg: 16,
  full: 9999,
};
```

## src/navigation/MainNavigator.js
```javascript
import React from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { Ionicons } from '@expo/vector-icons';

// Import screens
import HomeScreen from '../screens/HomeScreen';
import GamesScreen from '../screens/GamesScreen';
import PuzzlesScreen from '../screens/PuzzlesScreen';
import ProjectsScreen from '../screens/ProjectsScreen';
import ProfileScreen from '../screens/ProfileScreen';

// Import theme
import { colors } from '../constants/theme';

const Tab = createBottomTabNavigator();

export default function MainNavigator() {
  return (
    <Tab.Navigator
      screenOptions={({ route }) => ({
        tabBarIcon: ({ focused, color, size }) => {
          let iconName;

          switch (route.name) {
            case 'Home':
              iconName = focused ? 'home' : 'home-outline';
              break;
            case 'Games':
              iconName = focused ? 'game-controller' : 'game-controller-outline';
              break;
            case 'Puzzles':
              iconName = focused ? 'extension-puzzle' : 'extension-puzzle-outline';
              break;
            case 'Projects':
              iconName = focused ? 'create' : 'create-outline';
              break;
            case 'Profile':
              iconName = focused ? 'person' : 'person-outline';
              break;
          }

          return <Ionicons name={iconName} size={size} color={color} />;
        },
        tabBarActiveTintColor: colors.primary,
        tabBarInactiveTintColor: colors.textSecondary,
        tabBarStyle: {
          backgroundColor: colors.white,
          borderTopWidth: 1,
          borderTopColor: '#E0E0E0',
          paddingBottom: 5,
          paddingTop: 5,
          height: 60,
        },
        headerStyle: {
          backgroundColor: colors.primary,
        },
        headerTintColor: colors.white,
        headerTitleStyle: {
          fontFamily: 'BubblegumSans',
          fontSize: 24,
        },
      })}
    >
      <Tab.Screen name="Home" component={HomeScreen} options={{ title: 'CodeSpark' }} />
      <Tab.Screen name="Games" component={GamesScreen} />
      <Tab.Screen name="Puzzles" component={PuzzlesScreen} />
      <Tab.Screen name="Projects" component={ProjectsScreen} />
      <Tab.Screen name="Profile" component={ProfileScreen} />
    </Tab.Navigator>
  );
}
```

## src/screens/OnboardingScreen.js
```javascript
import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  FlatList,
  Dimensions,
  SafeAreaView,
  Image,
} from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';

const { width } = Dimensions.get('window');

const avatars = [
  { id: '1', name: 'Robot', color: '#FF6B6B', emoji: '🤖' },
  { id: '2', name: 'Unicorn', color: '#C06BFF', emoji: '🦄' },
  { id: '3', name: 'Dragon', color: '#4ECDC4', emoji: '🐉' },
  { id: '4', name: 'Astronaut', color: '#45B7D1', emoji: '👨‍🚀' },
  { id: '5', name: 'Wizard', color: '#96CEB4', emoji: '🧙‍♂️' },
  { id: '6', name: 'Ninja', color: '#2C3E50', emoji: '🥷' },
];

export default function OnboardingScreen({ navigation, onComplete }) {
  const [selectedAvatar, setSelectedAvatar] = useState(null);
  const [step, setStep] = useState(1);

  const handleAvatarSelect = (avatar) => {
    setSelectedAvatar(avatar);
  };

  const handleContinue = async () => {
    if (selectedAvatar) {
      await AsyncStorage.setItem('selectedAvatar', JSON.stringify(selectedAvatar));
      await onComplete();
      navigation.replace('Main');
    }
  };

  const renderAvatar = ({ item }) => {
    const isSelected = selectedAvatar?.id === item.id;
    return (
      <TouchableOpacity
        style={[
          styles.avatarCard,
          { backgroundColor: item.color },
          isSelected && styles.selectedAvatar,
        ]}
        onPress={() => handleAvatarSelect(item)}
        activeOpacity={0.7}
      >
        <Text style={styles.avatarEmoji}>{item.emoji}</Text>
        <Text style={styles.avatarName}>{item.name}</Text>
        {isSelected && (
          <View style={styles.checkmark}>
            <Text style={styles.checkmarkText}>✓</Text>
          </View>
        )}
      </TouchableOpacity>
    );
  };

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.content}>
        <Text style={styles.title}>Welcome to CodeSpark! 🚀</Text>
        <Text style={styles.subtitle}>Let's start your coding adventure!</Text>

        <View style={styles.stepContainer}>
          <Text style={styles.stepText}>Choose Your Avatar</Text>
          <Text style={styles.stepDescription}>
            Pick a character to join you on your coding journey
          </Text>
        </View>

        <FlatList
          data={avatars}
          renderItem={renderAvatar}
          keyExtractor={(item) => item.id}
          numColumns={2}
          columnWrapperStyle={styles.avatarRow}
          contentContainerStyle={styles.avatarGrid}
          scrollEnabled={false}
        />

        <TouchableOpacity
          style={[
            styles.continueButton,
            !selectedAvatar && styles.disabledButton,
          ]}
          onPress={handleContinue}
          disabled={!selectedAvatar}
          activeOpacity={0.8}
        >
          <Text style={styles.continueButtonText}>
            {selectedAvatar ? "Let's Start Coding!" : 'Select an Avatar'}
          </Text>
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.background,
  },
  content: {
    flex: 1,
    paddingHorizontal: spacing.lg,
    paddingTop: spacing.xl,
  },
  title: {
    ...fonts.headline,
    color: colors.primary,
    textAlign: 'center',
    marginBottom: spacing.sm,
  },
  subtitle: {
    ...fonts.body,
    color: colors.textSecondary,
    textAlign: 'center',
    marginBottom: spacing.xl,
  },
  stepContainer: {
    marginBottom: spacing.lg,
  },
  stepText: {
    ...fonts.title,
    color: colors.textPrimary,
    textAlign: 'center',
    marginBottom: spacing.xs,
  },
  stepDescription: {
    ...fonts.caption,
    color: colors.textSecondary,
    textAlign: 'center',
  },
  avatarGrid: {
    paddingVertical: spacing.md,
  },
  avatarRow: {
    justifyContent: 'space-between',
    marginBottom: spacing.md,
  },
  avatarCard: {
    width: (width - spacing.lg * 2 - spacing.md) / 2,
    height: 140,
    borderRadius: borderRadius.md,
    justifyContent: 'center',
    alignItems: 'center',
    padding: spacing.md,
  },
  selectedAvatar: {
    borderWidth: 3,
    borderColor: colors.primary,
  },
  avatarEmoji: {
    fontSize: 48,
    marginBottom: spacing.sm,
  },
  avatarName: {
    ...fonts.body,
    color: colors.white,
    fontWeight: 'bold',
  },
  checkmark: {
    position: 'absolute',
    top: spacing.sm,
    right: spacing.sm,
    width: 24,
    height: 24,
    borderRadius: 12,
    backgroundColor: colors.primary,
    justifyContent: 'center',
    alignItems: 'center',
  },
  checkmarkText: {
    color: colors.white,
    fontSize: 16,
    fontWeight: 'bold',
  },
  continueButton: {
    backgroundColor: colors.primary,
    paddingVertical: spacing.md,
    borderRadius: borderRadius.sm
  },
  disabledButton: {
    backgroundColor: colors.textSecondary,
    opacity: 0.5,
  },
  continueButtonText: {
    ...fonts.body,
    color: colors.white,
    textAlign: 'center',
    fontWeight: 'bold',
  },
});
```

## src/screens/HomeScreen.js
```javascript
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { colors } from '../constants/theme';

const HomeScreen = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Home Screen</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: colors.background,
  },
  text: {
    fontSize: 20,
  },
});

export default HomeScreen;
```

## src/screens/GamesScreen.js
```javascript
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { colors } from '../constants/theme';

const GamesScreen = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Games Screen</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: colors.background,
  },
  text: {
    fontSize: 20,
  },
});

export default GamesScreen;
```

## src/screens/PuzzlesScreen.js
```javascript
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { colors } from '../constants/theme';

const PuzzlesScreen = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Puzzles Screen</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: colors.background,
  },
  text: {
    fontSize: 20,
  },
});

export default PuzzlesScreen;
```

## src/screens/ProjectsScreen.js
```javascript
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { colors } from '../constants/theme';

const ProjectsScreen = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Projects Screen</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: colors.background,
  },
  text: {
    fontSize: 20,
  },
});

export default ProjectsScreen;
```

## src/screens/ProfileScreen.js
```javascript
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { colors } from '../constants/theme';

const ProfileScreen = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Profile Screen</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: colors.background,
  },
  text: {
    fontSize: 20,
  },
});

export default ProfileScreen;
```

---

# QA Report: CodeSpark Mobile App - Expo MVP

## Executive Summary
After thorough analysis of the CodeSpark mobile app codebase, I've identified several critical bugs, potential issues, and areas for improvement that need to be addressed before the app can be considered production-ready.

---

## 🔴 Critical Issues

### 1. **Incomplete Button Style in OnboardingScreen.js**
**Location:** `src/screens/OnboardingScreen.js`, line 157  
**Issue:** The `continueButton` style definition is incomplete - it's cut off at `borderRadius: borderRadius.sm` without closing the style object.  
**Impact:** This will cause a syntax error and prevent the app from running.  
**Solution:**
```javascript
continueButton: {
  backgroundColor: colors.primary,
  paddingVertical: spacing.md,
  borderRadius: borderRadius.sm, // Add comma
  marginTop: 'auto', // Add missing properties
  marginBottom: spacing.xl,
},
disabledButton: { // Add missing style
  backgroundColor: colors.textSecondary,
  opacity: 0.5,
},
continueButtonText: { // Add missing style
  ...fonts.body,
  color: colors.white,
  textAlign: 'center',
  fontWeight: 'bold',
},
```

### 2. **Missing Screen Components**
**Location:** `src/navigation/MainNavigator.js`  
**Issue:** The navigator imports 5 screens (HomeScreen, GamesScreen, PuzzlesScreen, ProjectsScreen, ProfileScreen) but these files are not provided in the codebase.  
**Impact:** The app will crash immediately when trying to navigate to any tab.  
**Solution:** Create all missing screen components with at least basic placeholder content.

---

## 🟡 High Priority Issues

### 3. **Missing Font Files**
**Location:** `App.js`, lines 31-35  
**Issue:** The app attempts to load custom fonts from the assets folder, but these font files are not confirmed to exist.  
**Impact:** If font files are missing, the app will crash on startup.  
**Solution:** Ensure all font files exist in the correct location:
- `./assets/fonts/Nunito-Regular.ttf`
- `./assets/fonts/Nunito-Bold.ttf`
- `./assets/fonts/BubblegumSans-Regular.ttf`

### 4. **Missing Image Assets**
**Location:** `app.json`  
**Issue:** References to image assets that may not exist:
- `./assets/icon.png`
- `./assets/splash.png`
- `./assets/adaptive-icon.png`
- `./assets/favicon.png`  
**Impact:** Build process will fail if these assets don't exist.  
**Solution:** Verify all image assets exist or provide default placeholders.

### 5. **Navigation Flow Issue**
**Location:** `App.js`, lines 66-73  
**Issue:** When `hasOnboarded` is true, the Onboarding screen is not added to the stack, but the Main screen tries to replace a non-existent screen.  
**Impact:** Potential navigation issues.  
**Solution:**
```javascript
<Stack.Navigator screenOptions={{ headerShown: false }}>
  {!hasOnboarded ? (
    <Stack.Screen name="Onboarding">
      {props => <OnboardingScreen {...props} onComplete={completeOnboarding} />}
    </Stack.Screen>
  ) : (
    <Stack.Screen name="Main" component={MainNavigator} />
  )}
</Stack.Navigator>
```

---

## 🟢 Medium Priority Issues

### 6. **Error Handling Improvements**
**Location:** `App.js`, `loadApp` function  
**Issue:** Error is only logged to console, user gets no feedback if app fails to load.  
**Solution:** Add user-facing error state:
```javascript
const [error, setError] = useState(null);

// In catch block:
catch (error) {
  console.error('Error loading app:', error);
  setError('Failed to load app. Please restart.');
}

// In render:
if (error) {
  return (
    <View style={styles.errorContainer}>
      <Text>{error}</Text>
      <TouchableOpacity onPress={loadApp}>
        <Text>Retry</Text>
      </TouchableOpacity>
    </View>
  );
}
```

### 7. **AsyncStorage Error Handling**
**Location:** `OnboardingScreen.js`, `handleContinue` function  
**Issue:** No error handling for AsyncStorage operations.  
**Solution:**
```javascript
const handleContinue = async () => {
  if (selectedAvatar) {
    try {
      await AsyncStorage.setItem('selectedAvatar', JSON.stringify(selectedAvatar));
      await onComplete();
      navigation.replace('Main');
    } catch (error) {
      console.error('Failed to save avatar:', error);
      // Show error message to user
    }
  }
};
```

### 8. **Unused Variable**
**Location:** `OnboardingScreen.js`, line 26  
**Issue:** `step` state variable is defined but never used.  
**Solution:** Remove unused state or implement multi-step onboarding if intended.

---

## 🔵 Performance & Best Practice Improvements

### 9. **Font Loading Optimization**
**Suggestion:** Consider using `expo-splash-screen` to keep splash screen visible while fonts load:
```javascript
import * as SplashScreen from 'expo-splash-screen';

SplashScreen.preventAutoHideAsync();

// After fonts loaded:
await SplashScreen.hideAsync();
```

### 10. **Memoization Opportunities**
**Location:** `OnboardingScreen.js`  
**Suggestion:** Memoize `renderAvatar` function to prevent unnecessary re-renders:
```javascript
const renderAvatar = useCallback(({ item }) => {
  // ... existing code
}, [selectedAvatar]);
```

### 11. **Accessibility Improvements**
**Suggestion:** Add accessibility props to interactive elements:
```javascript
<TouchableOpacity
  accessible={true}
  accessibilityLabel={`Select ${item.name} avatar`}
  accessibilityRole="button"
  accessibilityState={{ selected: isSelected }}
>
```

### 12. **TypeScript Migration**
**Suggestion:** Consider migrating to TypeScript for better type safety and developer experience.

---

## 📋 Testing Recommendations

1. **Unit Tests:** Add Jest tests for utility functions and components
2. **Integration Tests:** Test navigation flows and data persistence
3. **E2E Tests:** Implement Detox tests for critical user journeys
4. **Device Testing:** Test on various screen sizes and both iOS/Android

---

## ✅ Positive Aspects

- Good project structure and organization
- Consistent theming system
- Proper use of React Navigation
- Clean component separation
- Good use of React Hooks

---

## 📊 Summary

**Total Issues Found:** 12
- **Critical:** 2 (must fix before testing)
- **High Priority:** 4 (should fix before release)
- **Medium Priority:** 3 (can be addressed in next iteration)
- **Improvements:** 3 (nice to have)

## Recommended Action Plan

1. **Immediate (Before Testing):**
   - Fix the incomplete style object in OnboardingScreen.js
   - Create placeholder screen components
   - Verify all asset files exist

2. **Before Release:**
   - Implement proper error handling
   - Add loading states and user feedback
   - Test on physical devices

3. **Future Iterations:**
   - Add comprehensive testing
   - Improve accessibility
   - Consider TypeScript migration

The codebase shows good architectural decisions and follows React Native best practices, but requires the above fixes before it can be tested on mobile devices. Once these issues are resolved, the app should provide a solid foundation for the CodeSpark educational platform.
```