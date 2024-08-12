import axios from 'axios';
import { GIFresponse } from '../interfaces/gif.response';

const apiKey = "xoHILmQCZB0ECJdh1wzU8fMG1XYI8L9b";

export const giphyApi = axios.create({
    baseURL:  'https://api.giphy.com/v1/gifs',
    params: {
        api_key: apiKey,
    }
});

giphyApi.get<GIFresponse>('/random')
    .then(resp => console.log(resp.data.data.images.downsized_large.url))
    .catch(err => console.log(err))