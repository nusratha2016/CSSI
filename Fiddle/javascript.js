function TaskDone(nusrathahmed)
{
   var bulletstyle = document.getElementById(nusrathahmed).style.textDecoration;
  if(bulletstyle=="line-through")
  		document.getElementById(nusrathahmed).style.textDecoration="none";
      else
    		document.getElementById(nusrathahmed).style.textDecoration="line-through";

}

function clearAll(){
names = $('.task');
names.css("text-decoration","none");
}



function AddItem(){
  var i = prompt("Enter item to add to the list");
  addListItem(i);
}


function addListItem(text){
  list = document.querySelector('ol');
  item = document.createElement('li');
  item.innerText = text;
  list.appendChild(item);
}
/*
function clearAll(){
var names= document.getElementsByClassName("task");
for (i=0; i < names.length; i++)
{
names[i].style.textDecoration="none";
}

}
*/
