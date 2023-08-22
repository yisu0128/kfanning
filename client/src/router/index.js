import { createRouter, createWebHistory } from 'vue-router'
import SearchMovieSite from '../components/SearchMovieSite.vue';
import CreateMovieSite from '../components/CreateMovieSite.vue';
import EditMovieSite from '../components/EditMovieSite.vue';
import DeleteMovieSite from '../components/DeleteMovieSite.vue';
import ReadMovieSite from '../components/ReadMovieSite.vue'
import Home from '../components/Home.vue'

const routes = [
  {
    path: '/moviesites',
    component: ReadMovieSite,
    children: [
      { path: '', component: SearchMovieSite },
      { path: 'create', component: CreateMovieSite },
      { path: 'edit/:id', component: EditMovieSite },
      { path: 'delete/:id', component: DeleteMovieSite },
    ],
  },
  {
    path: '/',
    name: 'Home',
    component: Home,
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router