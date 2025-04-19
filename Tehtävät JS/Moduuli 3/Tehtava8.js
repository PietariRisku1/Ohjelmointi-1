function laske() {
  let luku1 = Number(document.getElementById("luku1").value);
  let luku2 = Number(document.getElementById("luku2").value);
  let operaatio = document.getElementById("operaatio").value;
  let tulos = 0;

  if (operaatio === "summa") {
    tulos = luku1 + luku2;
  } else if (operaatio === "erotus") {
    tulos = luku1 - luku2;
  } else if (operaatio === "tulo") {
    tulos = luku1 * luku2;
  } else if (operaatio === "jako") {
    if (luku2 !== 0) {
      tulos = luku1 / luku2;
    } else {
      document.getElementById("result").textContent = "Ei voida jakaa nollalla.";
      return;
    }
  }

  document.getElementById("result").textContent = "Tulos: " + tulos;
}
