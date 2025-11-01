```markdown
# Habitual: Simple Habit Tracker - Expo MVP Code

## package.json
```json
{
  "name": "habitual-habit-tracker",
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
    "@react-navigation/native-stack": "^6.9.17",
    "@react-navigation/bottom-tabs": "^6.5.11",
    "react-native-screens": "~3.22.0",
    "react-native-safe-area-context": "4.6.3",
    "@react-native-async-storage/async-storage": "1.18.2",
    "expo-secure-store": "~12.3.1",
    "@expo/vector-icons": "^13.0.0",
    "react-native-uuid": "^2.0.1",
    "expo-crypto": "~12.4.1"
  },
  "devDependencies": {
    "@babel/core": "^7.20.0"
  },
  "private": true
}
```

## App.js
```javascript
import React, { useMemo } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { StatusBar } from 'expo-status-bar';
import { View, ActivityIndicator } from 'react-native';
import { Ionicons } from '@expo/vector-icons';

// Import screens
import LoginScreen from './src/screens/LoginScreen';
import SignupScreen from './src/screens/SignupScreen';
import HomeScreen from './src/screens/HomeScreen';
import CreateHabitScreen from './src/screens/CreateHabitScreen';
import ProfileScreen from './src/screens/ProfileScreen';
import SettingsScreen from './src/screens/SettingsScreen';
import ProgressScreen from './src/screens/ProgressScreen';

// Import context and theme
import { ThemeProvider } from './src/context/ThemeContext';
import { AuthProvider, useAuth } from './src/context/AuthContext';
import { HabitProvider } from './src/context/HabitContext';
import ErrorBoundary from './src/components/ErrorBoundary';

const Stack = createNativeStackNavigator();
const Tab = createBottomTabNavigator();

function AuthStack() {
  return (
    <Stack.Navigator screenOptions={{ headerShown: false }}>
      <Stack.Screen name="Login" component={LoginScreen} />
      <Stack.Screen name="Signup" component={SignupScreen} />
    </Stack.Navigator>
  );
}

function MainTabs() {
  return (
    <Tab.Navigator
      screenOptions={({ route }) => ({
        tabBarIcon: ({ focused, color, size }) => {
          let iconName;
          if (route.name === 'Home') {
            iconName = focused ? 'home' : 'home-outline';
          } else if (route.name === 'Progress') {
            iconName = focused ? 'stats-chart' : 'stats-chart-outline';
          } else if (route.name === 'Profile') {
            iconName = focused ? 'person' : 'person-outline';
          }
          return <Ionicons name={iconName} size={size} color={color} />;
        },
        tabBarActiveTintColor: '#4CAF50',
        tabBarInactiveTintColor: '#757575',
        headerShown: false,
        tabBarAccessibilityLabel: route.name,
      })}
    >
      <Tab.Screen name="Home" component={HomeStack} />
      <Tab.Screen name="Progress" component={ProgressScreen} />
      <Tab.Screen name="Profile" component={ProfileStack} />
    </Tab.Navigator>
  );
}

function HomeStack() {
  return (
    <Stack.Navigator>
      <Stack.Screen 
        name="HomeMain" 
        component={HomeScreen} 
        options={{ title: 'Habitual' }}
      />
      <Stack.Screen 
        name="CreateHabit" 
        component={CreateHabitScreen} 
        options={{ title: 'Create New Habit' }}
      />
    </Stack.Navigator>
  );
}

function ProfileStack() {
  return (
    <Stack.Navigator>
      <Stack.Screen 
        name="ProfileMain" 
        component={ProfileScreen} 
        options={{ title: 'Profile' }}
      />
      <Stack.Screen 
        name="Settings" 
        component={SettingsScreen} 
        options={{ title: 'Settings' }}
      />
    </Stack.Navigator>
  );
}

