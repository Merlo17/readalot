import axios from 'axios';
import {api, browseEndpoint, swipeEndpoint} from './api';

const ApiService = {
  browse(query) {
    return api.post(browseEndpoint, query);
  },

  swipe(swipeData) {
    console.log("swiped")
    return api.post(swipeEndpoint, swipeData);
  },
};

export default ApiService;
