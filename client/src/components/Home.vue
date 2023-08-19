<template>
  <div class="home">
    <div class="jumbotron text-center" style="background-color: #0B3B2E;">
      <h1 class="display-4">FANNINGK</h1>
    </div>
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-md-6">
          <div class="input-group mb-3">
            <input class="form-control" type="text" placeholder="Search" v-model="searchQuery">
            <div class="input-group-append">
              <button class="btn btn-primary" @click="search">Search</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: 'FANNINGK',
      searchQuery: ''
    };
  },
  methods: {
    search() {
      console.log('Search button clicked! Search query:', this.searchQuery);
    }
  }
};
</script>

<style scoped>
.home {
  background-color: #0B3B2E;
  color: white;
  font-family: Georgia, serif;
  height: 100vh;
}

.jumbotron {
  background-color: transparent;
  padding: 100px 0;
  margin-bottom: 0;
}

.container {
  margin-top: 50px;
}
</style>
