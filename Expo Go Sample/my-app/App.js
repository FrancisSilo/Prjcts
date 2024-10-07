import React, { useState } from 'react';
import {
  StyleSheet,
  Text,
  View,
  Button,
  Image,
  FlatList,
  SafeAreaView,
  SectionList,
  StatusBar,
  Modal,
  TouchableOpacity,
} from 'react-native';

// Sample data for the FlatList
const FLATLIST_DATA = [
  { id: '1', title: 'Item 1', image: require('./assets/st.jpg') }, // Replace with your image paths
];

// Sample data for the SectionList
const SECTION_DATA = [
  {
    title: 'Hobbies',
    data: ['Gaming', 'Coding', 'Pizza'],
  },
];

const App = () => {
  const [showList, setShowList] = useState(false); // State to control FlatList visibility
  const [modalVisible, setModalVisible] = useState(false); // State for modal visibility

  const onPressShowList = () => {
    setShowList(true); // Show the FlatList when the button is pressed
  };

  const showMessageBox = () => {
    setModalVisible(true); // Show the modal with the image
  };

  // Render each item in the FlatList
  const renderFlatListItem = ({ item }) => (
    <View style={styles.itemContainer}>
      <Image source={item.image} style={styles.image} />
      <Text style={styles.itemTitle}>{item.title}</Text>
    </View>
  );

  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.title}>Nikmary Francis A. Silorio</Text>
      <Image
        source={require('./assets/Profile.jpg')} // Replace with your image path
        style={styles.profileImage}
      />
      {showList && ( // Conditional rendering of FlatList
        <FlatList
          data={FLATLIST_DATA}
          renderItem={renderFlatListItem}
          keyExtractor={item => item.id}
          contentContainerStyle={styles.list}
        />
      )}
      <SectionList
        sections={SECTION_DATA}
        keyExtractor={(item, index) => item + index}
        renderItem={({ item }) => (
          <View style={styles.item}>
            <Text style={styles.hobbyTitle}>{item}</Text>
          </View>
        )}
        renderSectionHeader={({ section: { title } }) => (
          <Text style={styles.header}>{title}</Text>
        )}
      />
      <Button
        onPress={showMessageBox}
        title="Show Message Box"
        color="#841584"
        accessibilityLabel="Show a message box with an image"
      />
      
      {/* Modal for the message box */}
      <Modal
        animationType="slide"
        transparent={true}
        visible={modalVisible}
        onRequestClose={() => setModalVisible(!modalVisible)}
      >
        <View style={styles.modalContainer}>
          <View style={styles.modalContent}>
            <Text style={styles.modalTitle}>Naay Ayuda Diri</Text>
            <Image
              source={require('./assets/my.png')} // Replace with your image path
              style={styles.modalImage}
            />
            <TouchableOpacity
              style={styles.closeButton}
              onPress={() => setModalVisible(false)}
            >
              <Text style={styles.closeButtonText}>Close</Text>
            </TouchableOpacity>
          </View>
        </View>
      </Modal>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#282c34',
    paddingTop: StatusBar.currentHeight,
    marginHorizontal: 16,
    alignItems: 'center',
  },
  title: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#61dafb',
    textAlign: 'center',
    marginBottom: 10,
  },
  profileImage: {
    width: 200, // Set your desired width
    height: 200, // Set your desired height
    marginBottom: 20,
    borderWidth: 2,
    borderColor: '#61dafb', // Optional: add border color
  },
  list: {
    alignItems: 'center',
    width: 300, // Match the profile image width
  },
  itemContainer: {
    alignItems: 'center',
    marginVertical: 10,
    width: '100%', // Ensure items take full width of FlatList
  },
  image: {
    width: 100, // Set your desired width for FlatList items
    height: 100, // Set your desired height for FlatList items
    borderRadius: 50, // Half of the width/height for a circular image
    marginBottom: 5,
  },
  item: {
    backgroundColor: '#61dafb',
    padding: 20,
    marginVertical: 8,
    width: '100%', // Full width for section items
  },
  header: {
    fontSize: 32,
    backgroundColor: '#fff',
    padding: 5,
  },
  itemTitle: {
    fontSize: 18,
    color: '#000',
  },
  hobbyTitle: {
    fontSize: 24,
    color: '#282c34', // Dark color for contrast
  },
  modalContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'rgba(0, 0, 0, 0.5)', // Semi-transparent background
  },
  modalContent: {
    width: 300,
    padding: 20,
    backgroundColor: 'white',
    borderRadius: 10,
    alignItems: 'center',
    elevation: 5,
  },
  modalTitle: {
    fontSize: 24,
    marginBottom: 10,
  },
  modalImage: {
    width: 150,
    height: 150,
    borderRadius: 75,
    marginBottom: 10,
  },
  closeButton: {
    backgroundColor: '#61dafb',
    padding: 10,
    borderRadius: 5,
  },
  closeButtonText: {
    color: '#fff',
    fontSize: 16,
  },
});

export default App;
