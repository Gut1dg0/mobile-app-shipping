```markdown
# App.js
```javascript
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { Ionicons } from '@expo/vector-icons';

// Screens
import DashboardScreen from './src/screens/DashboardScreen';
import BudgetsScreen from './src/screens/BudgetsScreen';
import TransactionsScreen from './src/screens/TransactionsScreen';
import GoalsScreen from './src/screens/GoalsScreen';
import ProfileScreen from './src/screens/ProfileScreen';

const Tab = createBottomTabNavigator();

const screenOptions = ({ route }) => ({
  tabBarIcon: ({ focused, color, size }) => {
    let iconName;

    if (route.name === 'Dashboard') {
      iconName = focused ? 'ios-home' : 'ios-home-outline';
    } else if (route.name === 'Budgets') {
      iconName = focused ? 'ios-list' : 'ios-list-outline';
    } else if (route.name === 'Transactions') {
      iconName = focused ? 'ios-cash' : 'ios-cash-outline';
    } else if (route.name === 'Goals') {
      iconName = focused ? 'ios-flag' : 'ios-flag-outline';
    } else if (route.name === 'Profile') {
      iconName = focused ? 'ios-person' : 'ios-person-outline';
    }

    // You can return any component that you like here!
    return <Ionicons name={iconName} size={size} color={color} accessibilityLabel={route.name} />;
  },
  tabBarActiveTintColor: '#2E94B9',
  tabBarInactiveTintColor: 'gray',
});

export default function App() {
  return (
    <View style={styles.container}>
      <StatusBar style="auto" />
      <NavigationContainer>
        <Tab.Navigator
          screenOptions={screenOptions}
        >
          <Tab.Screen name="Dashboard" component={DashboardScreen} />
          <Tab.Screen name="Budgets" component={BudgetsScreen} />
          <Tab.Screen name="Transactions" component={TransactionsScreen} />
          <Tab.Screen name="Goals" component={GoalsScreen} />
          <Tab.Screen name="Profile" component={ProfileScreen} />
        </Tab.Navigator>
      </NavigationContainer>
    </View>
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
# src/screens/DashboardScreen.js
```javascript
import React from 'react';
import { StyleSheet, View, Text } from 'react-native';

const DashboardScreen = () => {
  return (
    <View style={styles.container}>
      <Text>Dashboard Screen</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default DashboardScreen;
```

```markdown
# src/screens/BudgetsScreen.js
```javascript
import React from 'react';
import { StyleSheet, View, Text } from 'react-native';

const BudgetsScreen = () => {
  return (
    <View style={styles.container}>
      <Text>Budgets Screen</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default BudgetsScreen;
```

```markdown
# src/screens/TransactionsScreen.js
```javascript
import React from 'react';
import { StyleSheet, View, Text } from 'react-native';

const TransactionsScreen = () => {
  return (
    <View style={styles.container}>
      <Text>Transactions Screen</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default TransactionsScreen;
```

```markdown
# src/screens/GoalsScreen.js
```javascript
import React from 'react';
import { StyleSheet, View, Text } from 'react-native';

const GoalsScreen = () => {
  return (
    <View style={styles.container}>
      <Text>Goals Screen</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default GoalsScreen;
```

```markdown
# src/screens/ProfileScreen.js
```javascript
import React from 'react';
import { StyleSheet, View, Text } from 'react-native';

const ProfileScreen = () => {
  return (
    <View style={styles.container}>
      <Text>Profile Screen</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default ProfileScreen;
```