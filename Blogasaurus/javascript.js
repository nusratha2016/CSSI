function submitComment()
{
  var comment = $('#comment-content').val();
  $('#comments').append("<h4>Your Comment:</h4><br>" + comment + "<br>");
}

function setup()
{
  $("#submit_button").click(submitComment);
}

$(document).ready(setup);
