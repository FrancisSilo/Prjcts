// PopularPlacesScreen.js
import React, { useState } from 'react';
import { View, Text, StyleSheet, FlatList, Image, TouchableOpacity, TextInput } from 'react-native';
import KohImage from './assets/Koh.jpg'; // Ensure the path is correct
import PerthImage from './assets/Aus.jpg'; // Ensure the path is correct
import SantoriniImage from './assets/13.jpg'; // Ensure the path is correct

const places = [
  { id: '1', name: 'Koh Samui', country: 'Thailand', image: KohImage },
  { id: '2', name: 'Perth', country: 'Australia', image: PerthImage },
  { id: '3', name: 'Santorini', country: 'Greece', image: SantoriniImage },
  { id: '4', name: 'Mykonos', country: 'Greece', image: SantoriniImage },
];

const PopularPlacesScreen = ({ navigation }) => {
  const [searchQuery, setSearchQuery] = useState('');

  // Function to filter places based on the search query
  const filteredPlaces = places.filter(place =>
    place.name.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Find your perfect place to travel.</Text>

      <TextInput
        style={styles.searchBar}
        placeholder="Search..."
        value={searchQuery}
        onChangeText={setSearchQuery} // Update search query
      />

      <FlatList
        data={filteredPlaces} // Use filtered places
        horizontal
        renderItem={({ item }) => (
          <TouchableOpacity onPress={() => navigation.navigate('Details', { place: item })}>
            <View style={styles.placeContainer}>
              <Image source={item.image} style={styles.placeImage} />
              <Text style={styles.placeName}>{item.name}</Text>
              <Text style={styles.placeCountry}>{item.country}</Text>
            </View>
          </TouchableOpacity>
        )}
        keyExtractor={(item) => item.id}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, padding: 16, backgroundColor: '#fff' },
  title: { fontSize: 24, fontWeight: 'bold', marginBottom: 20 },
  searchBar: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    borderRadius: 8,
    paddingHorizontal: 10,
    marginBottom: 20,
    backgroundColor: '#fff',
  },
  placeContainer: { marginRight: 16 },
  placeImage: { width: 150, height: 150, borderRadius: 8 },
  placeName: { fontSize: 16, fontWeight: 'bold', marginTop: 8 },
  placeCountry: { fontSize: 14, color: 'gray' },
});

export default PopularPlacesScreen;
