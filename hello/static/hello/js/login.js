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


function loginAdmin(event){
	event.preventDefault();
     // jQuery AJAX call for JSON
     var nuser={
     	'uname': document.getElementById("uname").value,
     	'passwd':document.getElementById("passwd").value
     };
  xhr = createRequest();
	xhr.open("POST", "/authentication", true);
  xhr.onreadystatechange = function() {
	  	if (xhr.readyState == 4) {
	  		}
	}
	xhr.send(nuser);

}


// DOM Ready =============================================================
//check jsperf for performance
document.addEventListener('DOMContentLoaded',function(){
    document.getElementById('loginBtn').addEventListener('click', loginAdmin);
});