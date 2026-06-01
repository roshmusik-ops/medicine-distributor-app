# Medicine Distributor App

Free medicine distributor search app for Kerala. Find distributors, medicines, and prices instantly.

## Features

✅ **Free & Unlimited Search** — No subscription, no limits  
✅ **Web App** — React-based responsive design  
✅ **Android App** — React Native for mobile  
✅ **Real-time Search** — Find distributors by name or location  
✅ **Direct Contact** — Call distributors directly from the app  

## Tech Stack

- **Backend:** Node.js + Express
- **Web Frontend:** React + Tailwind CSS
- **Mobile:** React Native + Expo
- **Data Scraping:** Python + BeautifulSoup
- **Database:** JSON (can upgrade to PostgreSQL)

## Setup

### 1. Install Dependencies

```bash
npm install
pip install -r requirements.txt
```

### 2. Scrape Distributor Data

```bash
python scraper.py
```

This creates `data/distributors.json` with Kerala distributors.

### 3. Start Backend API

```bash
npm start
# or for development with auto-reload
npm run dev
```

API runs on `http://localhost:5000`

### 4. Start Web App

```bash
npm run web
```

Opens on `http://localhost:3000`

### 5. Start Android App

```bash
npm run native
```

Use Expo Go app to scan QR code.

## API Endpoints

- `GET /api/distributors` — Get all distributors
- `GET /api/search?q=query` — Search distributors
- `GET /api/distributors/:id` — Get distributor details
- `GET /api/health` — Health check

## Project Structure

```
medicine-distributor-app/
├── server.js              # Express API
├── scraper.py             # Pharmapps scraper
├── App.jsx                # React web app
├── App.native.jsx         # React Native app
├── package.json           # Node dependencies
├── requirements.txt       # Python dependencies
├── data/
│   └── distributors.json  # Distributor database
└── README.md
```

## Future Enhancements

- [ ] Medicine catalog search
- [ ] Price comparison
- [ ] Order placement
- [ ] Delivery tracking
- [ ] User accounts
- [ ] Reviews & ratings
- [ ] Payment integration

## License

MIT

## Contact

For issues or suggestions, contact: rosh.musik@gmail.com
