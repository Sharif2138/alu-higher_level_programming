#!/usr/bin/node

// Function to find the second biggest integer
const secondBiggest = () => {
  // Get command line arguments, convert them to integers and filter out NaN values
  const args = process.argv.slice(2).map(Number).filter(num => !isNaN(num));

  // If no arguments or only one argument, return 0
  if (args.length < 2) {
    console.log(0);
    return;
  }

  // Use a Set to get unique values, sort them, and get the second biggest
  const uniqueArgs = [...new Set(args)];
  uniqueArgs.sort((a, b) => b - a); // Sort in descending order

  // Print the second biggest integer
  console.log(uniqueArgs[1]);
};

// Call the function
secondBiggest();
