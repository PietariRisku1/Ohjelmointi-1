let ehdokkaat = [];
let ehdokasMaara = Number(prompt("Kuinka monta ehdokasta?"));

for (let i = 0; i < ehdokasMaara; i++) {
  let nimi = prompt(`Ehdokkaan ${i + 1} nimi:`);
  ehdokkaat.push({ name: nimi, votes: 0 });
}

let aanestajat = Number(prompt("Kuinka monta äänestäjää?"));

for (let i = 0; i < aanestajat; i++) {
  let aanestys = prompt(`Äänestäjä ${i + 1}, ketä äänestät?`);
  if (aanestys === "") {
    continue;
  }
  for (let j = 0; j < ehdokkaat.length; j++) {
    if (ehdokkaat[j].name.toLowerCase() === aanestys.toLowerCase()) {
      ehdokkaat[j].votes++;
    }
  }
}

ehdokkaat.sort((a, b) => b.votes - a.votes);

let voittaja = ehdokkaat[0];
console.log(`Voittaja on ${voittaja.name} ${voittaja.votes} äänellä.`);
console.log("Tulokset:");
for (let i = 0; i < ehdokkaat.length; i++) {
  console.log(`${ehdokkaat[i].name}: ${ehdokkaat[i].votes} ääntä`);
}
