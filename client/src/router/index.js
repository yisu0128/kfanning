import { createRouter, createWebHistory } from 'vue-router';
import MovieSiteList from '../components/MovieSiteList.vue';
import AddMovieSite from '../components/AddMovieSite.vue'; // 추가
import MoviesiteDetails from '../components/MoviesiteDetails.vue';
import EditMovieSite from '../components/EditMovieSite.vue';
import PostingDetails from '../components/PostingDetails.vue';
import PostingAdd from '../components/PostingAdd.vue'; 


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
  {
    path: '/posting/:posting_id',
    name: 'PostingDetails',
    component: PostingDetails,
  },
   {
    path: '/postings/add', // 추가
    name: 'PostingAdd',
    component: PostingAdd,
  },
  // Add more routes here if needed
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});


export default router;
