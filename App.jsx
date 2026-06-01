/**
 * Medicine Distributor App - Web Frontend
 * React + Tailwind CSS
 */

import React, { useState, useEffect } from 'react';
import './App.css';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

function App() {
  const [distributors, setDistributors] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [hasSearched, setHasSearched] = useState(false);

  // Load all distributors on mount
  useEffect(() => {
    fetchDistributors();
  }, []);

  const fetchDistributors = async () => {
    try {
      setLoading(true);
      const response = await fetch(`${API_URL}/distributors`);
      const data = await response.json();
      if (data.success) {
        setDistributors(data.data);
      }
    } catch (err) {
      console.error('Error fetching distributors:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = async (e) => {
    e.preventDefault();
    
    if (!searchQuery.trim()) {
      setSearchResults([]);
      setHasSearched(false);
      return;
    }

    try {
      setLoading(true);
      setHasSearched(true);
      const response = await fetch(`${API_URL}/search?q=${encodeURIComponent(searchQuery)}`);
      const data = await response.json();
      if (data.success) {
        setSearchResults(data.data);
      }
    } catch (err) {
      console.error('Error searching:', err);
    } finally {
      setLoading(false);
    }
  };

  const displayData = hasSearched ? searchResults : distributors;

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      {/* Header */}
      <header className="bg-white shadow-md sticky top-0 z-50">
        <div className="max-w-6xl mx-auto px-4 py-6">
          <h1 className="text-3xl font-bold text-indigo-600">💊 Medicine Distributor</h1>
          <p className="text-gray-600 mt-1">Find medicine distributors in Kerala</p>
        </div>
      </header>

      {/* Search Section */}
      <div className="max-w-6xl mx-auto px-4 py-8">
        <form onSubmit={handleSearch} className="bg-white rounded-lg shadow-lg p-6 mb-8">
          <div className="flex gap-2">
            <input
              type="text"
              placeholder="Search by distributor name or location..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="flex-1 px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
            />
            <button
              type="submit"
              className="px-6 py-3 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition font-semibold"
            >
              Search
            </button>
          </div>
          <p className="text-sm text-gray-500 mt-2">
            {displayData.length} distributor{displayData.length !== 1 ? 's' : ''} found
          </p>
        </form>

        {/* Loading State */}
        {loading && (
          <div className="text-center py-12">
            <div className="inline-block animate-spin">
              <div className="w-12 h-12 border-4 border-indigo-200 border-t-indigo-600 rounded-full"></div>
            </div>
            <p className="mt-4 text-gray-600">Loading...</p>
          </div>
        )}

        {/* Results Grid */}
        {!loading && displayData.length > 0 && (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {displayData.map((distributor, index) => (
              <div key={index} className="bg-white rounded-lg shadow-md hover:shadow-lg transition p-6">
                <h3 className="text-xl font-bold text-gray-800 mb-2">{distributor.name}</h3>
                <div className="space-y-2 text-gray-600">
                  <p className="flex items-center gap-2">
                    <span className="text-lg">📍</span>
                    {distributor.location || 'Kerala'}
                  </p>
                  <p className="flex items-center gap-2">
                    <span className="text-lg">📞</span>
                    <a href={`tel:${distributor.phone}`} className="text-indigo-600 hover:underline">
                      {distributor.phone || 'N/A'}
                    </a>
                  </p>
                  <p className="flex items-center gap-2">
                    <span className="text-lg">🏛️</span>
                    {distributor.state}
                  </p>
                </div>
                <button className="mt-4 w-full bg-indigo-600 text-white py-2 rounded-lg hover:bg-indigo-700 transition font-semibold">
                  View Details
                </button>
              </div>
            ))}
          </div>
        )}

        {/* Empty State */}
        {!loading && displayData.length === 0 && hasSearched && (
          <div className="text-center py-12">
            <p className="text-xl text-gray-600">No distributors found for "{searchQuery}"</p>
            <button
              onClick={() => {
                setSearchQuery('');
                setHasSearched(false);
              }}
              className="mt-4 px-6 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition"
            >
              Clear Search
            </button>
          </div>
        )}
      </div>

      {/* Footer */}
      <footer className="bg-gray-800 text-white text-center py-6 mt-12">
        <p>Medicine Distributor App © 2026 | Free & Unlimited Search</p>
      </footer>
    </div>
  );
}

export default App;
