var geo_lat = null;
var geo_lon = null;

function success(position) {
	geo_lat = position.coords.latitude;
	geo_lon = position.coords.longitude;
	
	document.getElementById("id_geo_lat").value = geo_lat;
	document.getElementById("id_geo_lon").value = geo_lon;
}

function error(msg) {
	var s = document.querySelector('#status');
	s.innerHTML = (typeof msg == 'string') ? msg: "It was impossible to retrive your location.";
	s.className = 'fail';
}

function hide(obj) {
	obj.style.display = 'none';
}

function displayCoords(coords) {
	var lable = document.createElement('p');
	lable.id = 'coord-lables';
	lable.innerHTML = 'Latitude, Longitude';
	document.querySelector('article').appendChild(lable);

	var disp = document.createElement('p');
	disp.id = 'coords';
	disp.innerHTML = coords.latitude + ', ' + coords.longitude;
	document.querySelector('article').appendChild(disp);
}

if ( !! navigator.geolocation) {
	navigator.geolocation.getCurrentPosition(success, error);
} else {
	error('Your browser does not support geolocation yet.');
}