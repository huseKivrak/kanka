//vite.config.js
import { defineConfig } from 'vite'
import djangoVite from 'django-vite-plugin'

export default defineConfig({
    plugins: [
        djangoVite([
            'home/js/app.js',
            'home/css/style.css',
        ])
    ],
});