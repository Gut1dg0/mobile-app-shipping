```markdown
# App.js
```javascript
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { StyleSheet, Text, View, ActivityIndicator } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { useState, useEffect } from 'react';

// Import screens
import DashboardScreen from './screens/DashboardScreen';
import TrackScreen from './screens/TrackScreen';
import ChallengesScreen from './screens/ChallengesScreen';
import DiscoverScreen from './screens/DiscoverScreen';
import ProfileScreen from './screens/ProfileScreen';
import OnboardingScreen from './screens/OnboardingScreen';

const Tab = createBottomTabNavigator();

const primaryColor = '#2E7D32';
const secondaryColor = '#A5D6A7';
const textColor = '#424242';
const backgroundColor = '#F5F5F5';

export default function App() {
  const [isOnboarded, setIsOnboarded] = useState(null);

  useEffect(() => {
    const checkOnboarding = async () => {
      try {
        const onboarded = await AsyncStorage.getItem('isOnboarded');
        setIsOnboarded(onboarded === 'true');
      } catch (error) {
        console.error("Error retrieving data", error);
        setIsOnboarded(false);
      }
    };

    checkOnboarding();
  }, []);

  if (isOnboarded === null) {
    return (
      <View style={[styles.container, { justifyContent: 'center' }]}>
        <ActivityIndicator size="large" color={primaryColor} />
      </View>
    );
  }

  if (!isOnboarded) {
    return <OnboardingScreen onCompleteOnboarding={() => setIsOnboarded(true)} />;
  }

  return (
    <NavigationContainer>
      <Tab.Navigator
        screenOptions={({ route }) => ({
          tabBarIcon: ({ focused, color, size }) => {
            let iconName;

            switch (route.name) {
              case 'Dashboard':
                iconName = focused ? 'ios-home' : 'ios-home-outline';
                break;
              case 'Track':
                iconName = focused ? 'ios-analytics' : 'ios-analytics-outline';
                break;
              case 'Challenges':
                iconName = focused ? 'ios-trophy' : 'ios-trophy-outline';
                break;
              case 'Discover':
                iconName = focused ? 'ios-compass' : 'ios-compass-outline';
                break;
              case 'Profile':
                iconName = focused ? 'ios-person' : 'ios-person-outline';
                break;
              default:
                iconName = 'ios-information-circle-outline';
            }

            return <Ionicons name={iconName} size={size} color={color} />;
          },
          tabBarActiveTintColor: primaryColor,
          tabBarInactiveTintColor: textColor,
          tabBarStyle: {
            backgroundColor: backgroundColor,
          },
        })}
      >
        <Tab.Screen name="Dashboard" component={DashboardScreen} />
        <Tab.Screen name="Track" component={TrackScreen} />
        <Tab.Screen name="Challenges" component={ChallengesScreen} />
        <Tab.Screen name="Discover" component={DiscoverScreen} />
        <Tab.Screen name="Profile" component={ProfileScreen} />
      </Tab.Navigator>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
```

```markdown
# screens/OnboardingScreen.js
```javascript
import React, { useState } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, TextInput, Alert } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';

const primaryColor = '#2E7D32';
const secondaryColor = '#A5D6A7';
const textColor = '#424242';
const backgroundColor = '#F5F5F5';

const OnboardingScreen = ({ onCompleteOnboarding }) => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');

  const isValidEmail = (email) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  };

  const handleOnboardingComplete = async () => {
    if (!name || !email) {
      Alert.alert('Error', 'Please enter your name and email.');
      return;
    }

    if (!isValidEmail(email)) {
      Alert.alert('Error', 'Please enter a valid email address.');
      return;
    }

    try {
      await AsyncStorage.setItem('isOnboarded', 'true');
      await AsyncStorage.setItem('userName', name);
      await AsyncStorage.setItem('userEmail', email);
      onCompleteOnboarding();
    } catch (error) {
      console.error("Error saving data", error);
      Alert.alert('Error', 'Failed to save data. Please try again.');
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Welcome to EcoTrack!</Text>
      <Text style={styles.subtitle}>Let's get to know you better.</Text>

      <TextInput
        style={styles.input}
        placeholder="Your Name"
        value={name}
        onChangeText={setName}
        placeholderTextColor={textColor}
        aria-label="Your Name"
      />
      <TextInput
        style={styles.input}
        placeholder="Your Email"
        value={email}
        onChangeText={setEmail}
        keyboardType="email-address"
        placeholderTextColor={textColor}
        aria-label="Your Email"
      />

      <TouchableOpacity style={styles.button} onPress={handleOnboardingComplete}>
        <Text style={styles.buttonText}>Get Started!</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: backgroundColor,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: primaryColor,
    marginBottom: 10,
  },
  subtitle: {
    fontSize: 16,
    color: textColor,
    marginBottom: 20,
    textAlign: 'center',
  },
  input: {
    width: '100%',
    height: 40,
    borderColor: secondaryColor,
    borderWidth: 1,
    borderRadius: 5,
    marginBottom: 10,
    paddingHorizontal: 10,
    backgroundColor: '#FFFFFF',
    color: textColor,
  },
  button: {
    backgroundColor: primaryColor,
    paddingVertical: 12,
    paddingHorizontal: 25,
    borderRadius: 5,
    marginTop: 20,
  },
  buttonText: {
    color: '#FFFFFF',
    fontSize: 16,
    fontWeight: 'bold',
    textAlign: 'center',
  },
});

export default OnboardingScreen;
```

```markdown
# screens/DashboardScreen.js
```javascript
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

const primaryColor = '#2E7D32';
const secondaryColor = '#A5D6A7';
const textColor = '#424242';
const backgroundColor = '#F5F5F5';

const DashboardScreen = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Dashboard</Text>
      <Text style={styles.text}>Welcome to your EcoTrack Dashboard!</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: backgroundColor,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: primaryColor,
    marginBottom: 10,
  },
  text: {
    fontSize: 16,
    color: textColor,
  },
});

