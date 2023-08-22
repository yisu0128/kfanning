<template>
    <div>
      <h2>Create Movie Site</h2>
      <form @submit.prevent="createMovieSite">
        <label>Site Name:</label>
        <input v-model="siteName" required /><br />
        <label>Province:</label>
        <input v-model="province" required /><br />
        <label>City:</label>
        <input v-model="city" required /><br />
        <label>Street:</label>
        <input v-model="street" required /><br />
        <label>Longitude:</label>
        <input v-model="longitude" required /><br />
        <label>Latitude:</label>
        <input v-model="latitude" required /><br />
        <button type="submit">Create</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        siteName: "",
        province: "",
        city: "",
        street: "",
        longitude: "",
        latitude: "",
      };
    },
    methods: {
      createMovieSite() {
        const newMovieSite = {
          site_name: this.siteName,
          province: this.province,
          city: this.city,
          street: this.street,
          longitude: this.longitude,
          latitude: this.latitude,
        };
  
        // Send an API request to create a new movie site using the newMovieSite object
        // You can use a library like Axios or Vue Resource for making HTTP requests
        // Example: this.$http.post('/create_moviesite', newMovieSite)
        // After successful creation, you can redirect or update the UI accordingly
      },
    },
  };
  </script>
  