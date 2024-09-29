#!/usr/bin/node

const Rectangle = require('./4-rectangle');

// Define the Square class that extends Rectangle
class Square extends Rectangle {
  constructor (size) {
    // Call the Rectangle constructor with size for both width and height
    super(size, size);
  }
}

module.exports = Square;
