<template>
  <div>
    <h1>Movie Sites</h1>
    
    <input v-model="searchQuery" placeholder="Search for a movie site" />
    <button @click="searchMovieSites">Search</button>
    
    <table>
      <thead>
        <tr>
          <th>Site Name</th>
          <th>Location</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="movieSite in filteredMovieSites" :key="movieSite.SITE_ID">
          <td>{{ movieSite.SITE_NAME }}</td>
          <td>{{ movieSite.PROVINCE }}, {{ movieSite.CITY }}</td>
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
      searchQuery: '',
      movieSites: [],
    };
  },
  computed: {
    filteredMovieSites() {
      if (this.searchQuery.trim() === '') {
        return this.movieSites;
      } else {
        return this.movieSites.filter(movieSite =>
          movieSite.SITE_NAME.toLowerCase().includes(this.searchQuery.toLowerCase())
        );
      }
    },
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
    searchMovieSites() {
      // No need to fetch data again; computed property handles the filtering
    },
  },
  mounted() {
    this.fetchMovieSites();
  },
};
</script>
