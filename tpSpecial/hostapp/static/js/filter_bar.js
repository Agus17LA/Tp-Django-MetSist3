function filterSelectionCity(){
  
  var select = document.querySelector("#select_filter");
  var cards = document.querySelectorAll(".card");
  cards.forEach(function(element){
    if(select.value != "All"){
      if(element.classList.contains(select.value)){
        element.style.display= "flex";
      }else{
        element.style.display= "none";
      }
    }else{
      element.style.display="flex";
    }
  });
}

function filterMaxPersons(){
  var value = "mx-persons-"+document.getElementById("inpt-prsns").value;
  var cards = document.querySelectorAll(".card");
  cards.forEach(function(element){
    if(value != "mx-persons-"){
      if(element.classList.contains(value)){
        element.style.display= "flex";
      }else{
        element.style.display= "none";
      }
    }else{
      element.style.display="flex";
    }
  });
}