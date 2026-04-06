

=== FILE: pubspec.yaml ===
name: puzzle_pal
description: PuzzlePal - A Comprehensive Puzzle Game Mobile App
version: 1.0.0+1

environment:
  sdk: '>=3.0.0 <4.0.0'

dependencies:
  flutter:
    sdk: flutter
  provider: ^6.1.1
  go_router: ^14.2.0
  shared_preferences: ^2.2.2
  google_fonts: ^6.1.0

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^3.0.1

flutter:
  uses-material-design: true
=== END FILE ===

=== FILE: lib/main.dart ===
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:puzzle_pal/providers/theme_provider.dart';
import 'package:puzzle_pal/providers/auth_provider.dart';
import 'package:puzzle_pal/router.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => ThemeProvider()),
        ChangeNotifierProvider(create: (_) => AuthProvider()),
      ],
      child: const PuzzlePalApp(),
    ),
  );
}

class PuzzlePalApp extends StatelessWidget {
  const PuzzlePalApp({super.key});

  @override
  Widget build(BuildContext context) {
    final themeProvider = context.watch<ThemeProvider>();
    return MaterialApp.router(
      title: 'PuzzlePal',
      debugShowCheckedModeBanner: false,
      theme: themeProvider.lightTheme,
      darkTheme: themeProvider.darkTheme,
      themeMode: themeProvider.themeMode,
      routerConfig: appRouter(context.read<AuthProvider>()),
    );
  }
}
=== END FILE ===

=== FILE: lib/router.dart ===
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:puzzle_pal/providers/auth_provider.dart';
import 'package:puzzle_pal/screens/login_screen.dart';
import 'package:puzzle_pal/screens/shell_screen.dart';
import 'package:puzzle_pal/screens/home_screen.dart';
import 'package:puzzle_pal/screens/explore_screen.dart';
import 'package:puzzle_pal/screens/daily_screen.dart';
import 'package:puzzle_pal/screens/leaderboard_screen.dart';
import 'package:puzzle_pal/screens/profile_screen.dart';
import 'package:puzzle_pal/screens/settings_screen.dart';

GoRouter appRouter(AuthProvider authProvider) {
  return GoRouter(
    initialLocation: '/login',
    refreshListenable: authProvider,
    redirect: (BuildContext context, GoRouterState state) {
      final isLoggedIn = authProvider.isLoggedIn;
      final isLoggingIn = state.matchedLocation == '/login';

      if (!isLoggedIn && !isLoggingIn) {
        return '/login';
      }
      if (isLoggedIn && isLoggingIn) {
        return '/home';
      }
      return null;
    },
    routes: [
      GoRoute(
        path: '/login',
        builder: (context, state) => const LoginScreen(),
      ),
      ShellRoute(
        builder: (context, state, child) => ShellScreen(child: child),
        routes: [
          GoRoute(
            path: '/home',
            pageBuilder: (context, state) => const NoTransitionPage(
              child: HomeScreen(),
            ),
          ),
          GoRoute(
            path: '/explore',
            pageBuilder: (context, state) => const NoTransitionPage(
              child: ExploreScreen(),
            ),
          ),
          GoRoute(
            path: '/daily',
            pageBuilder: (context, state) => const NoTransitionPage(
              child: DailyScreen(),
            ),
          ),
          GoRoute(
            path: '/leaderboard',
            pageBuilder: (context, state) => const NoTransitionPage(
              child: LeaderboardScreen(),
            ),
          ),
          GoRoute(
            path: '/profile',
            pageBuilder: (context, state) => const NoTransitionPage(
              child: ProfileScreen(),
            ),
          ),
        ],
      ),
      GoRoute(
        path: '/settings',
        builder: (context, state) => const SettingsScreen(),
      ),
    ],
  );
}
=== END FILE ===

=== FILE: lib/theme/app_colors.dart ===
import 'package:flutter/material.dart';

class AppColors {
  static const Color deepIndigo = Color(0xFF3D2B8E);
  static const Color electricViolet = Color(0xFF7B4FD4);
  static const Color tealGlow = Color(0xFF00C9B1);
  static const Color amberSpark = Color(0xFFFFB830);