function RootNavigator() {
  const { isLoggedIn, isLoading } = useAuth();

  if (isLoading) {
    return (
      <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
        <ActivityIndicator size="large" color="#4CAF50" accessibilityLabel="Loading" />
      </View>
    );
  }

  return (
    <NavigationContainer>
      {isLoggedIn ? <MainTabs /> : <AuthStack />}
    </NavigationContainer>
  );
}

export default function App() {
  return (
    <ErrorBoundary>
      <ThemeProvider>
        <AuthProvider>
          <HabitProvider>
            <StatusBar style="auto" />
            <RootNavigator />
          </HabitProvider>
        </AuthProvider>
      </ThemeProvider>
    </ErrorBoundary>
  );
}
```

## src/components/ErrorBoundary.js
```javascript
import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';

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
            {this.state.error?.message || 'An unexpected error occurred'}
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
    backgroundColor: '#f5f5f5',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 10,
    color: '#333',
  },
  message: {
    fontSize: 16,
    textAlign: 'center',
    marginBottom: 20,
    color: '#666',
  },
  button: {
    backgroundColor: '#4CAF50',
    paddingHorizontal: 30,
    paddingVertical: 12,
    borderRadius: 5,
  },
  buttonText: {
    color: 'white',
    fontSize: 16,
    fontWeight: '600',
  },
});

export default ErrorBoundary;
```

## src/context/AuthContext.js
```javascript
import React, { createContext, useState, useEffect, useContext, useMemo } from 'react';
import * as SecureStore from 'expo-secure-store';
import * as Crypto from 'expo-crypto';
import AsyncStorage from '@react-native-async-storage/async-storage';
import uuid from 'react-native-uuid';
import { validateEmail, validatePassword, sanitizeInput } from '../utils/validation';

const AuthContext = createContext({});

export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const [user, setUser] = useState(null);

  useEffect(() => {
    let isMounted = true;

    const checkAuthStatus = async () => {
      try {
        const token = await SecureStore.getItemAsync('authToken');
        const userData = await AsyncStorage.getItem('userData');
        
        if (isMounted && token && userData) {
          setUser(JSON.parse(userData));
          setIsLoggedIn(true);
        }
      } catch (error) {
        console.error('Auth check failed:', error);
      } finally {
        if (isMounted) {
          setIsLoading(false);
        }
      }
    };

    checkAuthStatus();

    return () => {
      isMounted = false;
    };
  }, []);

  const hashPassword = async (password) => {
    const digest = await Crypto.digestStringAsync(
      Crypto.CryptoDigestAlgorithm.SHA256,
      password + 'habitual_salt_2024', // Add salt for extra security
      { encoding: Crypto.CryptoEncoding.HEX }
    );
    return digest;
  };

  const login = async (email, password) => {
    try {
      // Validate and sanitize input
      const sanitizedEmail = sanitizeInput(email?.toLowerCase().trim());
      
      if (!sanitizedEmail || !password) {
        throw new Error('Email and password are required');
      }

      if (!validateEmail(sanitizedEmail)) {
        throw new Error('Invalid email format');
      }

      // Hash the password for comparison
      const hashedPassword = await hashPassword(password);

      // Check stored credentials
      const users = await AsyncStorage.getItem('users');
      const userList = users ? JSON.parse(users) : [];
      
      const user = userList.find(u => 
        u.email === sanitizedEmail && u.password === hashedPassword
      );
      
      if (!user) {
        throw new Error('Invalid email or password');
      }

      // Generate secure token
      const token = uuid.v4();
      
      // Store auth data
      await SecureStore.setItemAsync('authToken', token);
      
      // Don't store password in userData
      const { password: _, ...userWithoutPassword } = user;
      await AsyncStorage.setItem('userData', JSON.stringify(userWithoutPassword));
      
      setUser(userWithoutPassword);
      setIsLoggedIn(true);
      
      return { success: true };
    } catch (error) {
      return { success: false, error: error.message };
    }
  };

  const signup = async (name, email, password) => {
    try {
      // Sanitize inputs
      const sanitizedName = sanitizeInput(name?.trim());
      const sanitizedEmail = sanitizeInput(email?.toLowerCase().trim());
      
      // Validate inputs
      if (!sanitizedName || !sanitizedEmail || !password) {
        throw new Error('All fields are required');
      }

      if (sanitizedName.length > 50) {
        throw new Error('Name is too long (max 50 characters)');
      }

      if (!validateEmail(sanitizedEmail)) {
        throw new Error('Invalid email format');
      }

      const passwordValidation = validatePassword(password);
      if (!passwordValidation.isValid) {
        throw new Error(passwordValidation.message);
      }

      // Check if user exists
      const users = await AsyncStorage.getItem('users');
      const userList = users ? JSON.parse(users) : [];
      
      if (userList.find(u => u.email === sanitizedEmail)) {
        throw new Error('Email already registered');
      }

      // Hash password
      const hashedPassword = await hashPassword(password);

      // Create new user
      const newUser = {
        id: uuid.v4(),
        name: sanitizedName,
        email: sanitizedEmail,
        password: hashedPassword,
        createdAt: new Date().toISOString()
      };

      // Save user
      userList.push(newUser);
      await AsyncStorage.setItem('users', JSON.stringify(userList));

      // Auto-login
      return await login(sanitizedEmail, password);
    } catch (error) {
      return { success: false, error: error.message };
    }
  };

  const logout = async () => {
    try {
      await SecureStore.deleteItemAsync('authToken');
      await AsyncStorage.removeItem('userData');
      setUser(null);
      setIsLoggedIn(false);
      return { success: true };
    } catch (error) {
      return { success: false, error: error.message };
    }
  };

  const contextValue = useMemo(() => ({
    isLoggedIn,
    isLoading,
    user,
    login,
    signup,
    logout
  }), [isLoggedIn, isLoading, user]);

  return (
    <AuthContext.Provider value={contextValue}>
      {children}
    </AuthContext.Provider>
  );
};
```

## src/context/ThemeContext.js
```javascript
import React, { createContext, useState, useContext, useEffect, useMemo } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { THEME_CONSTANTS } from '../utils/constants';

