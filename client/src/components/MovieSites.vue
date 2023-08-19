<template>
  <div class="moviesites">
    <div class="jumbotron text-center">
      <h1 class="display-4">FANNINGK</h1>
    </div>
    <div class="container">
      <div class="row">
        <div class="col-md-6">
          <table class="table table-striped">
            <thead>
              <tr>
                <th>Name</th>
                <th>Location</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(place, index) in places" :key="index">
                <td>{{ place.name }}</td>
                <td>{{ place.location }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="row mt-4">
        <div class="col-md-6">
          <div class="input-group">
            <input v-model="newPlace.name" class="form-control" placeholder="Name">
            <input v-model="newPlace.location" class="form-control" placeholder="Location">
            <div class="input-group-append">
              <button @click="addPlace" class="btn btn-success">Add Place</button>
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
      places: [],
      newPlace: { name: '', location: '' }
    };
  },
  methods: {
    addPlace() {
      this.places.push({ name: this.newPlace.name, location: this.newPlace.location });
      this.newPlace.name = '';
      this.newPlace.location = '';
    }
  }
};
</script>

<style scoped>
.moviesites {
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

.table {
  color: black;
}

.input-group {
  margin-top: 20px;
}
</style>
