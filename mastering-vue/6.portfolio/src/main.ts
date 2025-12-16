import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import AOS from 'aos'
import 'aos/dist/aos.css'

const app = createApp(App)

app.use(router)

app.mount('#app')

AOS.init({
  once: true,        // animate only once
  duration: 3000,    // default duration
  easing: 'ease-out-cubic'
})
