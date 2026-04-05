# MindfulBreath Mobile App - Complete Expo Project Code

## Project Structure
```
mindfulbreath/
├── App.js
├── package.json
├── app.json
├── babel.config.js
├── assets/
│   └── fonts/
│       ├── Inter-Regular.ttf
│       ├── Inter-Medium.ttf
│       ├── Inter-SemiBold.ttf
│       └── Inter-Bold.ttf
├── components/
│   ├── ErrorBoundary.js
│   ├── NetworkStatus.js
│   └── LoadingOverlay.js
├── context/
│   ├── AuthContext.js
│   └── ThemeContext.js
├── navigation/
│   └── MainTabNavigator.js
├── screens/
│   ├── LoginScreen.js
│   ├── OnboardingFlow.js
│   ├── HomeScreen.js
│   ├── ProfileScreen.js
│   ├── SettingsScreen.js
│   ├── SessionScreen.js
│   └── PremiumScreen.js
└── utils/
    ├── validators.js
    └── constants.js
```

## package.json
```json
{
  "name": "mindfulbreath",
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
    "react": "18.2.0",
    "react-native": "0.72.6",
    "@react-navigation/native": "^6.1.9",
    "@react-navigation/bottom-tabs": "^6.5.11",
    "@react-navigation/stack": "^6.3.20",
    "react-native-screens": "~3.22.0",
    "react-native-safe-area-context": "4.6.3",
    "expo-linear-gradient": "~12.3.0",
    "expo-haptics": "~12.4.0",
    "expo-av": "~13.4.1",
    "react-native-gesture-handler": "~2.12.0",
    "react-native-reanimated": "~3.3.0",
    "@react-native-async-storage/async-storage": "1.18.2",
    "react-native-svg": "13.9.0",
    "expo-font": "~11.4.0",
    "@expo/vector-icons": "^13.0.0",
    "@react-native-community/netinfo": "9.3.10"
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
    "name": "MindfulBreath",
    "slug": "mindfulbreath",
    "version": "1.0.0",
    "orientation": "portrait",
    "icon": "./assets/icon.png",
    "userInterfaceStyle": "light",
    "splash": {
      "image": "./assets/splash.png",
      "resizeMode": "contain",
      "backgroundColor": "#4A90E2"
    },
    "assetBundlePatterns": [
      "**/*"
    ],
    "ios": {
      "supportsTablet": true,
      "bundleIdentifier": "com.mindfulbreath.app"
    },
    "android": {
      "adaptiveIcon": {
        "foregroundImage": "./assets/adaptive-icon.png",
        "backgroundColor": "#4A90E2"
      },
      "package": "com.mindfulbreath.app"
    },
    "web": {
      "favicon": "./assets/favicon.png"
    }
  }
}
```

## babel.config.js
```javascript
module.exports = function(api) {
  api.cache(true);
  return {
    presets: ['babel-preset-expo'],
    plugins: ['react-native-reanimated/plugin'],
  };
};
```

## App.js
```javascript
import React, { useState, useEffect } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { StatusBar } from 'expo-status-bar';
import * as Font from 'expo-font';
import { View, ActivityIndicator } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';
import NetInfo from '@react-native-community/netinfo';

// Import screens
import LoginScreen from './screens/LoginScreen';
import OnboardingFlow from './screens/OnboardingFlow';
import MainTabNavigator from './navigation/MainTabNavigator';
import SettingsScreen from './screens/SettingsScreen';
import SessionScreen from './screens/SessionScreen';
import PremiumScreen from './screens/PremiumScreen';

// Import context and components
import { AuthProvider } from './context/AuthContext';
import { ThemeProvider } from './context/ThemeContext';
import ErrorBoundary from './components/ErrorBoundary';
import NetworkStatus from './components/NetworkStatus';
import { STORAGE_KEYS } from './utils/constants';

const Stack = createStackNavigator();

export default function App() {
  const [isLoading, setIsLoading] = useState(true);
  const [isFirstLaunch, setIsFirstLaunch] = useState(false);
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [isConnected, setIsConnected] = useState(true);

  useEffect(() => {
    let unsubscribe;

    async function loadApp() {
      try {
        // Load fonts with fallback
        try {
          await Font.loadAsync({
            'Inter-Regular': require('./assets/fonts/Inter-Regular.ttf'),
            'Inter-Medium': require('./assets/fonts/Inter-Medium.ttf'),
            'Inter-SemiBold': require('./assets/fonts/Inter-SemiBold.ttf'),
            'Inter-Bold': require('./assets/fonts/Inter-Bold.ttf'),
          });
        } catch (fontError) {
          console.warn('Using system fonts as fallback');
        }

        // Check if first launch
        const hasLaunched = await AsyncStorage.getItem(STORAGE_KEYS.HAS_LAUNCHED);
        if (hasLaunched === null) {
          setIsFirstLaunch(true);
        }

        // Check authentication
        const token = await AsyncStorage.getItem(STORAGE_KEYS.USER_TOKEN);
        if (token) {
          setIsAuthenticated(true);
        }

        // Setup network monitoring
        unsubscribe = NetInfo.addEventListener(state => {
          setIsConnected(state.isConnected ?? true);
        });
      } catch (error) {
        console.error('Error loading app:', error);
      } finally {
        setIsLoading(false);
      }
    }

    loadApp();

    return () => {
      if (unsubscribe) {
        unsubscribe();
      }
    };
  }, []);

  if (isLoading) {
    return (
      <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center', backgroundColor: '#F7FAFC' }}>
        <ActivityIndicator size="large" color="#4A90E2" />
      </View>
    );
  }

  return (
    <ErrorBoundary>
      <ThemeProvider>
        <AuthProvider>
          <NavigationContainer>
            <StatusBar style="auto" />
            {!isConnected && <NetworkStatus />}
            <Stack.Navigator screenOptions={{ headerShown: false }}>
              {isFirstLaunch && !isAuthenticated ? (
                <Stack.Screen name="Onboarding" component={OnboardingFlow} />
              ) : !isAuthenticated ? (
                <>
                  <Stack.Screen name="Login" component={LoginScreen} />
                  <Stack.Screen name="Onboarding" component={OnboardingFlow} />
                </>
              ) : (
                <>
                  <Stack.Screen name="Main" component={MainTabNavigator} />
                  <Stack.Screen name="Settings" component={SettingsScreen} />
                  <Stack.Screen name="Session" component={SessionScreen} />
                  <Stack.Screen name="Premium" component={PremiumScreen} />
                </>
              )}
            </Stack.Navigator>
          </NavigationContainer>
        </AuthProvider>
      </ThemeProvider>
    </ErrorBoundary>
  );
}
```

