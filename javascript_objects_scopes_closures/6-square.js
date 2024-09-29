#!/usr/bin/node

// Import the Square class from 5-square.js
const Square5 = require('./5-square');

// Define the new Square class
class Square extends Square5 {
  // Define the charPrint method
  charPrint(c) {
    // If 'c' is undefined, use 'X'
    const char = c === undefined ? 'X' : c;

    // Print the square row by row using the given character
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
