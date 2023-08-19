<template>
    <div>
      <gmap-map
          :zoom="14"    
          :center="center"
          style="width:100%;  height: 600px;"
        >
      </gmap-map>
    </div>
  </template>
   
  <script>
  export default {
    name: "AddGoogleMap",
    data() {
      return {
        center: { lat: 37.5642135, lng: 127.0016985 },
        locationMarkers: [],
        locPlaces: [],
        existingPlace: null
      };
    }, 
  };
  </script>