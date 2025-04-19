let koirat = [];

for (let i = 0; i < 6; i++) {
  let nimi = prompt(`Anna koiran ${i + 1} nimi:`);
  koirat.push(nimi);
}

koirat.sort().reverse();

let lista = document.getElementById("lista");
for (let i = 0; i < koirat.length; i++) {
  let kohta = document.createElement("li");
  kohta.textContent = koirat[i];
  lista.appendChild(kohta);
}