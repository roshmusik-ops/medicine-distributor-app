# Deployment Guide

## Overview

This guide covers deploying the Medicine Distributor App to production:
- **Backend API** → Heroku / Railway
- **Web App** → Netlify / Vercel
- **Android App** → Google Play Store

---

## 1. Backend API Deployment (Heroku)

### Prerequisites
- Heroku account (free tier available)
- Heroku CLI installed

### Steps

```bash
# Login to Heroku
heroku login

# Create Heroku app
heroku create medicine-distributor-api

# Deploy
git push heroku main

# View logs
heroku logs --tail
```

### Environment Variables
```bash
heroku config:set NODE_ENV=production
heroku config:set PORT=5000
```

### API URL
```
https://medicine-distributor-api.herokuapp.com/api
```

---

## 2. Web App Deployment (Netlify)

### Prerequisites
- Netlify account
- GitHub repo connected

### Steps

1. **Connect GitHub**
   - Go to Netlify
   - Click "New site from Git"
   - Select your GitHub repo

2. **Configure Build**
   - Build command: `npm run build`
   - Publish directory: `build`

3. **Environment Variables**
   - `REACT_APP_API_URL=https://medicine-distributor-api.herokuapp.com/api`

4. **Deploy**
   - Netlify auto-deploys on push to main

### Site URL
```
https://medicine-distributor.netlify.app
```

---

## 3. Android App Deployment (Google Play Store)

### Prerequisites
- Google Play Developer account ($25)
- Android keystore file
- App signing certificate

### Steps

#### 3.1 Create Keystore
```bash
keytool -genkey -v -keystore my-release-key.keystore \
  -keyalg RSA -keysize 2048 -validity 10000 \
  -alias my-key-alias
```

#### 3.2 Build Signed APK
```bash
eas build --platform android --type app-signing
```

#### 3.3 Upload to Google Play

1. **Create Google Play Account**
   - Go to [Google Play Console](https://play.google.com/console)
   - Pay $25 registration fee
   - Create new app

2. **Fill App Details**
   - App name: "Medicine Distributor"
   - Category: Medical
   - Content rating: Fill questionnaire
   - Privacy policy: Add link

3. **Upload APK/AAB**
   - Go to "Release" → "Production"
   - Upload signed APK or AAB
   - Add release notes

4. **Add Screenshots**
   - 2-8 screenshots (1080x1920px)
   - Show search, results, contact features

5. **Submit for Review**
   - Review takes 24-48 hours
   - App goes live after approval

### Play Store URL
```
https://play.google.com/store/apps/details?id=com.rosh.medicinedistributor
```

---

## 4. Database Setup (Optional)

### PostgreSQL (Production)

```bash
# Create database
createdb medicine_distributor

# Connect from app
DATABASE_URL=postgresql://user:pass@localhost/medicine_distributor
```

### MongoDB Atlas (Cloud)

```bash
# Create cluster
# Get connection string
MONGODB_URI=mongodb+srv://user:pass@cluster.mongodb.net/medicine_distributor
```

---

## 5. Domain Setup

### Custom Domain

1. **Buy domain** (GoDaddy, Namecheap, etc.)
2. **Point to Netlify**
   - Add DNS records
   - Or use Netlify nameservers

3. **SSL Certificate**
   - Netlify auto-generates free SSL
   - Enable HTTPS

### Example
```
medicine-distributor.in → Netlify
api.medicine-distributor.in → Heroku
```

---

## 6. Monitoring & Analytics

### Backend Monitoring
```bash
# Heroku logs
heroku logs --tail

# Error tracking (Sentry)
npm install @sentry/node
```

### Web Analytics
```javascript
// Google Analytics
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_ID"></script>
```

### App Analytics
```javascript
// Expo Analytics
import * as Analytics from 'expo-analytics';
```

---

## 7. CI/CD Pipeline

### GitHub Actions

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-node@v2
      - run: npm install
      - run: npm run build
      - run: npm test
      - name: Deploy to Heroku
        uses: akhileshns/heroku-deploy@v3.12.12
        with:
          heroku_api_key: ${{ secrets.HEROKU_API_KEY }}
          heroku_app_name: medicine-distributor-api
          heroku_email: your-email@gmail.com
```

---

## 8. Checklist

- [ ] Backend deployed to Heroku
- [ ] Web app deployed to Netlify
- [ ] Android app on Google Play Store
- [ ] Custom domain configured
- [ ] SSL certificate enabled
- [ ] Environment variables set
- [ ] Database connected
- [ ] Monitoring enabled
- [ ] CI/CD pipeline working
- [ ] Analytics tracking

---

## 9. Post-Launch

### Marketing
- Social media posts
- App store optimization (ASO)
- Press release
- Email campaign

### Support
- Monitor user feedback
- Fix bugs quickly
- Update regularly
- Respond to reviews

### Growth
- Feature requests
- User analytics
- A/B testing
- Performance optimization

---

## Support

For deployment issues: rosh.musik@gmail.com
