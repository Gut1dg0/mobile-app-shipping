```markdown
# SoundSleep App - Expo MVP Code

## package.json
```json
{
  "name": "soundsleep-app",
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
    "expo-secure-store": "~12.3.1",
    "expo-image": "~1.3.5",
    "react": "18.2.0",
    "react-native": "0.72.6",
    "react-native-safe-area-context": "4.6.3",
    "react-native-screens": "~3.22.0",
    "@react-navigation/native": "^6.1.7",
    "@react-navigation/native-stack": "^6.9.13",
    "@react-navigation/bottom-tabs": "^6.5.8",
    "react-native-vector-icons": "^10.0.0",
    "@expo/vector-icons": "^13.0.0"
  },
  "devDependencies": {
    "@babel/core": "^7.20.0"
  },
  "private": true
}
```

## App.js
```javascript
import React, { useState, useEffect } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import { StatusBar } from 'expo-status-bar';
import * as Font from 'expo-font';
import * as SecureStore from 'expo-secure-store';
import { View, ActivityIndicator } from 'react-native';

import LoginScreen from './src/screens/LoginScreen';
import SignUpScreen from './src/screens/SignUpScreen';
import MainTabNavigator from './src/navigation/MainTabNavigator';
import { colors } from './src/constants/colors';

const Stack = createNativeStackNavigator();

