var newmap = L.map('map').setView([39.7456, -97.0892], 5);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(newmap);


function onMapClick(e) {

    if (pointer) {
        map.removeLayer(pointer);
        map.removeControl(pointer);
    }

    var pointer = L.marker(e.latlng).addTo(newmap);
    pointer.bindPopup('<h2>Geo Co-ordinates</h2><br>' + pointer.getLatLng()).openPopup();
    document.getElementById("lati").value = e.latlng.lat.toFixed(4)
    document.getElementById("longi").value = e.latlng.lng.toFixed(4)
}

newmap.on('click', onMapClick);
