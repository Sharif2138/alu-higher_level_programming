#!/usr/bin/node
const size = parseInt(process.argv[2]); // Get the first argument and convert it to an integer

if (isNaN(size)) {
  console.log('Missing size'); // If size is not a valid number, print "Missing size"
} else {
  let i = 0; // Initialize the row counter (starting from 0)
  while (i < size) { // Loop until we've printed 'size' number of rows
    console.log('X'.repeat(size)); // Print 'X' repeated 'size' times (this creates one row)
    i++; // Move to the next row by increasing i
  }
}
