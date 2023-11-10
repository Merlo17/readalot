import './assets/main.css';

import { createApp } from 'vue';
import { createPinia } from 'pinia';

import Vue from 'vue';
import App from './App.vue';
import router from './router';

Vue.config.productionTip = false;

const app = createApp(App);

app.use(createPinia());
app.use(router);

app.mount('#app');
