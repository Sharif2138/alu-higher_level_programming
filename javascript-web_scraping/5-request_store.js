#!/usr/bin/node

const request = require('request'); // Import the request module to make HTTP requests
const fs = require('fs'); // Import the fs (file system) module to interact with files

// Get the URL and file path from the command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make an HTTP request to the given URL
request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error); // Print the error if the request fails
  } else {
    // Write the body (response) to the specified file with UTF-8 encoding
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error('Error writing to file:', err); // Print an error if file writing fails
      } else {
        console.log('File saved successfully!');
      }
    });
  }
});
