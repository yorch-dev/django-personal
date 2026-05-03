window.addEventListener('DOMContentLoaded', ajustarPanel);
window.addEventListener('resize', ajustarPanel);

function ajustarPanel() {
  const contenedor = document.getElementById('panel');
  if (!contenedor) return;

  let alturaAcumulada = 0;
  let nodo = contenedor.previousElementSibling;
  while (nodo) {
    if (nodo.offsetHeight) {
      alturaAcumulada += nodo.offsetHeight;
    }
    nodo = nodo.previousElementSibling;
  }

  const menu = document.querySelector('nav');
  if (menu && !menu.contains(contenedor)) {
    alturaAcumulada += menu.offsetHeight;
  }

  const margenExtra = 0;

  const alturaRestante = window.innerHeight - alturaAcumulada - margenExtra;

  contenedor.style.maxHeight = `${alturaRestante}px`;
  contenedor.style.overflowY = 'auto';
}