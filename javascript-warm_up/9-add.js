#!/usr/bin/node
// Function to add two numbers
function add (a, b) {
  return a + b;
}

// Get the command-line arguments (the 3rd and 4th items)
const firstArg = parseInt(process.argv[2]);
const secondArg = parseInt(process.argv[3]);

// Call the add function and print the result
console.log(add(firstArg, secondArg));