export default DashboardScreen;
```

```markdown
# screens/TrackScreen.js
```javascript
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

const primaryColor = '#2E7D32';
const secondaryColor = '#A5D6A7';
const textColor = '#424242';
const backgroundColor = '#F5F5F5';

const TrackScreen = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Track</Text>
      <Text style={styles.text}>Log your activities to track your impact.</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: backgroundColor,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: primaryColor,
    marginBottom: 10,
  },
   text: {
    fontSize: 16,
    color: textColor,
  },
});

export default TrackScreen;
```

```markdown
# screens/ChallengesScreen.js
```javascript
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

const primaryColor = '#2E7D32';
const secondaryColor = '#A5D6A7';
const textColor = '#424242';
const backgroundColor = '#F5F5F5';

const ChallengesScreen = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Challenges</Text>
      <Text style={styles.text}>Participate in challenges to reduce your footprint!</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: backgroundColor,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: primaryColor,
    marginBottom: 10,
  },
   text: {
    fontSize: 16,
    color: textColor,
  },
});

export default ChallengesScreen;
```

```markdown
# screens/DiscoverScreen.js
```javascript
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

const primaryColor = '#2E7D32';
const secondaryColor = '#A5D6A7';
const textColor = '#424242';
const backgroundColor = '#F5F5F5';

const DiscoverScreen = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Discover</Text>
      <Text style={styles.text}>Find sustainable products and resources.</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: backgroundColor,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: primaryColor,
    marginBottom: 10,
  },
   text: {
    fontSize: 16,
    color: textColor,
  },
});

export default DiscoverScreen;
```

```markdown
# screens/ProfileScreen.js
```javascript
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

const primaryColor = '#2E7D32';
const secondaryColor = '#A5D6A7';
const textColor = '#424242';
const backgroundColor = '#F5F5F5';

const ProfileScreen = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Profile</Text>
      <Text style={styles.text}>Manage your profile and settings.</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: backgroundColor,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: primaryColor,
    marginBottom: 10,
  },
  text: {
    fontSize: 16,
    color: textColor,
  },
});

export default ProfileScreen;