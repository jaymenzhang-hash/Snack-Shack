const header = document.querySelector('.site-header');
const toggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelectorAll('#site-nav a');

toggle.addEventListener('click', () => {
  const isOpen = header.classList.toggle('open');
  toggle.setAttribute('aria-expanded', isOpen);
  toggle.querySelector('span').textContent = isOpen ? '−' : '+';
});

navLinks.forEach((link) => link.addEventListener('click', () => {
  header.classList.remove('open');
  toggle.setAttribute('aria-expanded', 'false');
  toggle.querySelector('span').textContent = '+';
}));

document.querySelectorAll('.product-photo').forEach((photo) => {
  ['stock-back far', 'stock-back near'].forEach((className) => {
    const duplicate = photo.cloneNode(true);
    duplicate.className = className;
    duplicate.alt = '';
    duplicate.setAttribute('aria-hidden', 'true');
    photo.before(duplicate);
  });
});
