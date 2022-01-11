const tl = gsap.timeline({defaults: {ease: "power1.out"}});

tl.to('.text', {y:'0%', duration: 1, stagger: 0.25});
tl.to('.slider', {y: '-100%', duration: 1.5, delay: 0.5});
tl.to('.intro', {y:'-100%', duration: 1}, "-=1");
tl.fromTo('nav', {opacity: 0}, {opacity: 1, duration: 1});
tl.fromTo('.big-text', {opacity: 0}, {opacity: 1, duration: 1}, "-=1");
tl.fromTo('.intro-para', {opacity: 0}, {opacity: 1, duration: 1});

const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');

    burger.addEventListener('click', ()=>{

        //toggle nav
        nav.classList.toggle('nav-active');

        // Burger animation
        burger.classList.toggle('toggle');
    });
}


/* if we have multiple functions we should invoke them like this, it 
will invoke them all at once */
const app =()=>{
    navSlide();
}

app();

