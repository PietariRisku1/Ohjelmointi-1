let numerot = [];

for (let i = 0; i < 5; i++) {
  let syöte = prompt(`Anna numero ${i + 1}:`);
  let numero = Number(syöte);
  numerot.push(numero);
}

console.log("Numerot käänteisessä järjestyksessä:");
for (let i = numerot.length - 1; i >= 0; i--) {
  console.log(numerot[i]);
}
