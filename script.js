function adjustImageSizes() {
  const containers = document.querySelectorAll("#projects .project-img");

  containers.forEach(container => {
      // Obține dimensiunile containerului
      const containerWidth = container.parentElement.clientWidth;
      const containerHeight = container.parentElement.clientHeight;

      // Aplică dimensiunile containerului pentru imagine
      container.style.width = `${containerWidth}px`;
      container.style.height = `${containerHeight}px`;
      container.style.objectFit = 'cover'; // Asigură proporțiile imaginii
  });
}

// Apelează funcția atunci când pagina este complet încărcată
window.addEventListener('load', adjustImageSizes);

// De asemenea, apelează funcția la redimensionarea ferestrei
window.addEventListener('resize', adjustImageSizes);
