const nav = document.querySelector('ul');
const toggle = document.querySelector('.toggle');
const Link = document.getElementsByClassName('brand');

toggle.addEventListener('click', ()=>{
 nav.classList.toggle('active') 
});


