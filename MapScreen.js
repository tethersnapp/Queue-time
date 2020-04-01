import React,{useState,useEffect} from 'react';
import MapView,{PROVIDER_GOOGLE,Marker}  from 'react-native-maps';
import {Platform,StyleSheet,Text,View,Alert,TouchableOpacity,Dimensions,Button} from "react-native";
import MapMethods from './Methods'

const MapScreen= props=>{
  const mapstyle = require('./mapstyle.json');
  const [position,setPosition]=useState({lat:51.5074,long:0.1274,alt:null})
  const [initialRegion,setInitialRegion]=useState({latitude: 37.78825,longitude: -122.4324, latitudeDelta: 0.01, longitudeDelta: 0.01})
  const [dataArray,setDataArray]=useState(null)
  const type=""
  const radius=400
  useEffect(async()=>{
    //runs everytime the position changes
    try{
      const newDataArray=await MapMethods.getMarkers(position.lat,position.long,type,radius)
      setDataArray(newDataArray)
    }catch(err){
      Alert.alert(err.title,err.message)
    }
  },[position])

  //Sets the self marker, if this needs to be changed, can be changed to a variable and set State accordingly
  const selfMarker=<Marker coordinate={{latitude:position.lat,longitude:position.long}}/>

  const markerArray=dataArray.map((marker, index) => (
    <Marker
        key={index}
        coordinate={{latitude: marker["geometry"]["location"]["lat"],longitude: marker["geometry"]["location"]["lng"]}}
        title={marker["name"]}>
      <View style={styles.circle} />
    </Marker>
  ));

  //function to retrieve coordinates initially
  const getCoordinates = () => {
    navigator.geolocation.getCurrentPosition(
      position => {
        var pos = { lat:position["coords"]["latitude"],
                    long:position["coords"]["longitude"],
                    alt:position["coords"]["longitude"]};
        setPosition(pos)
      },
      error => Alert.alert(error.message),
      { enableHighAccuracy: false, timeout: 20000, maximumAge: 1000 }
    );
  };

  //Runs only on start up
  useEffect(()=>{
    getCoordinates()
  },[])


  //Returns the Map if coordinates can be found. If not returns an error text
  const TheMap=()=>{
    if(position.lat!=null && position.long!=null){
      return (
        <MapView
          initialRegion={initialRegion}
          provider={PROVIDER_GOOGLE}
          customMapStyle={mapstyle}
          style={styles.mapStyle}>
          {selfMarker}
          {markerArray}
        </MapView>);
    }else{
      return (<Text>MAP HAS NOT YET FOUND YOUR LOCATION</Text>);
    }
  }

  return (
    <View style={styles.container}>
      <Text>Latitude {state.pos.lat} </Text>
      <Text>Longitude {state.pos.long} </Text>
      <Text>Altitude {state.pos.alt} </Text>
      <TheMap/>
      <Button
        onPress={getCoordinates}
        title="Refresh Coordinates"
      />
    </View>
  );
  }


const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  mapStyle: {
    width: Dimensions.get('window').width,
    height: Dimensions.get('window').height-100,
  },
});
export default MapScreen;
