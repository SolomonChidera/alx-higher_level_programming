#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }

  const characters = JSON.parse(body).characters;
  characters.forEach((movie) => {
    request(movie, (err, res, body) => {
      if (err) {
        console.log(err);
      }
      console.log(JSON.parse(body).name);
    });
  });
});
