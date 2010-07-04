var map;

function spawnMap() {
	var mapcanvas = document.getElementById("map");
	mapcanvas.style.height = '400px';
	mapcanvas.style.width = '100%';
	
	var latlng = new google.maps.LatLng(geo_lat || 40.20614809577503, geo_lon || -8.41552734375);
	var myOptions = {
		zoom: 17,
		center: latlng,
		mapTypeControl: true,
		navigationControlOptions: {
			style: google.maps.NavigationControlStyle.SMALL
		},
		mapTypeId: google.maps.MapTypeId.HYBRID
	};
	map = new google.maps.Map(document.getElementById("map"), myOptions);

	loadPlaces();
}

function centerAtGeo() {
	latlng = new google.maps.LatLng(geo_lat, geo_lon);
	map.setCenter(latlng);
}