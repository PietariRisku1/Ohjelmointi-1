document.getElementById("vitsihaku").addEventListener("submit", function(event) {
  event.preventDefault()
  var sana = document.getElementById("hakusana").value
  var osoite = "https://api.chucknorris.io/jokes/search?query=" + sana

  fetch(osoite)
    .then(function(vastaus) {
      return vastaus.json()
    })
    .then(function(data) {
      var vitsit = document.getElementById("vitsit")
      vitsit.innerHTML = ""

      data.result.forEach(function(vitsi) {
        var artikkeli = document.createElement("article")
        var p = document.createElement("p")
        p.textContent = vitsi.value
        artikkeli.appendChild(p)
        vitsit.appendChild(artikkeli)
      })
    })
    .catch(function(virhe) {
      console.log("Virhe:", virhe)
    })
})
