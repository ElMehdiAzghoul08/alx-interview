#!/usr/bin/node

const https = require('https');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as an argument');
  process.exit(1);
}

const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function httpsGet (url) {
  return new Promise((resolve, reject) => {
    https.get(url, (response) => {
      let data = '';
      response.on('data', (chunk) => {
        data += chunk;
      });
      response.on('end', () => {
        resolve(JSON.parse(data));
      });
    }).on('error', (error) => {
      reject(error);
    });
  });
}

httpsGet(filmUrl)
  .then(film => {
    return film.characters.reduce((promise, url) => {
      return promise.then(() => httpsGet(url))
        .then(character => console.log(character.name))
        .catch(error => console.error(`Failed to fetch character: ${error.message}`));
    }, Promise.resolve());
  })
  .catch(error => {
    console.error('Error:', error.message);
  });