const ThemeContext = createContext({});

export const useTheme = () => useContext(ThemeContext);

const lightTheme = {
  primary: '#4CAF50',
  secondary: '#E8F5E9',
  accent: '#FFC107',
  textPrimary: '#212121',
  textSecondary: '#757575',
  background: '#FFFFFF',
  cardBackground: '#FFFFFF',
  error: '#F44336',
  border: '#E0E0E0',
};

const darkTheme = {
  primary: '#4CAF50',
  secondary: '#1B5E20',
  accent: '#FFC107',
  textPrimary: '#FFFFFF',
  textSecondary: '#B0B0B0',
  background: '#121212',
  cardBackground: '#1E1E1E',
  error: '#CF6679',
  border: '#333333',
};

export const ThemeProvider = ({ children }) => {
  const [isDarkMode, setIsDarkMode] = useState(false);
  const theme = isDarkMode ? darkTheme : lightTheme;

  useEffect(() => {
    loadThemePreference();
  }, []);

  const loadThemePreference = async () => {
    try {
      const savedTheme = await AsyncStorage.getItem('themeMode');
      if (savedTheme === 'dark') {
        setIsDarkMode(true);
      }
    } catch (error) {
      console.error('Failed to load theme preference:', error);
    }
  };

  const toggleTheme = async () => {
    try {
      const newMode = !isDarkMode;
      setIsDarkMode(newMode);
      await AsyncStorage.setItem('themeMode', newMode ? 'dark' : 'light');
    } catch (error) {
      console.error('Failed to save theme preference:', error);
    }
  };

  const contextValue = useMemo(() => ({
    theme,
    isDarkMode,
    toggleTheme
  }), [theme, isDarkMode]);

  return (
    <ThemeContext.Provider value={contextValue}>
      {children}
    </ThemeContext.Provider>
  );
};
```

## src/context/HabitContext.js
```javascript
import React, { createContext, useState, useContext, useEffect, useMemo } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { useAuth } from './AuthContext';
import uuid from 'react-native-uuid';

