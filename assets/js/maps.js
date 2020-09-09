function initMap() {
    // The location of sunsetBeach
    var sunsetBeach = {lat: 10.576643, lng: 103.296556};
    // The map, centered at sunsetBeach
    var map = new google.maps.Map(
        document.getElementById('map'), {
            zoom: 11, 
            center: sunsetBeach,
            mapTypeControl: false,
            panControl: false,
            streetViewControl: false,
        });
    // The marker, positioned at sunsetBeach
    var marker = new google.maps.Marker({position: sunsetBeach, map: map});
  }