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


function populateTable(){
  xhr = createRequest();
  xhr.onreadystatechange = function(e) {
    if (xhr.readyState == 4) {
    htmldoc = $($.parseHTML(xhr.responseText));
    document.getElementById("bigTable").innerHTML = htmldoc.find("#bigTable").html(); 
    $('#dataTables-example').dataTable()
        }
      }
    xhr.open("GET", "/bigTable/", true);
    xhr.send()

}


  $(document).ready(function () {
      $('#ageTable').dataTable();
      $('#timeTable').dataTable();
      populateTable()
     
    });