//when login button is pressed
function read(){

  var username = document.getElementById("username").value
  var password = document.getElementById("pass").value
  console.log("I am Here")

  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function(){
    if(this.readyState == 4 && this.status == 200){
      document.getElementById("username").innerHTML = this.responseText;

    }
  };
  xmlhttp.open("GET", "login.py?q="+username, true);
  xmlhttp.send();
  console.log("I am Here2")
}

function deleteAd(houseId){
  console.log("Here")
  var xmlhttp = new XMLHttpRequest();
			xmlhttp.onreadystatechange = function(){
				if(this.readyState == 4 && this.status == 200){
					console.log(this.responseText)
          alert("successfully deleted!!");
				}
			};
			xmlhttp.open("GET", "deleteAdvertisement.py?q="+houseId, true);
			xmlhttp.send();
}
