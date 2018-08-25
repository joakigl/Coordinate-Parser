function initMap() {
  //var uluru = {lat: -25.363, lng: 131.044};
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 17,
    center: new google.maps.LatLng(63.417623,10.404519),
    mapTypeId: 'terrain'
  });


  var infowindow = new google.maps.InfoWindow();
  // When the user clicks, open an infowindow
  map.data.addListener('click', function(event) {
    if(event.feature.getProperty("description")!=undefined){
  	   var myHTML = event.feature.getProperty("description");
  	   infowindow.setContent("<div style='width:150px;'>"+myHTML+"</div>");
  	   // position the infowindow on the marker
  	   infowindow.setPosition(event.feature.getGeometry().get());
  	   // anchor the infowindow on the marker
  	   infowindow.setOptions({pixelOffset: new google.maps.Size(0,-30)});
  	   infowindow.open(map);
    }
  });

  // Color Capital letters blue, and lower case letters red.
  // Capital letters are represented in ascii by values less than 91
  map.data.setStyle(function(feature) {
      var color = feature.getProperty("color");
      //var color = ascii > 91 ? 'red' : 'blue';
      if(feature.getProperty("importence")){
        //console.log("importence is false");
        var mark = {
          path: google.maps.SymbolPath.CIRCLE,
          scale: 5,
          fillColor: color,
          fillOpacity: 1,
          strokeColor: color,
          strokeWeight: 1
        }
      }else{
        var mark = {
          path: google.maps.SymbolPath.CIRCLE,
          scale: 3,
          fillColor: color,
          fillOpacity: 1,
          strokeColor: color,
          strokeWeight: 1
        }
      }
      //marker = createMarker(color,map,feature.position);
      return {
        strokeColor: color,
        strokeWeight: 3,
        icon: mark
      };
  });



  setInterval(
    function(){
      map.data.forEach(function(feature) {
        map.data.remove(feature);
        });
      map.data.loadGeoJson('geoJson.json');
    },10000);
}



window.addEventListener("load", function () {
  initMap();
});
