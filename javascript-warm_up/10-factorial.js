#!/usr/bin/node

// Recursive function to compute factorial
const factorial = (n) => {
  // If n is NaN, return 1
  if (isNaN(n)) return 1;
  // Base case: if n is 0, return 1
  if (n === 0) return 1;
  // Recursive case
  return n * factorial(n - 1);
};

// Main function to handle command-line input and print the result
const main = () => {
  // Get the first argument passed to the script, default to 0 if not provided
  const num = parseInt(process.argv[2]) || 0;

  // Calculate and print the factorial
  console.log(factorial(num));
};

// Call the main function
main();
