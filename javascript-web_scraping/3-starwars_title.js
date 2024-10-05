#!/usr/bin/node

// Import the request module
const request = require('request');

// Get the movie ID from the first argument
const movieId = process.argv[2];

// URL for the Star Wars API, with the movie ID in the path
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Parse the response body to JSON
    const movieData = JSON.parse(body);

    // Print the title of the movie
    console.log(movieData.title);
  }
});