  static const Color deepSpace = Color(0xFF0F0E1A);
  static const Color midnightCard = Color(0xFF1C1A2E);
  static const Color softSlate = Color(0xFF252340);
  static const Color ghostLine = Color(0xFF2E2B4A);

  static const Color softLavenderWhite = Color(0xFFF4F2FF);
  static const Color pureWhite = Color(0xFFFFFFFF);
  static const Color lightGray = Color(0xFFEDEBF8);
  static const Color paleViolet = Color(0xFFD5D0F0);

  static const Color success = Color(0xFF00C9B1);
  static const Color warning = Color(0xFFFFB830);
  static const Color error = Color(0xFFFF4F6E);
  static const Color info = Color(0xFF5BB8FF);
  static const Color premiumGold = Color(0xFFF5C518);

  static const Color inactive = Color(0xFF6B6880);

  static const Color deepIndigoLight = Color(0xB33D2B8E);
  static const Color deepIndigoMedium = Color(0x803D2B8E);

  static const LinearGradient heroGradient = LinearGradient(
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
    colors: [deepIndigo, electricViolet, tealGlow],
  );

  static const LinearGradient cardAccentGradient = LinearGradient(
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
    colors: [deepIndigo, Color(0xFF5C3DBF)],
  );

  static const LinearGradient premiumGradient = LinearGradient(
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
    colors: [premiumGold, amberSpark],
  );

  static const LinearGradient dailyChallengeGradient = LinearGradient(
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
    colors: [deepIndigo, electricViolet],
  );
}
=== END FILE ===

=== FILE: lib/providers/theme_provider.dart ===
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:puzzle_pal/theme/app_colors.dart';

class ThemeProvider extends ChangeNotifier {
  ThemeMode _themeMode = ThemeMode.dark;

  ThemeMode get themeMode => _themeMode;

  bool get isDark => _themeMode == ThemeMode.dark;

  ThemeProvider() {
    _loadTheme();
  }

  Future<void> _loadTheme() async {
    final prefs = await SharedPreferences.getInstance();
    final isDarkMode = prefs.getBool('isDarkMode') ?? true;
    _themeMode = isDarkMode ? ThemeMode.dark : ThemeMode.light;
    notifyListeners();
  }

  Future<void> toggleTheme() async {
    _themeMode = isDark ? ThemeMode.light : ThemeMode.dark;
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool('isDarkMode', isDark);
    notifyListeners();
  }

