import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css'; // 부트스트랩 스타일 추가
import 'bootstrap/dist/js/bootstrap.js'; // 부트스트랩 스크립트 추가
import * as VueGoogleMaps from "vue2-google-maps" // Import package

Vue.config.productionTip = false

Vue.use(VueGoogleMaps, {
  load: {
    key: "AIzaSyBVjq1GKBNCEJxz2-SSSi5E_JHICuPl8dA",
    libraries: "places",
    region: "KR" // 반드시 추가하셔야됩니다.(추가 안하시면 동해가 일본해로 나타납니다.)
  }
});

new Vue({
  render: h => h(App),
}).$mount('#app')

const app = createApp(App)

app.use(router)

app.mount('#app')