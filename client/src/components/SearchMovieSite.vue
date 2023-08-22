<template>
    <div>
      <input v-model="searchQuery" placeholder="Enter site name" />
      <button @click="searchSites">Search</button>
  
      <ReadMovieSite :sites="searchedSites" @edit="showEditForm" @delete="deleteSite" />
    </div>
  </template>
  
  <script>
  import ReadMovieSite from './ReadMovieSite.vue';
  import EditMovieSite from './EditMovieSite.vue';
  
  export default {
    components: {
      ReadMovieSite,
      EditMovieSite,
    },
    data() {
      return {
        searchQuery: '',
        searchedSites: [],
        showEdit: false,
        siteToEdit: null,
      };
    },
    methods: {
      searchSites() {
        // Perform API request to search movie sites based on searchQuery
        // Update searchedSites with the result
      },
      showEditForm(site) {
        this.siteToEdit = site;
        this.showEdit = true;
      },
      deleteSite(site) {
        // Perform API request to delete the selected site
        // Update searchedSites after deletion
      },
      refreshList() {
        // Called after create or update to refresh the list
        this.searchSites();
      },
    },
  };
  </script>
  