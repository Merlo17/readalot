import './assets/main.css';

import { createApp } from 'vue';
import { createPinia } from 'pinia';

import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

import { faHeart, faCircleXmark } from '@fortawesome/free-solid-svg-icons';
import { faHeart as faHeartReg, faCircleXmark as faCircleXmarkReg } from '@fortawesome/free-regular-svg-icons';

import App from './App.vue';
import router from './router';

library.add(faHeart, faCircleXmark, faHeartReg, faCircleXmarkReg);

const app = createApp(App);

app.use(createPinia());
app.use(router);

app.mount('#app');
