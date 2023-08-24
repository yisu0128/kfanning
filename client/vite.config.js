import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  define: {
    'process.env': {
      VITE_GOOGLE_MAPS_API_KEY: JSON.stringify('YOUR_GOOGLE_MAPS_API_KEY_HERE'),
    },
  },
  resolve: {
    alias: {
      '@': '/src', // 수정 필요할 수 있습니다. 프로젝트 구조에 따라 경로 조정하세요.
    },
  },
});
