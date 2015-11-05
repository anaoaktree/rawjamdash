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

function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = cookies[i].trim();
                     // Does this cookie string begin with the name we want?
                 if (cookie.substring(0, name.length + 1) == (name + '=')) {
                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                     break;
                 }
             }
         }
         return cookieValue;
         }
function loginAdmin(event){
	event.preventDefault();
     // jQuery AJAX call for JSON
     var nuser={
     	'uname': document.getElementById("uname").value,
     	'passwd':document.getElementById("passwd").value
     };

  xhr = createRequest();

	xhr.open("POST", "/authentication/", true);
  xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
  
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