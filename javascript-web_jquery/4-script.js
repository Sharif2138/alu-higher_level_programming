// Wait for the document to be fully loaded
$(document).ready(function() {
    // Set up a click event listener on the div with id 'toggle_header'
    $('#toggle_header').click(function() {
      // Check if the header currently has the class 'red'
      if ($('header').hasClass('red')) {
        // If it does, remove 'red' and add 'green'
        $('header').removeClass('red').addClass('green');
      } else {
        // If it doesn't, remove 'green' and add 'red'
        $('header').removeClass('green').addClass('red');
      }
    });
  });
  