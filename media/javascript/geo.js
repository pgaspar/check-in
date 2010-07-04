var geo_lat = null;
var geo_lon = null;

function success(position) {
	geo_lat = position.coords.latitude;
	geo_lon = position.coords.longitude;
	
	var s = document.querySelector('#geo-status');
	
	if (s.className == 'success') {
		// not sure why we're hitting this twice in FF, I think it's to do with a cached result coming back
		return;
	}
	
	s.className = 'success';
	s.innerHTML = 'Found you here: <a id="coords" href="javascript:centerAtGeo();">(' + geo_lat + ', ' + geo_lon + ')</span>';
	
	if (document.getElementById("id_geo_lat")) {
		document.getElementById("id_geo_lat").value = geo_lat;
		document.getElementById("id_geo_lon").value = geo_lon;
	}
	
	if (spawnMap != null) spawnMap();
}

function error(msg) {
	var s = document.querySelector('#geo-status');
	s.innerHTML = (typeof msg == 'string') ? msg: "It was impossible to retrive your location.";
	s.className = 'fail';
}

function hide(obj) {
	obj.style.display = 'none';
}

if ( !! navigator.geolocation) {
	navigator.geolocation.getCurrentPosition(success, error);
} else {
	error('Your browser does not support geolocation yet.');
}