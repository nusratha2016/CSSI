function DisplayStory(PluralNoun1, PersonInRoom, Noun1, LastName, PluralNoun2,
APlace1, PluralNoun3, Aplace2, PluralNoun4, Noun2, Adjective1, Adjective2,
Noun3, Noun4, Noun5, Verb, Adjective3) {
    var MadLib2 = "Hello there, sports " + PluralNoun1 + "! This is " + PersonInRoom +
" <br/> talking to you from the press " + Noun1 + " in " + LastName + ", Stadium, where 57,000 cheering" +
PluralNoun2 + "<br/> have gathered to watch (the) " + APlace1 + " " + PluralNoun3 + " take on (the) " +
 APlace2 + " "  + PluralNoun4 + "<br/> Even thought the " + Noun2 + " is shining, it's a/an " + Adjective1 +
  " 20s. <br/> A strong " + Noun3 + " is blowing fiercely across the playing " + Noun4 +
" that will definitely affect the passing " + Noun5 + "<br/> We'll be back for the opening " + Verb +
" off after a few words from our " + Adjective3 + ", sponsor.";
$('#output').html(MadLib2);
}

$('#submit').click(function(){
    var passThis1 = $('input[name = "PluralNoun1"]').val();
    var passThis2 = $('input[name = "PersonInRoom"]').val();
    var passThis3 = $('input[name = "Noun1"]').val();
    var passThis4 = $('input[name = "LastName"]').val();
    var passThis5 = $('input[name = "PluralNoun2"]').val();
    var passThis6 = $('input[name = "APlace1"]').val();
    var passThis7 = $('input[name = "PluralNoun3"]').val();
    var passThis8 = $('input[name = "APlace2"]').val();
    var passThis9 = $('input[name = "PluralNoun4"]').val();
    var passThis10 = $('input[name = "Noun2"]').val();
    var passThis11 = $('input[name = "Adjective1"]').val();
    var passThis12 = $('input[name = "Adjective2"]').val();
    var passThis13 = $('input[name = "Noun3"]').val();
    var passThis14 = $('input[name = "Noun4"]').val();
    var passThis15 = $('input[name = "Noun5"]').val();
    var passThis16 = $('input[name = "Verb"]').val();
    var passThis17 = $('input[name = "Adjective3"]').val();
DisplayStory(passThis1, passThis2, passThis3, passThis4, passThis5, passThis6,
passThis7, passThis8, passThis9, passThis10, passThis11, passThis12, passThis13,
passThis14, passThis15, passThis16, passThis17);

});
