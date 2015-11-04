function createRequest() {
  try {
    request = new XMLHttpRequest();
  } catch (trymicrosoft) {
    try {
      request = new ActiveXObject ("Msxml2.XMLHTTP");
  } catch (othermicrosoft) {
    try {
      request = new ActiveXObject("Microsoft.XMLHTTP");
    } catch (failed) {
      request = null;
    }
  }
}

if (request == null)
  alert("Error creating request object!");
return request;
};


function getBigTable(){
  //ajax request to get conditions
  event.preventDefault();
  xhr = createRequest();
  xhr.open("GET", "/bigTable/", true);
  xhr.onreadystatechange = function(e) {
  if (xhr.readyState == 4) {
        var spinner= document.getElementById('spinner');
        spinner.style.visibility = "hidden";

      }
  }
}

  $(document).ready(function () {
        getBigTable();
    });