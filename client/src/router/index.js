import { createRouter, createWebHistory } from 'vue-router';
import MovieSiteList from '../components/MovieSiteList.vue';

const routes = [
  {
    path: '/',
    name: 'MovieSiteList',
    component: MovieSiteList,
  },
  // Add more routes here if needed
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
