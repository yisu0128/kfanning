<template>
  <div>
    <h1>Movie Site Details</h1>

    <div v-if="moviesite">
      <h2>{{ moviesite.SITE_NAME }}</h2>
      <p><strong>Location:</strong> {{ moviesite.PROVINCE }}, {{ moviesite.CITY }}, {{ moviesite.STREET }}</p>
      <p><strong>Coordinates:</strong> {{ moviesite.LATITUDE }}, {{ moviesite.LONGTITUDE }}</p>
    </div>

    <div id="map-container" ref="mapContainer" style="height: 600px;"></div>

    <button @click="editMovieSite">Edit</button>
    <button @click="deleteMovieSite">Delete</button>

    <div id="map"></div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'MoviesiteDetails',
  data() {
    return {
      moviesite: null,
      map: null, // Kakao Maps 인스턴스
    };
  },
  async created() {
    await this.loadMovieSite();
  },
  methods: {
    async loadMovieSite() {
      try {
        const response = await axios.get(`http://localhost:5000/get_moviesite/${this.$route.params.site_id}`);
        this.moviesite = response.data[0];
        this.initializeMap(); // 영화 사이트 정보를 가져온 후 지도 초기화
      } catch (error) {
        console.error('영화 사이트 불러오기 오류:', error);
      }
    },
    editMovieSite() {
      this.$router.push({ name: 'EditMovieSite', params: { site_id: this.$route.params.site_id } });
    },
    async deleteMovieSite() {
      try {
        const response = await axios.delete(`http://localhost:5000/delete_moviesite/${this.$route.params.site_id}`);
        console.log(response.data); // 성공 메시지 표시 또는 필요한대로 처리
        // 다른 경로로 리디렉션하거나 컴포넌트 상태 업데이트
      } catch (error) {
        console.error('영화 사이트 삭제 오류:', error);
      }
    },
    initializeMap() {
      if (window.kakao && window.kakao.maps) {
        this.loadMap();
      } else {
        this.loadScript();
      }
    },
    loadScript() {
      const script = document.createElement("script");
      script.src =
        "https://dapi.kakao.com/v2/maps/sdk.js?appkey=7a324c54e7ae9f797ffabfc7f114d83f&libraries=services&autoload=false";
      script.onload = () => window.kakao.maps.load(this.loadMap);

      document.head.appendChild(script);
    },
    loadMap() {
      const container = document.getElementById("map");
      const options = {
        center: new window.kakao.maps.LatLng(this.moviesite.LATITUDE, this.moviesite.LONGTITUDE),
        level: 3,
      };

      this.map = new window.kakao.maps.Map(container, options);
      this.loadMaker();
    },
    loadMaker() {
      const markerPosition = new window.kakao.maps.LatLng(
        this.moviesite.LATITUDE,
        this.moviesite.LONGTITUDE
      );

      const marker = new window.kakao.maps.Marker({
        position: markerPosition,
      });

      marker.setMap(this.map);
    },
  },
};
</script>

<style scoped>
#map {
  width: 50%;
  height: 400px;
}
</style>
