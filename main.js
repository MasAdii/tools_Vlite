window.addEventListener('load', () => {
  const fadeElements = document.querySelectorAll('.fade-in');
  fadeElements.forEach(element => {
    element.classList.add('fade-in-active');
  });
  
  const slideUpElements = document.querySelectorAll('.slide-up');
  slideUpElements.forEach(element => {
    element.classList.add('slide-up-active');
  });

  const fadeInUpElements = document.querySelectorAll('.fade-in-up');
  fadeInUpElements.forEach(element => {
    element.classList.add('fade-in-up-active');
  });
});
