/**
 * @author Marcus Willock
 */

$(document).ready(function(){
	
	//alert("Are you working?");
	
	function geoLocation(){
		
		if(navigator.geolocation){
			
			navigator.geolocation.getCurrentPosition(showPosition);
		}
		else{
			console.log("The geolocation function did not work...");
		}
	}
	
	function showPosition(position){
		
		console.log("Latitude: " + position.coords.latitude);
		console.log("Longitude: " + position.coords.longitude);
		
		//var latitude  = position.coords.latitude;
		//var longitude = position.coords.longitude;
		$("#form").find("input :eq(0)").attr("value", position.coords.latitude );
		$("#form").find("input :eq(1)").attr("value", position.coords.longitude);
		
		/*
		$.ajax({
			type: "POST",
			url: "/",
			data: {"latitude": position.coords.latitude, "longitude":position.coords.longitude},
			success: function(data) {console.log(data);}
		});
		*/
	}

	geoLocation();

});