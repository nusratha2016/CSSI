function showWhenClicked() {
    $("#pig").show();
}

function hideWhenClicked() {
    $("#pig").hide();
}

function flyWhenClicked() {
    $("#pig").Animate({left: '500px';},10000});
}


function setup() {
    $("#showPig").click(showWhenClicked);
    $("#hidePig").click(hideWhenClicked);
    $("#flyPig").click(flyWhenClicked);
}

$(document).ready(setup);

function color()
{
  window.alert('Hello');
}
