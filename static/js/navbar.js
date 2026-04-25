const sc = document.getElementById('scroller');
const hd = document.getElementById('header');
const pill = document.getElementById('pill');
const hint = document.getElementById('hint');
const scene = document.getElementById('scene');
const BREAKPOINT = 520;

sc.addEventListener('scroll', () => {
  if(sc.scrollTop > 8){
    hd.classList.remove('at-top'); hd.classList.add('scrolled');
    pill.classList.add('show'); hint.classList.add('hide');
  } else {
    hd.classList.add('at-top'); hd.classList.remove('scrolled');
    pill.classList.remove('show'); hint.classList.remove('hide');
  }
});

const ro = new ResizeObserver(entries => {
  for(const e of entries) applyMode(e.contentRect.width);
});
ro.observe(scene);
applyMode(scene.offsetWidth);

function toggleMenu(){
  const m = document.getElementById('mobileMenu');
  const h = document.getElementById('ham');
  const isOpen = m.classList.toggle('open');
  h.classList.toggle('open', isOpen);
}
function closeMenu(){
  document.getElementById('mobileMenu').classList.remove('open');
  document.getElementById('ham').classList.remove('open');
}
function setA(el){
  document.querySelectorAll('.nav-links a').forEach(a=>a.classList.remove('active'));
  el.classList.add('active');
}
function setAm(el){
  document.querySelectorAll('.mobile-menu a').forEach(a=>a.classList.remove('active'));
  el.classList.add('active');
  closeMenu();
}
document.addEventListener('click', e => {
  const h = document.getElementById('ham');
  const m = document.getElementById('mobileMenu');
  if(!h.contains(e.target) && !m.contains(e.target)) closeMenu();
});
