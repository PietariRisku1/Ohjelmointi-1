let numerot = [];

while (true) {
  let syöte = Number(prompt("Anna numero (0 lopettaa):"));
  if (syöte === 0) {
    break;
  }
  numerot.push(syöte);
}

numerot.sort((a, b) => b - a);

console.log("Numerot suurimmasta pienimpään:");
for (let i = 0; i < numerot.length; i++) {
  console.log(numerot[i]);
}
