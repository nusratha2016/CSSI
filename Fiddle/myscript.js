function showWhenClicked() {
    $("#pig").show();
}

function hideWhenClicked() {
    $("#pig").hide();
}

function flyWhenClicked(){
  $("#pig").fly();
}

function setup() {
    $("#showPig").click(showWhenClicked);
    $("#hidePig").click(hideWhenClicked);
    $("#flyPig").click(flyWhenClicked);
}

$(document).ready(setup);

$(document).ready(function(){
    $("button").click(function(){
        $("div").animate({left: '250px'});
    });
});
