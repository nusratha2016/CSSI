function showWhenClicked() {
    $("#pig").show();
    $("#pig2").hide();
}

function hideWhenClicked() {
    $("#pig").hide();
    $("#pig2").hide();
}

function flyWhenClicked() {
  $("#pig").animate({left: '1000px'},flyWhenClicked2);
}

function flyWhenClicked2() {
  $("#pig2").animate({left: '1000px'});
}

function setup() {
    $("#showPig").click(showWhenClicked);
    $("#hidePig").click(hideWhenClicked);
    $("#flyPig").click(flyWhenClicked);
}

$(document).ready(setup);
