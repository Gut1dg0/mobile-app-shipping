# Flutter App — Setup & Run Instructions

## Prerequisites

1. **Flutter SDK** (3.x or later)
   Install: https://docs.flutter.dev/get-started/install
   Verify:  `flutter doctor`

2. An **Android emulator** (via Android Studio) or a connected physical device.
   iOS testing requires macOS + Xcode.

## Steps

```bash
# 1 — Navigate into the generated project
cd flutter_app

# 2 — Fetch all dependencies declared in pubspec.yaml
flutter pub get

# 3 — Run the app (picks the first available device/emulator)
flutter run

# To target a specific platform:
flutter run -d android   # Android emulator or device
flutter run -d ios       # iOS simulator (macOS only)
flutter run -d chrome    # Web (if web support is enabled)
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `flutter doctor` reports issues | Follow the doctor's recommendations |
| No devices found | Start an emulator in Android Studio or connect a device |
| Dependency errors | Run `flutter pub upgrade` then retry `flutter run` |
| Build errors | Check that your Flutter SDK version satisfies `sdk: '>=3.0.0 <4.0.0'` |

## Project Structure

```
flutter_app/
  pubspec.yaml        — project manifest & dependencies
  lib/
    main.dart         — app entry point
    screens/          — one file per screen
    widgets/          — reusable widget components
```
