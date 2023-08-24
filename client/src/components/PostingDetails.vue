<template>
    <div class="container mt-5">
      <h1 class="mb-4">Posting Details</h1>
  
      <div v-if="posting" class="card">
        <div class="card-body">
          <h2 class="card-title">{{ posting.title }}</h2>
          <p class="card-text"><strong>Author:</strong> {{ posting.author }}</p>
          <p class="card-text"><strong>Content:</strong> {{ posting.content }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'PostingDetails',
    data() {
      return {
        posting: null,
      };
    },
    async created() {
      const postingId = this.$route.params.posting_id;
      await this.loadPosting(postingId);
    },
    methods: {
      async loadPosting(postingId) {
        try {
          const response = await axios.get(`http://localhost:5000/get_posting/${postingId}`);
          this.posting = response.data[0];
        } catch (error) {
          console.error('Error loading posting:', error);
        }
      },
    },
  };
  </script>
  