const HabitContext = createContext({});

export const useHabits = () => useContext(HabitContext);

export const HabitProvider = ({ children }) => {
  const [habits, setHabits] = useState([]);
  const [loading, setLoading] = useState(false);
  const { user } = useAuth();

  useEffect(() => {
    if (user) {
      loadHabits();
    }
  }, [user]);

  const loadHabits = async () => {
    try {
      setLoading(true);
      const key = `habits_${user?.id}`;
      const storedHabits = await AsyncStorage.getItem(key);
      if (storedHabits) {
        setHabits(JSON.parse(storedHabits));
      }
    } catch (error) {
      console.error('Failed to load habits:', error);
    } finally {
      setLoading(false);
    }
  };

  const saveHabits = async (updatedHabits) => {
    try {
      const key = `habits_${user?.id}`;
      await AsyncStorage.setItem(key, JSON.stringify(updatedHabits));
      setHabits(updatedHabits);
      return { success: true };
    } catch (error) {
      console.error('Failed to save habits:', error);
      return { success: false, error: error.message };
    }
  };

  const addHabit = async (habitData) => {
    try {
      // Validate habit data
      if (!habitData.name?.trim()) {
        throw new Error('Habit name is required');
      }

      if (habitData.name.length > 50) {
        throw new Error('Habit name too long (max 50 characters)');
      }

      // Check for duplicates
      if (habits.find(h => h.name.toLowerCase() === habitData.name.toLowerCase())) {
        throw new Error('A habit with this name already exists');
      }

      const newHabit = {
        id: uuid.v4(),
        ...habitData,
        createdAt: new Date().toISOString(),
        completedDates: [],
        streak: 0,
        bestStreak: 0,
      };

      const updatedHabits = [...habits, newHabit];
      const result = await saveHabits(updatedHabits);
      
      if (result.success) {
        return { success: true, habit: newHabit };
      } else {
        throw new Error(result.error);
      }
    } catch (error) {
      return { success: false, error: error.message };
    }
  };

  const calculateStreak = (completedDates) => {
    if (!completedDates || completedDates.length === 0) return 0;
    
    const sortedDates = completedDates
      .map(d => new Date(d))
      .sort((a, b) => b - a);
    
    let streak = 0;
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    
    for (let i = 0; i < sortedDates.length; i++) {
      const checkDate = new Date(today);
      checkDate.setDate(checkDate.getDate() - i);
      checkDate.setHours(0, 0, 0, 0);
      
      if (sortedDates.some(d => {
        const compareDate = new Date(d);
        compareDate.setHours(0, 0, 0, 0);
        return compareDate.getTime() === checkDate.getTime();
      })) {
        streak++;
      } else if (i > 0) {
        break;
      }
    }
    
    return streak;
  };

  const toggleHabitCompletion = async (habitId, date = new Date().toISOString().split('T')[0]) => {
    try {
      const updatedHabits = habits.map(habit => {
        if (habit.id === habitId) {
          const completedDates = [...habit.completedDates];
          const dateIndex = completedDates.indexOf(date);
          
          if (dateIndex > -1) {
            completedDates.splice(dateIndex, 1);
          } else {
            completedDates.push(date);
          }
          
          // Calculate streak
          const streak = calculateStreak(completedDates);
          const bestStreak = Math.max(streak, habit.bestStreak || 0);
          
          return {
            ...habit,
            completedDates,
            streak,
            bestStreak
          };
        }
        return habit;
      });
      
      const result = await saveHabits(updatedHabits);
      return result;
    } catch (error) {
      return { success: false, error: error.message };
    }
  };

  const deleteHabit = async (habitId) => {
    try {
      const updatedHabits = habits.filter(habit => habit.id !== habitId);
      return await saveHabits(updatedHabits);
    } catch (error) {
      return { success: false, error: error.message };
    }
  };

  const updateHabit = async (habitId, updatedData) => {
    try {
      const updatedHabits = habits.map(habit => {
        if (habit.id === habitId) {
          return { ...habit, ...updatedData };
        }
        return habit;
      });
      return await saveHabits(updatedHabits);
    } catch (error) {
      return { success: false, error: error.message };
    }
  };

  const getHabitById = (habitId) => {
    return habits.find(habit => habit.id === habitId) || null;
  };

  const contextValue = useMemo(() => ({
    habits,
    loading,
    addHabit,
    toggleHabitCompletion,
    deleteHabit,
    updateHabit,
    getHabitById
  }), [habits, loading]);

  return (
    <HabitContext.Provider value={contextValue}>
      {children}
    </HabitContext.Provider>
  );
};
```

## src/screens/LoginScreen.js
```javascript
import React from 'react';
import { View, Text } from 'react-native';

