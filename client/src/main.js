import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.js';
import SearchMovieSite from './components/SearchMovieSite.vue'; // 추가
import CreateMovieSite from './components/CreateMovieSite.vue'; // 추가
import EditMovieSite from './components/EditMovieSite.vue'; 
import DeleteMovieSite from './components/DeleteMovieSite.vue'; // 추가
import ReadMovieSite from './components/ReadMovieSite.vue'; 

const app = createApp(App);

app.use(router);

app.component('search-movie-site', SearchMovieSite); // 추가
app.component('create-movie-site', CreateMovieSite); // 추가
app.component('edit-movie-site', EditMovieSite); // 추가
app.component('delete-movie-site', DeleteMovieSite);
app.component('read-movie-site', ReadMovieSite);

app.mount('#app');