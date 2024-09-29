#!/usr/bin/node

// Function to compute the factorial
const factorial = (n) => {
  // Convert the argument to an integer
  n = parseInt(n);
  
  // If n is NaN or less than 0, return 1 (factorial of NaN is 1)
  if (isNaN(n) || n < 0) {
    return 1;
  }
  
  // Base case: factorial of 0 or 1 is 1
  if (n === 0 || n === 1) {
    return 1;
  }

  // Recursive case: n * factorial of (n - 1)
  return n * factorial(n - 1);
};

// Get the first argument passed to the script
const input = process.argv[2];

// Compute and print the factorial
console.log(factorial(input));
