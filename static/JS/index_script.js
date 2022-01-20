function checkCookie() {
    let username = getCookie("logged_in");
    if (username == "True") {
     alert("Welcome again " + username);
    } else {
      username = prompt("Please enter your name:", "");
      if (username != "" && username != null) {
        setCookie("username", username, 365);
      }
    }
  }

  function ReadCookie() {
    var allcookies = document.cookie;
    //document.write ("All Cookies : " + allcookies );
    
    // Get all the cookies pairs in an array
    cookiearray = allcookies.split(';');
    
    // Now take key value pair out of this array
    for(var i=0; i<cookiearray.length; i++) {
       name = cookiearray[i].split('=')[0];
       value = cookiearray[i].split('=')[1];
       if (name== "logged_in" && value == "True") {
        document.getElementById("login_status").innerHTML = "Logout";//document.write ("Key is : " + name + " and Value is : " + value);
       }
       
    }
 }