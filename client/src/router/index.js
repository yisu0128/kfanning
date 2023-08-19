import { createRouter, createWebHistory } from 'vue-router'
import MovieSites from '../components/MovieSites.vue'
import Home from '../components/Home.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/moviesites',
      name: 'MovieSites',
      component: MovieSites,
    },
    {
      path : '/',
      name: 'Home',
      component: Home,
    }

  ]
})

export default router