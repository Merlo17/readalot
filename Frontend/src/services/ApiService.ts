import axios from 'axios';
import { api, browseEndpoint, swipeEndpoint } from './api';

const ApiService = {
  browse(query : any) {
    return api.post(browseEndpoint, query);
  },

  swipe(swipeData : any) {
    return api.post(swipeEndpoint, swipeData);
  },
};

export default ApiService;
