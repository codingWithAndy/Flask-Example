// function checkCookie() {
//     let username = getCookie("logged_in");
//     if (username == "True") {
//      alert("Welcome again " + username);
//     } else {
//       username = prompt("Please enter your name:", "");
//       if (username != "" && username != null) {
//         setCookie("username", username, 365);
//       }
//     }
//   }

//   function ReadCookie() {
//     var allcookies = document.cookie;
//     //document.write ("All Cookies : " + allcookies );
    
//     // Get all the cookies pairs in an array
//     cookiearray = allcookies.split(';');
    
//     // Now take key value pair out of this array
//     for(var i=0; i<cookiearray.length; i++) {
//        name = cookiearray[i].split('=')[0];
//        value = cookiearray[i].split('=')[1];
//        if (name== "logged_in" && value == "True") {
//         document.getElementById("login_status").innerHTML = "Logout";//document.write ("Key is : " + name + " and Value is : " + value);
//        }
       
//     }
//  }

 $(document).ready(function () {
  $("#yourFormId").submit(function () {
      $("#submitBtn").attr("disabled", true);
      return true;
  });
});

$("#tweet_2").height($("#tweet_1").height());



//document.getElementById('down_1').onclick = test_click;
//document.getElementById('up_1').onclick = test_click;

//function test_click(clicked) {
//                document.getElementById('workPageNumber').innerHTML = "Button clicked, id = "
//                    + this.id;
//            }   

$('#1up').click(function() {
//do something
var workPage1 = document.getElementById('workPageNumber').innerHTML;
  
  var params = {work1_up:workPage1,work1_down:None}

  var xhr = new XMLHttpRequest();

  xhr.open('post', '../update_work', true);
  xhr.setRequestHeader('Content-type', 'application/json');

  xhr.onload = function () {
      console.log('Reached');
      document.getElementById('workPageNumber').innerHTML = this.responseText;
  }
  xhr.send(JSON.stringify(params));
});
$('#1down').click(function() {
var workPage1 = document.getElementById('workPageNumber').innerHTML;
  
  var params = {work1_up:None,work1_down:workPage1}

  var xhr = new XMLHttpRequest();

  xhr.open('post', '../update_work', true);
  xhr.setRequestHeader('Content-type', 'application/json');

  xhr.onload = function () {
      console.log('Reached');
      document.getElementById('workPageNumber').innerHTML = this.responseText;
  }
  xhr.send(JSON.stringify(params));
});

//https://www.youtube.com/watch?v=rxYBDOgdwDs
//document.getElementById("ajaxTest").addEventListener('submit', getData)

function getData(e) {
  e.preventDefault();

  var workPage1 = document.getElementById('workPageNumber').innerHTML;
  
  var params = {work1:workPage1}

  var xhr = new XMLHttpRequest();

  xhr.open('post', '../update_work', true);
  xhr.setRequestHeader('Content-type', 'application/json');

  xhr.onload = function () {
      console.log('Reached');
      document.getElementById('workPageNumber').innerHTML = this.responseText;
  }
  xhr.send(JSON.stringify(params));
}

  if ( window.history.replaceState ) {
      window.history.replaceState( null, null, window.location.href );
  }


// https://www.youtube.com/watch?v=v2TSTKlrPwo
//function loadNewDecimal() {
//   $.ajax({
//        URL:"/update_work",
//        type: "POST",
//        dataType: "json",
//        success: function(data) {
//            $(one).replaceWith(data)
//        }
//    });
//}

var d = $('#tweet_1');
//d.scrollTop(d.prop("scrollHeight"));