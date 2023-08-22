<template>
    <div>
      <h2>Delete Movie Site</h2>
      <form @submit.prevent="deleteMovieSite">
        <label>Site ID:</label>
        <input v-model="siteId" required /><br />
        <button type="submit">Delete</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        siteId: "",
      };
    },
    methods: {
      deleteMovieSite() {
        const siteIdToDelete = this.siteId;
  
        // Send an API request to delete the movie site with the given siteId
        // You can use a library like Axios or Vue Resource for making HTTP requests
        // Example: this.$http.delete(`/delete_moviesite?site_id=${siteIdToDelete}`)
        // After successful deletion, you can redirect or update the UI accordingly
      },
    },
  };
  </script>
  
  