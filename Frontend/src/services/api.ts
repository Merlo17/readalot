import axios from 'axios';

// const baseURL = 'https://api.example.com';
const baseURL = 'http://94.237.114.105:80/';
const swipeEndpoint = 'swipe';
const browseEndpoint = 'start';

const api = axios.create({
    baseURL,
});

export { api, swipeEndpoint, browseEndpoint };
