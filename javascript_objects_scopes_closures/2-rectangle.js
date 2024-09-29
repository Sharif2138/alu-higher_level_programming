#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    // Check if w and h are positive integers greater than 0
    if (w > 0 && h > 0) {
      this.width = w;  // Initialize width
      this.height = h; // Initialize height
    }
    // If w or h is 0 or not a positive integer, nothing is assigned
  }
}

module.exports = Rectangle;
