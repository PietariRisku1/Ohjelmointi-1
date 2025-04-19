document.getElementById("hakulomake").addEventListener("submit", function(event) {
  event.preventDefault()
  var haku = document.getElementById("query").value
  var osoite = "https://api.tvmaze.com/search/shows?q=" + haku

  fetch(osoite)
    .then(function(response) {
      return response.json()
    })
    .then(function(data) {
      console.log("Hakutulokset:")
      console.log(data)
    })
    .catch(function(virhe) {
      console.log("Virhe haussa:", virhe)
    })
})
