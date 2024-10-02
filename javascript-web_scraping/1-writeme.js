#!/usr/bin/node

// Import the 'fs' module, so we can work with files
const fs = require('fs');

// Get the file path and the string to write from the arguments provided by the user
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write the string into the file
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    // If something goes wrong, print the error
    console.log(err);
  }
});
