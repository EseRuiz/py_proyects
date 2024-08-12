import type { GIFresponse } from "../interfaces/gif.response";

const apiKey = 'xoHILmQCZB0ECJdh1wzU8fMG1XYI8L9b';

fetch(`https://api.giphy.com/v1/gifs/random?api_key=${ apiKey}`)
    .then(res => res.json())
    .then((body: GIFresponse) => {
        console.log(body.data.images.downsized_medium.url);
    })
    .catch(err => console.info(err))