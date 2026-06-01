#!/bin/bash

echo "🚀 Medicine Distributor App - Setup"
echo "===================================="

# Install Node dependencies
echo "📦 Installing Node dependencies..."
npm install

# Install Python dependencies
echo "🐍 Installing Python dependencies..."
pip install -r requirements.txt

# Create data directory
mkdir -p data

# Scrape distributor data
echo "🔍 Scraping distributor data..."
python scraper.py

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Start backend:  npm start"
echo "2. Start Android:  npm run android"
echo "3. Or use Expo:    npm run native"
echo ""
