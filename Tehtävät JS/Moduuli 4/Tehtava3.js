document.getElementById("hakulomake").addEventListener("submit", function(event) {
  event.preventDefault()
  var arvo = document.getElementById("query").value
  var osoite = "https://api.tvmaze.com/search/shows?q=" + arvo

  fetch(osoite)
    .then(function(vastaus) {
      return vastaus.json()
    })
    .then(function(data) {
      var tulokset = document.getElementById("results")
      tulokset.innerHTML = ""

      data.forEach(function(tvShow) {
        var artikkeli = document.createElement("article")

        var otsikko = document.createElement("h2")
        otsikko.textContent = tvShow.show.name
        artikkeli.appendChild(otsikko)

        var linkki = document.createElement("a")
        linkki.href = tvShow.show.url
        linkki.textContent = "Lisätiedot"
        linkki.target = "_blank"
        artikkeli.appendChild(linkki)

        if (tvShow.show.image?.medium) {
          var kuva = document.createElement("img")
          kuva.src = tvShow.show.image.medium
          kuva.alt = tvShow.show.name
          artikkeli.appendChild(kuva)
        }

        var yhteenveto = document.createElement("div")
        yhteenveto.innerHTML = tvShow.show.summary
        artikkeli.appendChild(yhteenveto)

        tulokset.appendChild(artikkeli)
      })
    })
    .catch(function(virhe) {
      console.log("Virhe:", virhe)
    })
})
