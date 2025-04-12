window.addEventListener('load', () => {
  const elements = document.querySelectorAll('.fade-in');
  elements.forEach(element => {
    element.classList.add('fade-in-active');
  });
});
