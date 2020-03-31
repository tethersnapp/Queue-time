import React,{useState} from 'react';
import MapView,{PROVIDER_GOOGLE,Marker}  from 'react-native-maps';
import {Platform,StyleSheet,Text,View,Alert,TouchableOpacity,Dimensions} from "react-native";

const mapstyle = require('./mapstyle.json');


export default class App extends React.Component {
  _isMounted = false;
  selfMarker = null;
  state = {
    pos: {lat:null,long:null,alt:null},
    initialRegion: {latitude: 37.78825,longitude: -122.4324, latitudeDelta: 0.01, longitudeDelta: 0.01},
    nearby: []
  };

  constructor(props){
    super(props);
  }

  componentDidMount(){
    this._isMounted = true;
    console.log("*MOUNTED");
    this.findCoordinates();
  }

  componentWillUnmount(){
    this._isMounted = false;
    console.log("*UN-MOUNT");
  }

  getMarkers(){
    let APIKEY  = PLACE API KEY HERE;
    let radius  = 500;
    let lat   = this.state.pos.lat;
    let long  = this.state.pos.long;
    let type  = "restaurant";

    let url = `https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=${lat},${long}&radius=${radius}&type=${type}&key=${APIKEY}`;
    console.log("TRYING: "+url)
    console.log("Requesting");
    fetch(url)
        .then((response) => {console.log("jsonifying"); return response.json();})
        .then((resjson) => {console.log(JSON.stringify(resjson)); return resjson["results"];})
        .then((dataArray) => {
          var res = dataArray.map((marker, index) => (
              <Marker
                key = {index}
                coordinate = {{latitude: marker["geometry"]["location"]["lat"],longitude: marker["geometry"]["location"]["lng"]}}
                title = { marker["name"] }>
                <View style={{width: 8, height: 8, borderRadius: 8, backgroundColor: "rgba(0,255,0, 0.9)"}} />
              </Marker>
            ));
          console.log("going through");
          for(var j=0;j<dataArray.length;j++){
            console.log(dataArray[j]["name"]);
            console.log(res[j]);
          }
          console.log("FOUND")
          console.log(res)
          this._isMounted && this.setState({nearby:res});
          console.log("updating canvas");})
          console.log("done");
  }

  findCoordinates = () => {
    navigator.geolocation.getCurrentPosition(
      position => {
        var pos = { lat:position["coords"]["latitude"],
                    long:position["coords"]["longitude"],
                    alt:position["coords"]["longitude"]};
        var initialRegion = this.state.initialRegion;
        initialRegion.latitude = pos.lat
        initialRegion.longitude = pos.long
        this._isMounted && this.setState({pos:pos,initialRegion:initialRegion});
        this.selfMarker = <Marker coordinate={{latitude:pos.lat,longitude:pos.long}}/>;
        const res = this.getMarkers();
      },
      error => Alert.alert(error.message),
      { enableHighAccuracy: false, timeout: 20000, maximumAge: 1000 }
    );
  };

  getMap(props){
    if(this.state.pos.lat!=null && this.state.pos.long!=null){
      return (
        <MapView
          initialRegion={this.state.initialRegion}
          provider={PROVIDER_GOOGLE}
          customMapStyle={mapstyle}
          style={styles.mapStyle}>
          {this.selfMarker}
          {this.state.nearby}
        </MapView>);
    }else{
      return (<Text>MAP HAS NOT YET FOUND YOUR LOCATION</Text>);
    }


  }


  render() {
    return (
      <View style={styles.container}>
        <Text>Latitude {this.state.pos.lat} </Text>
        <Text>Longitude {this.state.pos.long} </Text>
        <Text>Altitude {this.state.pos.alt} </Text>
        {this.getMap()}
      </View>
    );
  }
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
