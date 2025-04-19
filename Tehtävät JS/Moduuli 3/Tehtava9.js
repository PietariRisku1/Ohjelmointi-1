function laske() {
  let syote = document.getElementById("lasku").value;
  let tulos = 0;

  if (syote.includes("+")) {
    let osat = syote.split("+");
    tulos = Number(osat[0]) + Number(osat[1]);
  } else if (syote.includes("-")) {
    let osat = syote.split("-");
    tulos = Number(osat[0]) - Number(osat[1]);
  } else if (syote.includes("*")) {
    let osat = syote.split("*");
    tulos = Number(osat[0]) * Number(osat[1]);
  } else if (syote.includes("/")) {
    let osat = syote.split("/");
    if (Number(osat[1]) === 0) {
      document.getElementById("result").textContent = "Ei voida jakaa nollalla.";
      return;
    }
    tulos = Math.floor(Number(osat[0]) / Number(osat[1])); // kokonaisluku
  } else {
    document.getElementById("result").textContent = "Virheellinen syöte.";
    return;
  }

  document.getElementById("result").textContent = "Tulos: " + tulos;
}
