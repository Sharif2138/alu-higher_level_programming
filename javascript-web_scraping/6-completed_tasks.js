#!/usr/bin/node

const request = require('request');

// The API URL is passed as the first argument
const url = process.argv[2];

// Send the GET request to the API
request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else {
    // Parse the JSON data from the response body
    const todos = JSON.parse(body);

    // Create an empty object to store the count of completed tasks per user
    const completedTasks = {};

    // Loop through all the tasks
    todos.forEach((todo) => {
      // Check if the task is completed
      if (todo.completed) {
        // If the task is completed, increase the count for the corresponding userId
        if (completedTasks[todo.userId]) {
          completedTasks[todo.userId]++;
        } else {
          completedTasks[todo.userId] = 1;
        }
      }
    });

    // Print the result: users and their number of completed tasks
    console.log(completedTasks);
  }
});