## utils/constants.js
```javascript
export const STORAGE_KEYS = {
  HAS_LAUNCHED: '@MindfulBreath:hasLaunched',
  USER_TOKEN: '@MindfulBreath:userToken',
  USER_DATA: '@MindfulBreath:userData',
  SETTINGS: '@MindfulBreath:settings',
  SESSION_HISTORY: '@MindfulBreath:sessionHistory',
};

export const BREATHING_EXERCISES = {
  BOX: {
    id: 'box',
    name: 'Box Breathing',
    duration: 240,
    inhale: 4,
    hold1: 4,
    exhale: 4,
    hold2: 4,
  },
  CALM: {
    id: 'calm',
    name: '4-7-8 Breathing',
    duration: 180,
    inhale: 4,
    hold1: 7,
    exhale: 8,
    hold2: 0,
  },
  ENERGIZE: {
    id: 'energize',
    name: 'Energizing Breath',
    duration: 120,
    inhale: 6,
    hold1: 0,
    exhale: 2,
    hold2: 0,
  },
};
```

## utils/validators.js
```javascript
export const validateEmail = (email) => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
};

export const validatePassword = (password) => {
  return {
    isValid: password.length >= 8,
    hasMinLength: password.length >= 8,
    hasUpperCase: /[A-Z]/.test(password),
    hasLowerCase: /[a-z]/.test(password),
    hasNumber: /[0-9]/.test(password),
    hasSpecialChar: /[!@#$%^&*]/.test(password),
  };
};

export const sanitizeInput = (input) => {
  return input.trim().replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '');
};
```

## components/ErrorBoundary.js
```javascript
import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { Ionicons } from '@expo/vector-icons';

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Error caught by boundary:', error, errorInfo);
  }

  handleReset = () => {
    this.setState({ hasError: false, error: null });
  };

  render() {
    if (this.state.hasError) {
      return (
        <View style={styles.container}>
          <Ionicons name="warning-outline" size={64} color="#FC8181" />
          <Text style={styles.title}>Oops! Something went wrong</Text>
          <Text style={styles.message}>
            We're sorry for the inconvenience. Please try restarting the app.
          </Text>
          <TouchableOpacity 
            style={styles.button} 
            onPress={this.handleReset}
            accessible={true}
            accessibilityLabel="Try again button"
            accessibilityHint="Tap to reload the app"
            accessibilityRole="button"
          >
            <Text style={styles.buttonText}>Try Again</Text>
          </TouchableOpacity>
        </View>
      );
    }

    return this.props.children;
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
    backgroundColor: '#F7FAFC',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#2D3748',
    marginTop: 16,
    marginBottom: 8,
  },
  message: {
    fontSize: 16,
    color: '#718096',
    textAlign: 'center',
    marginBottom: 24,
  },
  button: {
    backgroundColor: '#4A90E2',
    paddingHorizontal: 32,
    paddingVertical: 12,
    borderRadius: 8,
  },
  buttonText: {
    color: 'white',
    fontSize: 16,
    fontWeight: '600',
  },
});

export default ErrorBoundary;
```

## components/NetworkStatus.js
```javascript
import React, { useEffect, useRef } from 'react';
import { View, Text, StyleSheet, Animated } from 'react-native';
import { Ionicons } from '@expo/vector-icons';

const NetworkStatus = () => {
  const slideAnim = useRef(new Animated.Value(-100)).current;

  useEffect(() => {
    Animated.spring(slideAnim, {
      toValue: 0,
      useNativeDriver: true,
      tension: 50,
      friction: 8,
    }).start();
  }, []);

  return (
    <Animated.View 
      style={[
        styles.container,
        { transform: [{ translateY: slideAnim }] }
      ]}
    >
      <Ionicons name="wifi-outline" size={20} color="#FFF" />
      <Text style={styles.text}>No Internet Connection</Text>
    </Animated.View>
  );
};

const styles = StyleSheet.create({
  container: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    backgroundColor: '#FC8181',
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingTop: 50,
    paddingBottom: 10,
    zIndex: 1000,
  },
  text: {
    color: '#FFF',
    fontSize: 14,
    fontWeight: '500',
    marginLeft: 8,
  },
});

export default NetworkStatus;
```

## components/LoadingOverlay.js
```javascript
import React from 'react';
import { View, ActivityIndicator, StyleSheet, Text } from 'react-native';

const LoadingOverlay = ({ message = 'Loading...' }) => {
  return (
    <View style={styles.container}>
      <View style={styles.content}>
        <ActivityIndicator size="large" color="#4A90E2" />
        <Text style={styles.text}>{message}</Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    ...StyleSheet.absoluteFillObject,
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
    justifyContent: 'center',
    alignItems: 'center',
    zIndex: 9999,
  },
  content: {
    backgroundColor: 'white',
    