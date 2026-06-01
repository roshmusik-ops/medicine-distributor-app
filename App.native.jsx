/**
 * Medicine Distributor App - Android/React Native
 */

import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  ScrollView,
  ActivityIndicator,
  StyleSheet,
  SafeAreaView,
  Linking,
} from 'react-native';

const API_URL = 'http://localhost:5000/api';

export default function App() {
  const [distributors, setDistributors] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [hasSearched, setHasSearched] = useState(false);

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

  const handleSearch = async () => {
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

  const DistributorCard = ({ distributor }) => (
    <View style={styles.card}>
      <Text style={styles.cardTitle}>{distributor.name}</Text>
      
      <View style={styles.cardRow}>
        <Text style={styles.cardLabel}>📍 Location:</Text>
        <Text style={styles.cardValue}>{distributor.location || 'Kerala'}</Text>
      </View>

      <View style={styles.cardRow}>
        <Text style={styles.cardLabel}>📞 Phone:</Text>
        <TouchableOpacity onPress={() => Linking.openURL(`tel:${distributor.phone}`)}>
          <Text style={styles.cardPhone}>{distributor.phone || 'N/A'}</Text>
        </TouchableOpacity>
      </View>

      <View style={styles.cardRow}>
        <Text style={styles.cardLabel}>🏛️ State:</Text>
        <Text style={styles.cardValue}>{distributor.state}</Text>
      </View>

      <TouchableOpacity style={styles.callButton}>
        <Text style={styles.callButtonText}>Call Now</Text>
      </TouchableOpacity>
    </View>
  );

  return (
    <SafeAreaView style={styles.container}>
      {/* Header */}
      <View style={styles.header}>
        <Text style={styles.headerTitle}>💊 Medicine Distributor</Text>
        <Text style={styles.headerSubtitle}>Find distributors in Kerala</Text>
      </View>

      {/* Search Bar */}
      <View style={styles.searchContainer}>
        <TextInput
          style={styles.searchInput}
          placeholder="Search by name or location..."
          value={searchQuery}
          onChangeText={setSearchQuery}
          placeholderTextColor="#999"
        />
        <TouchableOpacity style={styles.searchButton} onPress={handleSearch}>
          <Text style={styles.searchButtonText}>Search</Text>
        </TouchableOpacity>
      </View>

      <Text style={styles.resultCount}>
        {displayData.length} distributor{displayData.length !== 1 ? 's' : ''} found
      </Text>

      {/* Loading */}
      {loading && (
        <View style={styles.centerContainer}>
          <ActivityIndicator size="large" color="#4F46E5" />
          <Text style={styles.loadingText}>Loading...</Text>
        </View>
      )}

      {/* Results */}
      {!loading && displayData.length > 0 && (
        <ScrollView style={styles.resultsList} showsVerticalScrollIndicator={false}>
          {displayData.map((distributor, index) => (
            <DistributorCard key={index} distributor={distributor} />
          ))}
        </ScrollView>
      )}

      {/* Empty State */}
      {!loading && displayData.length === 0 && hasSearched && (
        <View style={styles.centerContainer}>
          <Text style={styles.emptyText}>No distributors found</Text>
          <TouchableOpacity
            style={styles.clearButton}
            onPress={() => {
              setSearchQuery('');
              setHasSearched(false);
            }}
          >
            <Text style={styles.clearButtonText}>Clear Search</Text>
          </TouchableOpacity>
        </View>
      )}
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F3F4F6',
  },
  header: {
    backgroundColor: '#FFFFFF',
    paddingVertical: 16,
    paddingHorizontal: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#E5E7EB',
  },
  headerTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#4F46E5',
  },
  headerSubtitle: {
    fontSize: 14,
    color: '#666',
    marginTop: 4,
  },
  searchContainer: {
    flexDirection: 'row',
    padding: 16,
    gap: 8,
  },
  searchInput: {
    flex: 1,
    borderWidth: 1,
    borderColor: '#D1D5DB',
    borderRadius: 8,
    paddingHorizontal: 12,
    paddingVertical: 10,
    fontSize: 14,
    backgroundColor: '#FFFFFF',
  },
  searchButton: {
    backgroundColor: '#4F46E5',
    paddingHorizontal: 16,
    borderRadius: 8,
    justifyContent: 'center',
  },
  searchButtonText: {
    color: '#FFFFFF',
    fontWeight: '600',
  },
  resultCount: {
    paddingHorizontal: 16,
    fontSize: 12,
    color: '#666',
    marginBottom: 8,
  },
  resultsList: {
    flex: 1,
    paddingHorizontal: 16,
  },
  card: {
    backgroundColor: '#FFFFFF',
    borderRadius: 8,
    padding: 16,
    marginBottom: 12,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  cardTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#1F2937',
    marginBottom: 12,
  },
  cardRow: {
    flexDirection: 'row',
    marginBottom: 8,
    alignItems: 'center',
  },
  cardLabel: {
    fontSize: 14,
    fontWeight: '600',
    color: '#4B5563',
    width: 100,
  },
  cardValue: {
    fontSize: 14,
    color: '#1F2937',
    flex: 1,
  },
  cardPhone: {
    fontSize: 14,
    color: '#4F46E5',
    textDecorationLine: 'underline',
    flex: 1,
  },
  callButton: {
    backgroundColor: '#4F46E5',
    paddingVertical: 10,
    borderRadius: 6,
    marginTop: 12,
    alignItems: 'center',
  },
  callButtonText: {
    color: '#FFFFFF',
    fontWeight: '600',
    fontSize: 14,
  },
  centerContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  loadingText: {
    marginTop: 12,
    fontSize: 16,
    color: '#666',
  },
  emptyText: {
    fontSize: 18,
    color: '#666',
    marginBottom: 16,
  },
  clearButton: {
    backgroundColor: '#4F46E5',
    paddingHorizontal: 24,
    paddingVertical: 12,
    borderRadius: 6,
  },
  clearButtonText: {
    color: '#FFFFFF',
    fontWeight: '600',
  },
});
