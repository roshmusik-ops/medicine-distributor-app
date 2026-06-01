# Android App Build Guide

## Prerequisites

1. **Node.js** (v16+) — [Download](https://nodejs.org/)
2. **Expo CLI** — `npm install -g expo-cli`
3. **Android Studio** (optional, for emulator)
4. **Expo Go App** (on your phone) — [Download from Play Store](https://play.google.com/store/apps/details?id=host.exp.exponent)

## Quick Start (Development)

### 1. Install Dependencies
```bash
npm install
```

### 2. Start Expo Server
```bash
npm run native
```

### 3. Run on Android
**Option A: Using Expo Go (Easiest)**
- Scan QR code with your phone's camera
- Open link in Expo Go app
- App loads instantly

**Option B: Using Android Emulator**
```bash
npm run android
```

## Build APK (For Distribution)

### 1. Create Expo Account
```bash
expo login
# or
eas login
```

### 2. Build APK
```bash
eas build --platform android --local
```

### 3. Download APK
- APK will be generated and ready to install
- Install on your Android phone via USB or download link

## Build AAB (For Google Play Store)

### 1. Configure app.json
```json
{
  "expo": {
    "android": {
      "package": "com.rosh.medicinedistributor",
      "versionCode": 1
    }
  }
}
```

### 2. Build AAB
```bash
eas build --platform android
```

### 3. Upload to Google Play Console
- Create Google Play Developer account ($25 one-time)
- Upload AAB to Google Play Console
- Fill in app details, screenshots, description
- Submit for review (24-48 hours)

## Project Structure

```
medicine-distributor-app/
├── App.native.jsx          # Main app component
├── app.json                # Expo config
├── index.js                # Entry point
├── babel.config.js         # Babel config
├── package.json            # Dependencies
├── assets/                 # Icons, splash screen
│   ├── icon.png
│   ├── splash.png
│   └── adaptive-icon.png
└── data/
    └── distributors.json   # Distributor database
```

## Features

✅ Search medicine distributors  
✅ View distributor details  
✅ Call directly from app  
✅ Location-based search  
✅ Offline support (cached data)  

## Troubleshooting

### App won't start
```bash
npm install
expo start --clear
```

### Can't connect to backend
- Make sure backend is running: `npm start`
- Update API_URL in App.native.jsx
- Check firewall settings

### Build fails
```bash
rm -rf node_modules package-lock.json
npm install
npm run android
```

## API Configuration

Update `App.native.jsx` to point to your backend:

```javascript
const API_URL = 'http://YOUR_BACKEND_URL/api';
```

For local testing:
```javascript
const API_URL = 'http://192.168.x.x:5000/api';  // Your machine IP
```

## Next Steps

1. ✅ Test on phone with Expo Go
2. ✅ Build APK for distribution
3. ✅ Submit to Google Play Store
4. ✅ Market on social media

## Support

For issues: rosh.musik@gmail.com
