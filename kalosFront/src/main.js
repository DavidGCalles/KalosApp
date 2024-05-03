import './assets/main.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import PrimeVue from 'primevue/config';
import 'primeicons/primeicons.css';
import 'primeflex/primeflex.css'; // if using PrimeFlex for layout
import "primevue/resources/themes/aura-light-teal/theme.css"
import 'primevue/resources/primevue.min.css'; // PrimeVue core styles

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(PrimeVue)

app.mount('#app')
