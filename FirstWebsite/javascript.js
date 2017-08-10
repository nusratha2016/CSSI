function Task1Done(nusrathahmed)
{
   var bulletstyle = document.getElementById(nusrathahmed).style.textDecoration;
  if(bulletstyle=="line-through")
  		document.getElementById(nusrathahmed).style.textDecoration="none";
      else
    		document.getElementById(nusrathahmed).style.textDecoration="line-through";

}