  ThemeData get darkTheme {
    return ThemeData(
      brightness: Brightness.dark,
      scaffoldBackgroundColor: AppColors.deepSpace,
      primaryColor: AppColors.deepIndigo,
      colorScheme: const ColorScheme.dark(
        primary: AppColors.electricViolet,
        secondary: AppColors.tealGlow,
        surface: AppColors.midnightCard,
        error: AppColors.error,
      ),
      cardColor: AppColors.midnightCard,
      dividerColor: AppColors.ghostLine,
      appBarTheme: AppBarTheme(
        backgroundColor: AppColors.deepSpace,
        elevation: 0,
        centerTitle: true,
        titleTextStyle: GoogleFonts.nunito(
          fontSize: 24,
          fontWeight: FontWeight.w700,
          color: Colors.white,
        ),
        iconTheme: const IconThemeData(color: Colors.white),
      ),
      textTheme: TextTheme(
        headlineLarge: GoogleFonts.nunito(
          fontSize: 32,
          fontWeight: FontWeight.w800,
          color: Colors.white,
        ),
        headlineMedium: GoogleFonts.nunito(
          fontSize: 24,
          fontWeight: FontWeight.w700,
          color: Colors.white,
        ),
        headlineSmall: GoogleFonts.nunito(
          fontSize: 20,
          fontWeight: FontWeight.w700,
          color: Colors.white,
        ),
        bodyLarge: GoogleFonts.inter(
          fontSize: 16,
          fontWeight: FontWeight.w400,
          color: Colors.white,
        ),
        bodyMedium: GoogleFonts.inter(
          fontSize: 14,
          fontWeight: FontWeight.w400,
          color: Colors.white70,
        ),
        labelSmall: GoogleFonts.inter(
          fontSize: 12,
          fontWeight: FontWeight.w400,
          color: Colors.white54,
        ),
        labelLarge: GoogleFonts.inter(
          fontSize: 15,
          fontWeight: FontWeight.w600,
          color: Colors.white,
        ),
      ),
      inputDecorationTheme: InputDecorationTheme(
        filled: true,
        fillColor: AppColors.softSlate,
        contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 16),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
          borderSide: const BorderSide(color: AppColors.ghostLine),
        ),
        enabledBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
          borderSide: const BorderSide(color: AppColors.ghostLine),
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
          borderSide: const BorderSide(color: AppColors.electricViolet, width: 2),
        ),
        errorBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
          borderSide: const BorderSide(color: AppColors.error, width: 2),
        ),
        labelStyle: GoogleFonts.inter(
          fontSize: 14,
          color: AppColors.inactive,
        ),
        hintStyle: GoogleFonts.inter(
          fontSize: 16,
          color: Colors.white38,
        ),
      ),
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          backgroundColor: AppColors.electricViolet,
          foregroundColor: Colors.white,
          minimumSize: const Size(double.infinity, 52),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(100),
          ),
          textStyle: GoogleFonts.inter(
            fontSize: 15,
            fontWeight: FontWeight.w600,
          ),
          elevation: 4,
        ),
      ),
      outlinedButtonTheme: OutlinedButtonThemeData(
        style: OutlinedButton.styleFrom(
          foregroundColor: AppColors.electricViolet,
          minimumSize: const Size(double.infinity, 52),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(100),
          ),
          side: const BorderSide(color: AppColors.electricViolet, width: 1.5),
          textStyle: GoogleFonts.inter(
            fontSize: 15,
            fontWeight: FontWeight.w600,
          ),
        ),
      ),
      bottomNavigationBarTheme: const BottomNavigationBarThemeData(
        backgroundColor: AppColors.midnightCard,
        selectedItemColor: AppColors.electricViolet,
        unselectedItemColor: AppColors.inactive,
        type: BottomNavigationBarType.fixed,
        elevation: 0,
      ),
    );
  }

  ThemeData get lightTheme {
    return ThemeData(
      brightness: Brightness.light,
      scaffoldBackgroundColor: AppColors.softLavenderWhite,
      primaryColor: AppColors.deepIndigo,
      colorScheme: const ColorScheme.light(
        primary: AppColors.electricViolet,
        secondary: AppColors.tealGlow,
        surface: AppColors.pureWhite,
        error: AppColors.error,
      ),
      cardColor: AppColors.pureWhite,
      dividerColor: AppColors.paleViolet,
      appBarTheme: AppBarTheme(
        backgroundColor: AppColors.softLavenderWhite,
        elevation: 0,
        centerTitle: true,
        titleTextStyle: GoogleFonts.nunito(
          fontSize: 24,
          fontWeight: FontWeight.w700,
          color: AppColors.deepIndigo,
        ),
        iconTheme: const IconThemeData(color: AppColors.deepIndigo),
      ),
      textTheme: TextTheme(
        headlineLarge: GoogleFonts.nunito(
          fontSize: 32,
          fontWeight: FontWeight.w800,
          color: AppColors.deepIndigo,
        ),
        headlineMedium: GoogleFonts.nunito(
          fontSize: 24,
          fontWeight: FontWeight.w700,
          color: AppColors.deepIndigo,
        ),
        headlineSmall: GoogleFonts.nunito(
          fontSize: 20,
          fontWeight: FontWeight.w700,
          color: AppColors.deepIndigo,
        ),
        bodyLarge: GoogleFonts.inter(
          fontSize: 16,
          fontWeight: FontWeight.w400,
          color: AppColors.deepIndigo,
        ),
        bodyMedium: GoogleFonts.inter(
          fontSize: 14,
          fontWeight: FontWeight.w400,
          color: AppColors.deepIndigoLight,
        ),
        labelSmall: GoogleFonts.inter(
          fontSize: 12,
          fontWeight: FontWeight.w400,
          color: AppColors.deepIndigoMedium,
        ),
        labelLarge: GoogleFonts.inter(
          fontSize: 15,
          fontWeight: FontWeight.w600,
          color: AppColors.deepIndigo,
        ),
      ),
      inputDecorationTheme: InputDecorationTheme(
        filled: true,
        fillColor: AppColors.lightGray,
        contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical