#!/usr/bin/node

const request = require('request'); // Import the request module
const apiUrl = process.argv[2]; // Get the API URL from the first argument

// Make an API request
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error); // Print the error if any occurs
  } else {
    // Parse the API response (JSON format)
    const films = JSON.parse(body).results;
    let count = 0;

    // Loop through each film
    for (const film of films) {
      // Check if any character URL contains '18' (Wedge Antilles' ID)
      for (const characterUrl of film.characters) {
        if (characterUrl.includes('/18/')) {
          count++;
          break; // Stop once Wedge Antilles is found in this movie
        }
      }
    }

    // Print the count of films where Wedge Antilles appears
    console.log(count);
  }
});
