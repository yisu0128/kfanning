import { createRouter, createWebHistory } from 'vue-router';
import MovieSiteList from '../components/MovieSiteList.vue';
import AddMovieSite from '../components/AddMovieSite.vue'; // 추가
import MoviesiteDetails from '../components/MoviesiteDetail.vue';
import EditMovieSite from '../components/EditMovieSite.vue';

const routes = [
  {
    path: '/',
    name: 'MovieSiteList',
    component: MovieSiteList,
  },
  {
    path: '/add-moviesite', // 추가
    name: 'AddMovieSite',
    component: AddMovieSite, // 추가
  },
  {
    path: '/get-moviesite/:site_id', // 추가
    name: 'MoviesiteDetails',
    component: MoviesiteDetails, // 추가
  },
  {
    path: '/edit-moviesite/:site_id', // 추가
    name: 'EditMovieSite',
    component: EditMovieSite, // 추가
  },
  // Add more routes here if needed
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
