import { createRouter, createWebHistory } from 'vue-router';
import MovieSiteList from '../components/MovieSiteList.vue';
import AddMovieSite from '../components/AddMovieSite.vue'; // 추가

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
  // Add more routes here if needed
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
