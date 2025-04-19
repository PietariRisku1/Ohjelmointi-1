let osallistujat = [];
let määrä = Number(prompt("Kuinka monta osallistujaa?"));

for (let i = 0; i < määrä; i++) {
  let nimi = prompt(`Anna osallistujan ${i + 1} nimi:`);
  osallistujat.push(nimi);
}

osallistujat.sort();

let lista = document.getElementById("lista");
for (let i = 0; i < osallistujat.length; i++) {
  let kohta = document.createElement("li");
  kohta.textContent = osallistujat[i];
  lista.appendChild(kohta);
}