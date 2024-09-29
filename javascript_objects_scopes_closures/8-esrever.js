#!/usr/bin/node

// Define the function esrever
exports.esrever = function (list) {
  const reversedList = [];

  // Loop through the list from the last element to the first
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }

  return reversedList;
};
