<template>
  <div style="width: 300px; height: 300px" id="map"></div>
</template>
<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBVjq1GKBNCEJxz2-SSSi5E_JHICuPl8dA"></script>
<script>
export default {
  mounted() {
    this.initMap();
    this.setMarker(this.mapCenter, "ce");
    this.setMarker(this.bands, "1");
    this.setMarker(this.bands2, "2");
  },
  methods: {
    initMap() {
      this.map = new google.maps.Map(document.getElementById("map"), {
        //getElementById로 map id 속성의 요소를 가져온다.
        center: this.mapCenter, //center로 할 위도, 경도를 지정한다.
        zoom: 17, //zoom size를 지정.
        maxZoom: 20,
        minZoom: 3,
        streetViewControl: true,
        mapTypeControl: true,
        fuulscreenControl: true,
        zoomControl: true,
      });
    },
    setMarker(Points, Label) {
      //지도에 마커를 찍는 함수.
      const markers = new google.maps.Marker({
        position: Points,
        map: this.map,
        label: {
          text: Label,
          color: "#FFF",
        },
      });
    },
  },
  data() {
    return {
      map: null,
      mapCenter: { lat: 35.105696, lng: 129.042857 },
      bands: {
        lat: 35.106187,
        lng: 129.042943,
      },
      bands2: {
        lat: 35.105556,
        lng: 129.04393,
      },
    };
  },
};
</script>
