#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the URL from the first argument (passed by the user)
const url = process.argv[2];

// Make a GET request to the provided URL
request(url, (error, response, body) => {
  if (error) {
    // If there's an error, print it
    console.log(error);
  } else {
    // Otherwise, print the status code of the response
    console.log('code:', response.statusCode);
  }
});
