
import React from 'react';
import { View, Text, Image, StyleSheet, FlatList } from 'react-native';
import KohImage from './assets/Koh.jpg'; // Make sure the path is correct
import PerthImage from './assets/Aus.jpg'; // Make sure the path is correct
import SantoriniImage from './assets/13.jpg'; // Make sure the path is correct

const photos = [
    { id: '1', name: 'Koh Samui', country: 'Thailand', image: 'https://kampatour.com/pic/blog/images/ks1.jpg' }, // Use the imported image
    { id: '2', name: 'Perth', country: 'Australia', image: PerthImage }, // Use the imported image
    { id: '3', name: 'Santorini', country: 'Greece', image: SantoriniImage }, // Use the imported image
    { id: '4', name: 'Santorini', country: 'Greece', image: SantoriniImage }, 
];

const DetailsScreen = ({ route }) => {
  const { place } = route.params;
  return (
    <View style={styles.container}>
      <Image source={KohImage} style={styles.mainImage} />
      <Text style={styles.title}>{place.name}</Text>
      <Text style={styles.subtitle}>{place.country}</Text>
      <Text style={styles.description}>
        Santorini is one of the Cyclades islands in the Aegean Sea. It was devastated by a volcanic eruption in the 16th century BC, forever shaping its rugged landscape.
      </Text>
      <FlatList
        data={photos}
        horizontal
        renderItem={({ item }) => (
          <Image source={{ uri: item.image }} style={styles.photo} />
        )}
        keyExtractor={(item) => item.id}
        style={styles.photoList}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' },
  mainImage: { width: '100%', height: 300, marginBottom: 16 },
  title: { fontSize: 32, fontWeight: 'bold', marginHorizontal: 16 },
  subtitle: { fontSize: 18, color: 'gray', marginHorizontal: 16, marginBottom: 8 },
  description: { fontSize: 16, marginHorizontal: 16, marginBottom: 16 },
  photo: { width: 100, height: 100, marginRight: 8, borderRadius: 8 },
  photoList: { paddingLeft: 16 },
});

export default DetailsScreen;