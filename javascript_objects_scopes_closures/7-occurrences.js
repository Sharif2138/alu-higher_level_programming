#!/usr/bin/node

// Define the function nbOccurences
exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  // Loop through the list and check if each element matches searchElement
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }

  return count;
};
