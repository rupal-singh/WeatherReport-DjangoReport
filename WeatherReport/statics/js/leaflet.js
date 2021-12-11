var newmap = L.map('map').setView([39.7456, -97.0892], 5);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(newmap);

// L.marker([51.5, -0.09]).addTo(newmap)
//     .bindPopup('')
//     .openPopup();


function onMapClick(e) {
    var marker = L.marker(e.latlng).addTo(newmap);
    marker.bindPopup('<h2>Geo Co-ordinates</h2><br>' + marker.getLatLng()).openPopup();
    document.getElementById("lati").value = e.latlng.lat.toFixed(4)
    document.getElementById("longi").value = e.latlng.lng.toFixed(4)

    map.removeLayer(marker);
    map.removeControl(marker);

    // if (marker) {
    //     map.removeLayer(marker);
    //     map.removeControl(marker);

    // }
}

newmap.on('click', onMapClick);