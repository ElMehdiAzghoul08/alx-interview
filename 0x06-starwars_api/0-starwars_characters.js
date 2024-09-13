#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as an argument');
  process.exit(1);
}

const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function requestGet (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

requestGet(filmUrl)
  .then(film => {
    return film.characters.reduce((promise, url) => {
      return promise.then(() => requestGet(url))
        .then(character => console.log(character.name))
        .catch(error => console.error(`Failed to fetch character: ${error.message}`));
    }, Promise.resolve());
  })
  .catch(error => {
    console.error('Error:', error.message);
  });
