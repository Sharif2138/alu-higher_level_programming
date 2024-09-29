#!/usr/bin/node

// Step 1: Define the class 'Rectangle'
class Rectangle {
    // Step 2: Create a constructor method
    constructor(w, h) {
        // Step 3: Initialize the 'width' and 'height' attributes with the values of 'w' and 'h'
        this.width = w;   // 'this.width' refers to the object's width
        this.height = h;  // 'this.height' refers to the object's height
    }
}

// Step 4: Export the class so it can be used in other files
module.exports = Rectangle;
