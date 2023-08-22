<template>
  <div>
    <h1>Movie Sites</h1>
    
    <table>
      <thead>
        <tr>
          <th>Site Name</th>
          <th>Location</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="movieSite in movieSites" :key="movieSite.SITE_ID">
          <td>{{ movieSite.SITE_NAME }}</td>
          <td>{{ movieSite.PROVINCE }}, {{ movieSite.CITY }}, {{ movieSite.STREET }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'MovieSiteList',
  data() {
    return {
      movieSites: [],
    };
  },
  methods: {
    async fetchMovieSites() {
      try {
        const response = await axios.get('http://localhost:5000/get_all_moviesites');
        this.movieSites = response.data;
      } catch (error) {
        console.error('Error fetching movie sites:', error);
      }
    },
  },
  mounted() {
    this.fetchMovieSites();
  },
};
</script>

