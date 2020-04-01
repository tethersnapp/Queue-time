const MapMethods={
    getMarkers:async(lat,long,type,radius)=>{
        let APIKEY  = "AIzaSyBXYaJf79P51MqE6JXZjfZohBUnpuV1RyU";
        let url = `https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=${lat},${long}&radius=${radius}&type=${type}&key=${APIKEY}`;
        console.log("TRYING: "+url)
        console.log("Requesting");
        try{
            const response =await fetch(url)
            const resjson=await response.json()
            if(resjson.status==='OK'){
              console.log(resjson)
              const dataArray= resjson.results
              return(dataArray)
            }else{
                throw new Error('Couldn\'t retrieve data')
            }
            }catch(err){
                throw err
        }
    },
}
