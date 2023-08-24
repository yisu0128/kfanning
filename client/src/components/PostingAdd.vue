<template>
    <div class="container mt-5">
      <h1 class="mb-4">Add New Posting</h1>
  
      <form @submit.prevent="addPosting" class="card">
        <div class="card-body">
          <div class="form-group">
            <label for="title">Title</label>
            <input type="text" v-model="newPosting.title" class="form-control" required>
          </div>
          <div class="form-group">
            <label for="author">Author</label>
            <input type="text" v-model="newPosting.author" class="form-control" required>
          </div>
          <div class="form-group">
            <label for="content">Content</label>
            <textarea v-model="newPosting.content" class="form-control" rows="5" required></textarea>
          </div>
          <button type="submit" class="btn btn-primary">Add Posting</button>
        </div>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'PostingAdd',
    data() {
      return {
        newPosting: {
          title: '',
          author: '',
          content: '',
        },
      };
    },
    methods: {
      async addPosting() {
        try {
          const response = await axios.post('http://localhost:5000/create_posting', this.newPosting);
          console.log(response.data); // Display success message or handle as needed
          this.$router.push('/postings'); // Redirect to the postings list
        } catch (error) {
          console.error('Error adding posting:', error);
        }
      },
    },
  };
  </script>
  