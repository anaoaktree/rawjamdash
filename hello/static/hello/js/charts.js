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

 xhr = createRequest();
      xhr.onreadystatechange = function(e) {
        if (xhr.readyState == 4) {
        resp = xhr.responseText
        counter.male = resp.male
        counter.female = resp.female


      }
    }
    xhr.open("GET", "/getCounter/", true);
    xhr.send()

 $(document).ready(function () {
    var counter= {
        male: 0,
        female:0,
        age1:0,
        age2:0,
        age3:0
    }
    var genderchart = c3.generate({
    bindto: '#genderChart',
    data: {
        // iris data from R
        columns: [
            ['men', 30],
            ['women', 120],
        ],
        type : 'pie',
        onclick: function (d, i) { console.log("onclick", d, i); },
        onmouseover: function (d, i) { console.log("onmouseover", d, i); },
        onmouseout: function (d, i) { console.log("onmouseout", d, i); }
    }
      var genderchart = c3.generate({
        bindto: '#ageChart',
        data: {
        // iris data from R
        columns: [
            ['< 10', 30],
            ['10-16', 44],
            ['17-23', 183],
            ['24-30', 120],
            ['31-37', 208],
            ['38-50', 74],
            ['51-59', 86],
            ['>60', 100],
        ],
        type : 'pie',
    }
});
    var genderchart = c3.generate({
    bindto: '#genderChart',
    data: {
        // iris data from R
        columns: [
            ['men', 30],
            ['women', 120],
        ],
        type : 'pie',
    }
});