export default function App() {
  const [isLoading, setIsLoading] = useState(true);
  const [userToken, setUserToken] = useState(null);
  const [fontsLoaded, setFontsLoaded] = useState(false);

  useEffect(() => {
    loadResources();
  }, []);

  const loadResources = async () => {
    try {
      // Load fonts
      await Font.loadAsync({
        'Montserrat-SemiBold': require('./assets/fonts/Montserrat-SemiBold.ttf'),
        'OpenSans-Regular': require('./assets/fonts/OpenSans-Regular.ttf'),
      });
      setFontsLoaded(true);

      // Check for stored token
      const token = await SecureStore.getItemAsync('userToken');
      if (token) {
        setUserToken(token);
      }
    } catch (error) {
      console.error('Error loading resources:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const authContext = {
    signIn: async (token) => {
      try {
        await SecureStore.setItemAsync('userToken', token);
        setUserToken(token);
      } catch (error) {
        console.error('Error saving token:', error);
        throw error;
      }
    },
    signOut: async () => {
      try {
        await SecureStore.deleteItemAsync('userToken');
        setUserToken(null);
      } catch (error) {
        console.error('Error removing token:', error);
      }
    },
  };

  if (isLoading || !fontsLoaded) {
    return (
      <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center', backgroundColor: colors.background }}>
        <ActivityIndicator size="large" color={colors.primary} />
      </View>
    );
  }

  return (
    <SafeAreaProvider>
      <NavigationContainer>
        <StatusBar style="dark" backgroundColor={colors.background} />
        <Stack.Navigator screenOptions={{ headerShown: false }}>
          {userToken == null ? (
            <>
              <Stack.Screen name="Login">
                {props => <LoginScreen {...props} authContext={authContext} />}
              </Stack.Screen>
              <Stack.Screen name="SignUp">
                {props => <SignUpScreen {...props} authContext={authContext} />}
              </Stack.Screen>
            </>
          ) : (
            <Stack.Screen name="Main">
              {props => <MainTabNavigator {...props} authContext={authContext} />}
            </Stack.Screen>
          )}
        </Stack.Navigator>
      </NavigationContainer>
    </SafeAreaProvider>
  );
}
```

## src/constants/colors.js
```javascript
export const colors = {
  primary: '#E6E6FA', // Soft Lavender
  secondary: '#B0E2FF', // Light Teal
  accent: '#F5F5DC', // Warm Sand
  textPrimary: '#333333', // Dark Gray
  textSecondary: '#777777', // Gray
  background: '#FAFAFA', // Off-White
  white: '#FFFFFF',
  error: '#FF6B6B',
  success: '#4ECDC4',
};
```

## src/constants/typography.js
```javascript
import { Platform } from 'react-native';

export const typography = {
  heading: {
    fontFamily: Platform.select({
      ios: 'Montserrat-SemiBold',
      android: 'Montserrat-SemiBold',
      default: 'System',
    }),
    fontSize: 24,
  },
  subheading: {
    fontFamily: Platform.select({
      ios: 'Montserrat-SemiBold',
      android: 'Montserrat-SemiBold',
      default: 'System',
    }),
    fontSize: 18,
  },
  body: {
    fontFamily: Platform.select({
      ios: 'OpenSans-Regular',
      android: 'OpenSans-Regular',
      default: 'System',
    }),
    fontSize: 16,
  },
  caption: {
    fontFamily: Platform.select({
      ios: 'OpenSans-Regular',
      android: 'OpenSans-Regular',
      default: 'System',
    }),
    fontSize: 14,
  },
};
```

## src/screens/LoginScreen.js
```javascript
import React, { useState } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  StyleSheet,
  KeyboardAvoidingView,
  Platform,
  ScrollView,
  Alert,
  ActivityIndicator,
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { colors } from '../constants/colors';
import { typography } from '../constants/typography';
import { validateEmail, validatePassword } from '../utils/validation';

const LoginScreen = ({ navigation, authContext }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [errors, setErrors] = useState({});

  const handleLogin = async () => {
    // Validate inputs
    const newErrors = {};
    
    if (!validateEmail(email)) {
      newErrors.email = 'Please enter a valid email address';
    }
    
    if (!validatePassword(password)) {
      newErrors.password = 'Password must be at least 8 characters';
    }

    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return;
    }

    setLoading(true);
    setErrors({});

    try {
      // Simulate API call
      await new Promise(resolve => setTimeout(resolve, 1500));
      
      // For MVP, we'll simulate successful login
      const mockToken = 'mock_jwt_token_' + Date.now();
      await authContext.signIn(mockToken);
    } catch (error) {
      Alert.alert('Login Error', 'Failed to login. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <SafeAreaView style={styles.container}>
      <KeyboardAvoidingView
        behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
        style={styles.keyboardView}
      >
        <ScrollView
          contentContainerStyle={styles.scrollContent}
          showsVerticalScrollIndicator={false}
        >
          <View style={styles.logoContainer}>
            <Text style={styles.logo}>SoundSleep</Text>
            <Text style={styles.tagline}>Your path to better rest</Text>
          </View>

          <View style={styles.formContainer}>
            <Text style={styles.title}>Welcome Back</Text>

            <View style={styles.inputContainer}>
              <Text style={styles.label}>Email</Text>
              <TextInput
                style={[styles.input, errors.email && styles.inputError]}
                placeholder="Enter your email"
                placeholderTextColor={colors.textSecondary}
                value={email}
                onChangeText={setEmail}
                keyboardType="email-address"
                autoCapitalize="none"
                autoCorrect={false}
                accessibilityLabel="Email input"
                accessibilityHint="Enter your email address to login"
              />
              {errors.email && <Text style={styles.errorText}>{errors.email}</Text>}
            </View>

            <View style={styles.inputContainer}>
              <Text style={styles.label}>Password</Text>
              <TextInput
                style={[styles.input, errors.password && styles.inputError]}
                placeholder="Enter your password"
                placeholderTextColor={colors.textSecondary}
                value={password}
                onChangeText={setPassword}
                secureTextEntry
                autoCapitalize="none"
                accessibilityLabel="Password input"
                accessibilityHint="Enter your password to login"
              />
              {errors.password && <Text style={styles.errorText}>{errors.password}</Text>}
            </View>

            <TouchableOpacity
              style={[styles.button, loading && styles.buttonDisabled]}
              onPress={handleLogin}
              disabled={loading}
              accessibilityRole="button"
              accessibilityLabel="Login button"
            >
              {loading ? (
                <ActivityIndicator color={colors.white} />
              ) : (
                <Text style={styles.buttonText}>Login</Text>
              )}
            </TouchableOpacity>

            <TouchableOpacity
              style={styles.linkContainer}
              onPress={() => navigation.navigate('SignUp')}
              accessibilityRole="button"
              accessibilityLabel="Sign up link"
            >
              <Text style={styles.linkText}>
                Don't have an account? <Text style={styles.linkTextBold}>Sign Up</Text>
              </Text>
            </TouchableOpacity>

            <TouchableOpacity
              style={styles.linkContainer}
              onPress={() => Alert.alert('Forgot Password', 'Password reset functionality coming soon!')}
              accessibilityRole="button"
              accessibilityLabel="Forgot password link"
            >
              <Text style={styles.forgotText}>Forgot Password?</Text>
            </TouchableOpacity>
          </View>
        </ScrollView>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.background,
  },
  keyboardView: {
    flex: 1,
  },
  scrollContent: {
    flexGrow: 1,
    paddingHorizontal: 20,
    paddingVertical: 30,
  },
  logoContainer: {
    alignItems: 'center',
    marginBottom: 40,
    marginTop: 40,
  },
  logo: {
    ...typography.heading,
    fontSize: 36,
    color: colors.primary,
    marginBottom: 8,
  },
  tagline: {
    ...typography.caption,
    color: colors.textSecondary,
  },
  formContainer: {
    flex: 1,
  },
  title: {
    ...typography.heading,
    color: colors.textPrimary,
    marginBottom: 30,
    textAlign: 'center',
  },
  inputContainer: {
    marginBottom: 20,
  },
  label: {
    ...typography.body,
    color: colors.textPrimary,
    marginBottom: 8,
  },
  input: {
    ...typography.body,
    backgroundColor: colors.white,
    borderRadius: 12,
    paddingHorizontal: 16,
    paddingVertical: 14,
    borderWidth: 1,
    borderColor: '#E0E0E0',
    color: colors.textPrimary,
  },
  inputError: {
    borderColor: colors.error,
  },
  errorText: {
    ...typography.caption,
    color: colors.error,
    marginTop: 4,
  },
  button: {
    backgroundColor: colors.primary,
    borderRadius: 12,
    paddingVertical: 16,
    alignItems: 'center',
    marginTop: 20,
    elevation: 2,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
  },
  buttonDisabled: {
    opacity: 0.7,
  },
  buttonText: {
    ...typography.subheading,
    color: colors.white,
  },
  linkContainer: {
    alignItems: 'center',
    marginTop: 20,
  },
  linkText: {
    ...typography.body,
    color: colors.textSecondary,
  },
  linkTextBold: {
    ...typography.body,
    color: colors.primary,
    fontWeight: '600',
  },
  forgotText: {
    ...typography.body,
    color: colors.secondary,
  },
});

export default LoginScreen;
```

## src/screens/SignUpScreen.js
```javascript
import React, { useState } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  StyleSheet,
  KeyboardAvoidingView,
  Platform,
  ScrollView,
  Alert,
  ActivityIndicator,
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { colors } from '../constants/colors';
import { typography } from '../constants/typography';
import { validateEmail, validatePassword, validateName } from '../utils/validation';

const SignUpScreen = ({ navigation, authContext }) => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [errors, setErrors] = useState({});

  const handleSignUp = async () => {
    const newErrors = {};
    
    if (!validateName(name)) {
      newErrors.name = 'Name must be at least 2 characters';
    }

----------

# QA Report: SoundSleep App - Expo MVP Code Analysis

## Executive Summary
After thoroughly analyzing the SoundSleep App Expo MVP code, I've identified several critical bugs, potential issues, and areas for improvement. While the overall structure is good, there are important issues that need to be addressed before the app can be considered production-ready.

## 🔴 Critical Issues

### 1. **Incomplete SignUpScreen Implementation**
**File:** `src/screens/SignUpScreen.js`
**Issue:** The code is truncated and incomplete. The `handleSignUp` function is not fully implemented, and the component doesn't return any JSX.
**Solution:** Complete the implementation:
```javascript
// Add after line with validateName check
if (!validateEmail(email)) {
  newErrors.email = 'Please enter a valid email address';
}

if (!validatePassword(password)) {
  newErrors.password = 'Password must be at least 8 characters';
}

if (password !== confirmPassword) {
  newErrors.confirmPassword = 'Passwords do not match';
}

if (Object.keys(newErrors).length > 0) {
  setErrors(newErrors);
  return;
}

setLoading(true);
setErrors({});

try {
  await new Promise(resolve => setTimeout(resolve, 1500));
  const mockToken = 'mock_jwt_token_' + Date.now();
  await authContext.signIn(mockToken);
} catch (error) {
  Alert.alert('Sign Up Error', 'Failed to create account. Please try again.');
} finally {
  setLoading(false);
}
```

### 2. **Missing Validation Utils Module**
**Files Referenced:** `src/utils/validation.js`
**Issue:** The validation functions are imported but the file is not provided.
**Solution:** Create the validation utils file:
```javascript
// src/utils/validation.js
export const validateEmail = (email) => {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(email);
};

export const validatePassword = (password) => {
  return password && password.length >= 8;
};

export const validateName = (name) => {
  return name && name.trim().length >= 2;
};
```

### 3. **Missing MainTabNavigator Component**
**File Referenced:** `src/navigation/MainTabNavigator.js`
**Issue:** The MainTabNavigator is imported but not provided.
**Solution:** Create the navigation component with proper tab structure.

### 4. **Missing Font Files**
**Files Referenced:** 
- `./assets/fonts/Montserrat-SemiBold.ttf`
- `./assets/fonts/OpenSans-Regular.ttf`
**Issue:** Font files are referenced but not included, which will cause the app to crash on startup.
**Solution:** Either include the font files or implement a fallback mechanism:
```javascript
const loadResources = async () => {
  try {
    await Font.loadAsync({
      'Montserrat-SemiBold': require('./assets/fonts/Montserrat-SemiBold.ttf'),
      'OpenSans-Regular': require('./assets/fonts/OpenSans-Regular.ttf'),
    });
    setFontsLoaded(true);
  } catch (error) {
    console.warn('Fonts not available, using system fonts');
    setFontsLoaded(true); // Continue with system fonts
  }
  // ... rest of the code
};
```

## 🟡 Medium Priority Issues

### 5. **AuthContext Not Properly Implemented**
**File:** `App.js`
**Issue:** AuthContext is created as a plain object but not using React Context API properly.
**Solution:** Implement proper React Context:
```javascript
import React, { createContext, useContext } from 'react';

export const AuthContext = createContext(null);

// In App.js, wrap the NavigationContainer:
<AuthContext.Provider value={authContext}>
  <NavigationContainer>
    {/* ... */}
  </NavigationContainer>
</AuthContext.Provider>
```

### 6. **No Error Boundary Implementation**
**Issue:** No error boundary to catch runtime errors.
**Solution:** Add an error boundary component:
```javascript
class ErrorBoundary extends React.Component {
  state = { hasError: false };
  
  static getDerivedStateFromError(error) {
    return { hasError: true };
  }
  
  componentDidCatch(error, errorInfo) {
    console.error('Error caught by boundary:', error, errorInfo);
  }
  
  render() {
    if (this.state.hasError) {
      return <Text>Something went wrong. Please restart the app.</Text>;
    }
    return this.props.children;
  }
}
```

### 7. **Insecure Token Storage Pattern**
**File:** `App.js`
**Issue:** While SecureStore is used, there's no token validation or expiration handling.
**Solution:** Implement token validation:
```javascript
const validateToken = (token) => {
  // Add token structure validation
  if (!token || typeof token !== 'string') return false;
  // Add expiration check if token contains timestamp
  return true;
};

const loadResources = async () => {
  const token = await SecureStore.getItemAsync('userToken');
  if (token && validateToken(token)) {
    setUserToken(token);
  } else if (token) {
    await SecureStore.deleteItemAsync('userToken');
  }
};
```

## 🟢 Minor Issues & Improvements

### 8. **Missing Accessibility Labels**
**Issue:** Some interactive elements lack proper accessibility attributes.
**Solution:** Add accessibility labels to all touchable elements and ensure proper screen reader support.

### 9. **No Network Status Handling**
**Issue:** No handling for offline scenarios.
**Solution:** Implement network status monitoring using NetInfo:
```javascript
import NetInfo from '@react-native-community/netinfo';

useEffect(() => {
  const unsubscribe = NetInfo.addEventListener(state => {
    if (!state.isConnected) {
      Alert.alert('No Internet', 'Please check your connection');
    }
  });
  return unsubscribe;
}, []);
```

### 10. **Platform-Specific Style Issues**
**File:** `src/screens/LoginScreen.js`
**Issue:** `elevation` property only works on Android, iOS shadow properties might not render correctly.
**Solution:** Create platform-specific shadow styles:
```javascript
const shadowStyle = Platform.select({
  ios: {
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
  },
  android: {
    elevation: 2,
  },
});
```

### 11. **Memory Leak Potential**
**File:** `App.js`
**Issue:** Async operations in useEffect without cleanup.
**Solution:** Add cleanup and cancellation:
```javascript
useEffect(() => {
  let isMounted = true;
  
  const loadResources = async () => {
    try {
      // ... loading logic
      if (isMounted) {
        setFontsLoaded(true);
        setUserToken(token);
      }
    } catch (error) {
      if (isMounted) {
        console.error('Error:', error);
      }
    }
  };
  
  loadResources();
  
  return () => {
    isMounted = false;
  };
}, []);
```

### 12. **Input Validation Timing**
**Files:** `LoginScreen.js`, `SignUpScreen.js`
**Issue:** Validation only occurs on submit, not real-time.
**Solution:** Add real-time validation with debouncing:
```javascript
useEffect(() => {
  const timer = setTimeout(() => {
    if (email && !validateEmail(email)) {
      setErrors(prev => ({ ...prev, email: 'Invalid email format' }));
    } else {
      setErrors(prev => ({ ...prev, email: null }));
    }
  }, 500);
  
  return () => clearTimeout(timer);
}, [email]);
```

## 📋 Performance Recommendations

1. **Implement React.memo** for components that don't need frequent re-renders
2. **Use useCallback and useMemo** for expensive operations and callback functions
3. **Implement lazy loading** for screens using React.lazy()
4. **Add image optimization** using expo-image with proper caching
5. **Implement proper list virtualization** if lists are added later

## 🔒 Security Recommendations

1. **Implement proper API authentication** instead of mock tokens
2. **Add rate limiting** for login attempts
3. **Implement certificate pinning** for production
4. **Add input sanitization** beyond basic validation
5. **Implement proper session management** with token refresh

## 📱 Device Compatibility Issues

1. **Test on different screen sizes** - Add responsive design patterns
2. **Handle notch/safe areas properly** - Current SafeAreaView might not cover all cases
3. **Test keyboard behavior** on different devices
4. **Add tablet support considerations**

## Conclusion

The SoundSleep App has a solid foundation but requires immediate attention to the critical issues listed above, particularly:
- Completing the SignUpScreen implementation
- Adding missing files (validation utils, navigation, fonts)
- Implementing proper error handling and boundaries
- Fixing the AuthContext implementation

Once these issues are resolved, the app should undergo thorough testing on both iOS and Android devices before being considered ready for production deployment.

**Priority Action Items:**
1. Complete all missing implementations (Critical)
2. Add proper error handling and validation (Critical)
3. Implement security best practices (High)
4. Add performance optimizations (Medium)
5. Enhance accessibility features (Medium)

The mobile_developer should address these issues in order of priority to ensure a stable, secure, and user-friendly application.

----------

# SoundSleep App - Refactored Expo MVP Code

## package.json
```json
{
  "name": "soundsleep-app",
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
    "expo-secure-store": "~12.3.1",
    "expo-image": "~1.3.5",
    "react": "18.2.0",
    "react-native": "0.72.6",
    "react-native-safe-area-context": "4.6.3",
    "react-native-screens": "~3.22.0",
    "@react-navigation/native": "^6.1.7",
    "@react-navigation/native-stack": "^6.9.13",
    "@react-navigation/bottom-tabs": "^6.5.8",
    "@expo/vector-icons": "^13.0.0",
    "@react-native-community/netinfo": "9.3.10"
  },
  "devDependencies": {
    "@babel/core": "^7.20.0"
  },
  "private": true
}
```

## App.js
```javascript
import React, { useState, useEffect, createContext, useContext } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import { StatusBar } from 'expo-status-bar';
import * as Font from 'expo-font';
import * as SecureStore from 'expo-secure-store';
import NetInfo from '@react-native-community/netinfo';
import { View, ActivityIndicator, Text, Alert } from 'react-native';

import LoginScreen from './src/screens/LoginScreen';
import SignUpScreen from './src/screens/SignUpScreen';
import MainTabNavigator from './src/navigation/MainTabNavigator';
import ErrorBoundary from './src/components/ErrorBoundary';
import { colors } from './src/constants/colors';

const Stack = createNativeStackNavigator();

// Create Auth Context
export const AuthContext = createContext(null);

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within AuthProvider');
  }
  return context;
};

// Token validation function
const validateToken = (token) => {
  if (!token || typeof token !== 'string') return false;
  // Add more sophisticated token validation here
  // For MVP, we just check if it exists and is a string
  return true;
};

export default function App() {
  const [isLoading, setIsLoading] = useState(true);
  const [userToken, setUserToken] = useState(null);
  const [fontsLoaded, setFontsLoaded] = useState(false);
  const [isConnected, setIsConnected] = useState(true);

  useEffect(() => {
    let isMounted = true;

    const loadResources = async () => {
      try {
        // Try to load fonts with fallback
        try {
          await Font.loadAsync({
            'Montserrat-SemiBold': require('./assets/fonts/Montserrat-SemiBold.ttf'),
            'OpenSans-Regular': require('./assets/fonts/OpenSans-Regular.ttf'),
          });
          if (isMounted) setFontsLoaded(true);
        } catch (fontError) {
          console.warn('Fonts not available, using system fonts');
          if (isMounted) setFontsLoaded(true); // Continue with system fonts
        }

        // Check for stored token with validation
        const token = await SecureStore.getItemAsync('userToken');
        if (token && validateToken(token)) {
          if (isMounted) setUserToken(token);
        } else if (token) {
          // Invalid token, remove it
          await SecureStore.deleteItemAsync('userToken');
        }
      } catch (error) {
        console.error('Error loading resources:', error);
      } finally {
        if (isMounted) setIsLoading(false);
      }
    };

    loadResources();

    // Network status monitoring
    const unsubscribe = NetInfo.addEventListener(state => {
      if (isMounted) {
        setIsConnected(state.isConnected);
        if (!state.isConnected) {
          Alert.alert('No Internet', 'Please check your connection');
        }
      }
    });

    return () => {
      isMounted = false;
      unsubscribe();
    };
  }, []);

  const authContext = {
    signIn: async (token) => {
      try {
        if (!validateToken(token)) {
          throw new Error('Invalid token format');
        }
        await SecureStore.setItemAsync('userToken', token);
        setUserToken(token);
      } catch (error) {
        console.error('Error saving token:', error);
        throw error;
      }
    },
    signOut: async () => {
      try {
        await SecureStore.deleteItemAsync('userToken');
        setUserToken(null);
      } catch (error) {
        console.error('Error removing token:', error);
      }
    },
    userToken,
    isConnected,
  };

  if (isLoading) {
    return (
      <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center', backgroundColor: colors.background }}>
        <ActivityIndicator size="large" color={colors.primary} />
      </View>
    );
  }

  return (
    <ErrorBoundary>
      <SafeAreaProvider>
        <AuthContext.Provider value={authContext}>
          <NavigationContainer>
            <StatusBar style="dark" backgroundColor={colors.background} />
            <Stack.Navigator screenOptions={{ headerShown: false }}>
              {userToken == null ? (
                <>
                  <Stack.Screen name="Login" component={LoginScreen} />
                  <Stack.Screen name="SignUp" component={SignUpScreen} />
                </>
              ) : (
                <Stack.Screen name="Main" component={MainTabNavigator} />
              )}
            </Stack.Navigator>
          </NavigationContainer>
        </AuthContext.Provider>
      </SafeAreaProvider>
    </ErrorBoundary>
  );
}
```

## src/components/ErrorBoundary.js
```javascript
import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import { colors } from '../constants/colors';
import { typography } from '../constants/typography';

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
          <Text style={styles.title}>Oops! Something went wrong</Text>
          <Text style={styles.message}>
            We're sorry for the inconvenience. Please try restarting the app.
          </Text>
          <TouchableOpacity style={styles.button} onPress={this.handleReset}>
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
    backgroundColor: colors.background,
  },
  title: {
    ...typography.heading,
    color: colors.textPrimary,
    marginBottom: 10,
    textAlign: 'center',
  },
  message: {
    ...typography.body,
    color: colors.textSecondary,
    textAlign: 'center',
    marginBottom: 30,
  },
  button: {
    backgroundColor: colors.primary,
    paddingHorizontal: 30,
    paddingVertical: 12,
    borderRadius: 8,
  },
  buttonText: {
    ...typography.body,
    color: colors.white,
    fontWeight: '600',
  },
});

export default ErrorBoundary;
```

## src/utils/validation.js
```javascript
export const validateEmail = (email) => {
  const re = /^[^\s@]+@[^\s@]+\.[^\