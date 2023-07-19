import { defineConfig } from 'vite'
import {splitVendorChunkPlugin} from 'vite'
import react from '@vitejs/plugin-react'



export default defineConfig({
  build: { manifest: true },
  base: process.env.NODE_ENV === "production" ? "/static/" : "/",
  root: './src/',
  plugins: [
    react(),
    splitVendorChunkPlugin(),
  ]
});