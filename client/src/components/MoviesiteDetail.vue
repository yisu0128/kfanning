<template>
    <div>
      <h1>Movie Site Details</h1>
      
      <div v-if="moviesite">
        <h2>{{ moviesite.SITE_NAME }}</h2>
        <p><strong>Location:</strong> {{ moviesite.PROVINCE }}, {{ moviesite.CITY }}, {{ moviesite.STREET}}</p>
        <p><strong>Coordinates:</strong> {{ moviesite.LATITUDE }}, {{ moviesite.LONGTITUDE }}</p>
      </div>
      
      <button @click="editMovieSite">Edit</button>
      <button @click="deleteMovieSite">Delete</button>
    </div>
    
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'MoviesiteDetails',
    data() {
      return {
        moviesite: null,
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
        } catch (error) {
          console.error('Error loading movie site:', error);
        }
      },
      editMovieSite() {
        this.$router.push({ name: 'EditMovieSite', params: { site_id: this.$route.params.site_id } });
      },
      async deleteMovieSite() {
        try {
          const response = await axios.delete(`http://localhost:5000/delete_moviesite/${this.$route.params.site_id}`);
          console.log(response.data); // Display success message or handle as needed
          // Redirect to a different route or update component state
        } catch (error) {
          console.error('Error deleting movie site:', error);
        }
      },
    },
  };
  </script>
  