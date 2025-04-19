var picArray = [
  {
    title: "Kuva 1",
    medium: "https://via.placeholder.com/300x200?text=Kuva+1",
    large: "https://via.placeholder.com/800x600?text=Kuva+1+Suuri",
    caption: "Kuvateksti 1",
    description: "Tämä on kuvaus 1."
  },
  {
    title: "Kuva 2",
    medium: "https://via.placeholder.com/300x200?text=Kuva+2",
    large: "https://via.placeholder.com/800x600?text=Kuva+2+Suuri",
    caption: "Kuvateksti 2",
    description: "Tämä on kuvaus 2."
  },
  {
    title: "Kuva 3",
    medium: "https://via.placeholder.com/300x200?text=Kuva+3",
    large: "https://via.placeholder.com/800x600?text=Kuva+3+Suuri",
    caption: "Kuvateksti 3",
    description: "Tämä on kuvaus 3."
  }
];

var section = document.getElementById("artikkelit");

for (var i = 0; i < picArray.length; i++) {
  var kuva = picArray[i];

  var article = document.createElement("article");

  var otsikko = document.createElement("h2");
  otsikko.textContent = kuva.title;

  var figure = document.createElement("figure");
  var img = document.createElement("img");
  img.src = kuva.medium;
  img.alt = kuva.title;

  var figcaption = document.createElement("figcaption");
  figcaption.textContent = kuva.caption;

  figure.appendChild(img);
  figure.appendChild(figcaption);

  var teksti = document.createElement("p");
  teksti.textContent = kuva.description;

  article.appendChild(otsikko);
  article.appendChild(figure);
  article.appendChild(teksti);

  section.appendChild(article);

  article.onclick = function() {
    var dialog = document.querySelector("dialog");
    var dialogImg = dialog.querySelector("img");
    dialogImg.src = kuva.large;
    dialogImg.alt = kuva.title;
    dialog.showModal();
  };
}

var suljeNappi = document.querySelector("span");
suljeNappi.onclick = function() {
  var dialog = document.querySelector("dialog");
  dialog.close();
};
