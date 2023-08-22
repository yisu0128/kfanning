<template>
  <div>
    <h1>Movie Sites</h1>
    <ul>
      <li v-for="movieSite in movieSites" :key="movieSite.site_id">
        {{ movieSite.site_name }} - {{ movieSite.province }}, {{ movieSite.city }}
      </li>
    </ul>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';

export default {
  name: 'ReadMovieSite',
  data() {
    return {
      movieSites: [], // 데이터를 저장할 배열
    };
  },
  mounted() {
    // 컴포넌트가 마운트된 후 데이터를 불러옴
    this.fetchMovieSites();
  },
  methods: {
    async fetchMovieSites() {
      try {
        const response = await fetch('/api/moviesites'); // 서버 API 엔드포인트로 변경
        const data = await response.json();
        this.movieSites = data.moviesites;
      } catch (error) {
        console.error('Error fetching movie sites:', error);
      }
    },
  },
};
</script>
