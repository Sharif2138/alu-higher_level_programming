#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Method to print the rectangle using 'X'
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // Method to swap width and height
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // Method to double the width and height
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
