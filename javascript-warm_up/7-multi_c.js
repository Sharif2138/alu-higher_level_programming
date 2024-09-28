#!/usr/bin/node
const x = process.argv[2]; // Get the first argument
const num = parseInt(x); // Convert the argument to an integer

if (isNaN(num)) {
  console.log('Missing number of occurrences'); // Handle invalid or missing argument
} else {
  let i = 0;
  while (i < num) {
    console.log('C is fun'); // Print "C is fun"
    i++;
  }
}
}
