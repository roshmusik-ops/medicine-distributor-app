/**
 * Medicine Distributor App - Backend API
 * Node.js + Express
 */

const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(express.json());

// Load distributor data
const distributorsFile = path.join(__dirname, 'data', 'distributors.json');
let distributors = [];

try {
  const data = fs.readFileSync(distributorsFile, 'utf-8');
  distributors = JSON.parse(data);
  console.log(`Loaded ${distributors.length} distributors`);
} catch (err) {
  console.log('Distributor data not found. Using empty array.');
}

// Routes

// Get all distributors
app.get('/api/distributors', (req, res) => {
  res.json({
    success: true,
    count: distributors.length,
    data: distributors
  });
});

// Search distributors by name or location
app.get('/api/search', (req, res) => {
  const { q } = req.query;
  
  if (!q) {
    return res.json({
      success: false,
      message: 'Search query required'
    });
  }

  const query = q.toLowerCase();
  const results = distributors.filter(d => 
    d.name.toLowerCase().includes(query) ||
    d.location.toLowerCase().includes(query)
  );

  res.json({
    success: true,
    query,
    count: results.length,
    data: results
  });
});

// Get distributor by ID
app.get('/api/distributors/:id', (req, res) => {
  const distributor = distributors[req.params.id];
  
  if (!distributor) {
    return res.status(404).json({
      success: false,
      message: 'Distributor not found'
    });
  }

  res.json({
    success: true,
    data: distributor
  });
});

// Health check
app.get('/api/health', (req, res) => {
  res.json({
    success: true,
    message: 'API is running',
    distributors: distributors.length
  });
});

// Error handling
app.use((err, req, res, next) => {
  console.error(err);
  res.status(500).json({
    success: false,
    message: 'Internal server error'
  });
});

// Start server
app.listen(PORT, () => {
  console.log(`Medicine Distributor API running on port ${PORT}`);
  console.log(`Health check: http://localhost:${PORT}/api/health`);
});
