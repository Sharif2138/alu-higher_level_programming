// Wait for the document to be fully loaded
$(document).ready(function() {
    // Select the div with id 'red_header' and set up a click event listener
    $('#red_header').click(function() {
      // When the div is clicked, add the 'red' class to the header
      $('header').addClass('red');
    });
  });
  