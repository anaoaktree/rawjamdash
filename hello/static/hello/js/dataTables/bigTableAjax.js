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

}

  $(document).ready(function () {
      xhr = createRequest();
      xhr.onreadystatechange = function(e) {
        if (xhr.readyState == 4) {
        table = xhr.responseText;
        log(table)
        var spinner= document.getElementById('spinner');
        spinner.style.visibility = "hidden";
      }
    }
    xhr.open("GET", "/bigTable/", true);
    xhr.send()
    });