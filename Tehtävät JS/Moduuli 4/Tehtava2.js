document.getElementById("hakulomake").addEventListener("submit", function(event) {
  event.preventDefault()
  var arvo = document.getElementById("query").value
  var osoite = "https://api.tvmaze.com/search/shows?q=" + arvo

  fetch(osoite)
    .then(function(vastaus) {
      return vastaus.json()
    })
    .then(function(data) {
      console.log(data)
    })
    .catch(function(virhe) {
      console.log("Virhe:", virhe)
    })
})
