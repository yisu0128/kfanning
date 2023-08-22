<template>
    <div>
      <h1>Add Movie Site</h1>
      
      <form @submit.prevent="addMovieSite">
        <label for="siteName">Site Name:</label>
        <input v-model="siteName" id="siteName" required />
        <br />
        
        <label for="province">Province:</label>
        <input v-model="province" id="province" required />
        <br />
        
        <label for="city">City:</label>
        <input v-model="city" id="city" required />
        <br />
        
        <label for="street">Street:</label>
        <input v-model="street" id="street" required />
        <br />
        
        <label for="longtitude">Longtitude:</label>
        <input v-model="longtitude" type="number" step="0.000001" id="longtitude" required />
        <br />
        
        <label for="latitude">Latitude:</label>
        <input v-model="latitude" type="number" step="0.000001" id="latitude" required />
        <br />
        
        <button type="submit">Add Movie Site</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'AddMovieSite',
    data() {
      return {
        siteName: '',
        province: '',
        city: '',
        street: '',
        longtitude: null,
        latitude: null,
      };
    },
    methods: {
      async addMovieSite() {
        try {
          const response = await axios.post('http://localhost:5000/add_moviesite', {
            site_name: this.siteName,
            province: this.province,
            city: this.city,
            street: this.street,
            longtitude: this.longtitude,
            latitude: this.latitude,
          });
          console.log(response.data); // Display success message or handle as needed
        } catch (error) {
          console.error('Error adding movie site:', error);
        }
      },
    },
  };
  </script>
  