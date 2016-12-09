// Any needed javascript can go here
// this is a simple app so we don't need a framework

// state variables
var googleMap 
var markers = []
var visibleMarkers = []
var systems = []

$( document ).ready(function() {
  $.getJSON('http://127.0.0.1:5000/systems')
  .done(function(systemsFromServer) {
    systems = systemsFromServer
    buildMap(systems)
    buildChart(systems)
  })
});

var buildChart = function(systems) {

  var series = systems.map(function(system) {
    return system.avg_performance
  })

  var labels = systems.map(function(system) {
    return system.name
  })
  var ctx = $('#ct-chart')
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [
        {
          data: series,
          label: 'System Performance'
        }
      ]
    },
  })
}

var buildMap = function(systems) {
  googleMap = new google.maps.Map(document.getElementById('googleMap'), {
    zoom: 4,
    center: {lat: 40.6, lng: -101.7}
  })
  systems.forEach(function(system) {
    var marker = addMarker(googleMap, system)
    markers.push(marker)
  })

  googleMap.addListener('bounds_changed', function() {
    getVisibleMarkers()
    addSystemsList()
  })    
}

var addMarker = function(googleMap, system) {
  var marker = new google.maps.Marker({
    position: {
      lat: system.latitude, 
      lng: system.longitude
    }, 
    label: system.avg_performance.toString().slice(1),  //slice removes the zero before the decimal
    systemId: system.id,
    map: googleMap
  })
  addInfoWindow(googleMap, marker, system)
  return marker
}

var addInfoWindow = function(googleMap, marker, system) {
  var infoWindow = new google.maps.InfoWindow({
    map: googleMap,
    content: system.name + '<br />' + system.model + '<br />' + system.system_size +' MW',
    anchor: marker
  });

  infoWindow.close(googleMap, marker)
  marker.addListener('mouseover', function() {
    infoWindow.open(googleMap, marker);
  });
  marker.addListener('mouseout', function() {
    infoWindow.close(googleMap, marker)
  });
}

var getVisibleMarkers = function() {
  visibleMarkers = []
  for(var i = markers.length, bounds = googleMap.getBounds(); i--;) {
    if( bounds.contains(markers[i].getPosition()) ){
      visibleMarkers.push(markers[i])
    }
  }
}

var addSystemsList = function() {
  console.log('systems', systems)
  var visibleSystems = systems.filter(function(system) {
    for(var i = 0; i < visibleMarkers.length; i++) {
      if(visibleMarkers[i].systemId === system.id) {
        return true
      }
    }
    return false
  })
  console.log(systemsListHtml)
  var systemsListHtml = visibleSystems.map(function(system) {
    return '<a href="#" class="list-group-item">' +
    '<h4 class="list-group-item-heading">'+system.name+'</h4>'+
    '<p class="list-group-item-text">Manufacturer: '+ system.manufacturer+'</p>' +
    '<p class="list-group-item-text">Average Performance: '+ system.avg_performance+'</p>' +
    '<p class="list-group-item-text">System Size: '+ system.system_size+' MW</p>' +
    "</a>"
  })

  $('#systemsList').children().remove()
  $('#systemsList').html(systemsListHtml)
  
}
