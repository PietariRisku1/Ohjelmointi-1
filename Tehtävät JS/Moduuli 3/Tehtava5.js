const picArray = [
  {
    title: "Kuva 1",
    medium: "https://via.placeholder.com/300x200?text=Kuva+1",
    caption: "Kuvateksti 1",
    description: "Tämä on kuvauksen teksti kuvasta 1."
  },
  {
    title: "Kuva 2",
    medium: "https://via.placeholder.com/300x200?text=Kuva+2",
    caption: "Kuvateksti 2",
    description: "Tämä on kuvauksen teksti kuvasta 2."
  },
  {
    title: "Kuva 3",
    medium: "https://via.placeholder.com/300x200?text=Kuva+3",
    caption: "Kuvateksti 3",
    description: "Tämä on kuvauksen teksti kuvasta 3."
  }
];

const section = document.getElementById("artikkelit");

for (let kuva of picArray) {
  const article = document.createElement("article");
  article.className = "card";

  const otsikko = document.createElement("h2");
  otsikko.textContent = kuva.title;

  const figure = document.createElement("figure");

  const img = document.createElement("img");
  img.src = kuva.medium;
  img.alt = kuva.title;

  const figcaption = document.createElement("figcaption");
  figcaption.textContent = kuva.caption;

  figure.appendChild(img);
  figure.appendChild(figcaption);

  const teksti = document.createElement("p");
  teksti.textContent = kuva.description;

  article.appendChild(otsikko);
  article.appendChild(figure);
  article.appendChild(teksti);

  section.appendChild(article);
}