const LoginScreen = () => {
  return (
    <View>
      <Text>Login Screen</Text>
    </View>
  );
};

export default LoginScreen;
```

## src/screens/SignupScreen.js
```javascript
import React from 'react';
import { View, Text } from 'react-native';

const SignupScreen = () => {
  return (
    <View>
      <Text>Signup Screen</Text>
    </View>
  );
};

export default SignupScreen;
```

## src/screens/HomeScreen.js
```javascript
import React from 'react';
import { View, Text } from 'react-native';

const HomeScreen = () => {
  return (
    <View>
      <Text>Home Screen</Text>
    </View>
  );
};

export default HomeScreen;
```

## src/screens/CreateHabitScreen.js
```javascript
import React from 'react';
import { View, Text } from 'react-native';

const CreateHabitScreen = () => {
  return (
    <View>
      <Text>Create Habit Screen</Text>
    </View>
  );
};

export default CreateHabitScreen;
```

## src/screens/ProfileScreen.js
```javascript
import React from 'react';
import { View, Text } from 'react-native';

const ProfileScreen = () => {
  return (
    <View>
      <Text>Profile Screen</Text>
    </View>
  );
};

export default ProfileScreen;
```

## src/screens/SettingsScreen.js
```javascript
import React from 'react';
import { View, Text } from 'react-native';

const SettingsScreen = () => {
  return (
    <View>
      <Text>Settings Screen</Text>
    </View>
  );
};

export default SettingsScreen;
```

## src/screens/ProgressScreen.js
```javascript
import React from 'react';
import { View, Text } from 'react-native';

const ProgressScreen = () => {
  return (
    <View>
      <Text>Progress Screen</Text>
    </View>
  );
};

export default ProgressScreen;
```

## src/utils/validation.js
```javascript
// src/utils/validation.js

export const validateEmail = (email) => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
};

export const validatePassword = (password) => {
  if (password.length < 8) {
    return { isValid: false, message: 'Password must be at least 8 characters' };
  }
  if (!/[A-Z]/.test(password)) {
    return { isValid: false, message: 'Password must contain at least one uppercase letter' };
  }
  if (!/[a-z]/.test(password)) {
    return { isValid: false, message: 'Password must contain at least one lowercase letter' };
  }
  if (!/[0-9]/.test(password)) {
    return { isValid: false, message: 'Password must contain at least one digit' };
  }
  if (!/[^A-Za-z0-9]/.test(password)) {
    return { isValid: false, message: 'Password must contain at least one special character' };
  }
  return { isValid: true, message: null };
};

export const sanitizeInput = (input) => {
  // Implement more robust sanitization as needed
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
};
```

## src/utils/constants.js
```javascript
export const THEME_CONSTANTS = {
    LIGHT: 'light',
    DARK: 'dark',
  };