#!/usr/bin/node

const factorial = (n) => {
  // If n is NaN, return 1
  if (isNaN(n)) return 1;
  // Base case: if n is 0, return 1
  if (n === 0) return 1;
  // Recursive case
  return n * factorial(n - 1);
};

// Get the first argument passed to the script
const num = parseInt(process.argv[2]);

// Calculate and print the factorial
console.log(factorial(num));
