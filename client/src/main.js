import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css'; // 부트스트랩 스타일 추가
import 'bootstrap/dist/js/bootstrap.js'; // 부트스트랩 스크립트 추가


const app = createApp(App)

app.use(router)

app.mount('#app')