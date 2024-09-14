#!/usr/bin/node
const request = require('request');
const baseUrl = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request(`${baseUrl}/films/${process.argv[2]}/`, (error, response, filmData) => {
    if (error) {
      console.log(error);
    }
    const characterUrls = JSON.parse(filmData).characters;
    const characterPromises = characterUrls.map(
      url => new Promise((resolve, reject) => {
        request(url, (charError, charResponse, charData) => {
          if (charError) {
            reject(charError);
          }
          resolve(JSON.parse(charData).name);
        });
      }));

    Promise.all(characterPromises)
      .then(characterNames => console.log(characterNames.join('\n')))
      .catch(allErrors => console.log(allErrors));
  });
}
