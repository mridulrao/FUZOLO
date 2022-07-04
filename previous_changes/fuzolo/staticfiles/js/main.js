const myslide = document.querySelectorAll('.myslide'),
	  dot = document.querySelectorAll('.dot');
let counter = 1;
slidefun(counter);

let timer = setInterval(autoSlide, 8000);
function autoSlide() {
	counter += 1;
	slidefun(counter);
}
function plusSlides(n) {
	counter += n;
	slidefun(counter);
	resetTimer();
}
function currentSlide(n) {
	counter = n;
	slidefun(counter);
	resetTimer();
}
function resetTimer() {
	clearInterval(timer);
	timer = setInterval(autoSlide, 8000);
}

function slidefun(n) {
	
	let i;
	for(i = 0;i<myslide.length;i++){
		myslide[i].style.display = "none";
	}
	for(i = 0;i<dot.length;i++) {
		dot[i].className = dot[i].className.replace(' active', '');
	}
	if(n > myslide.length){
	   counter = 1;
	   }
	if(n < 1){
	   counter = myslide.length;
	   }
	myslide[counter - 1].style.display = "block";
	dot[counter - 1].className += " active";
}







// window.addEventListener('scroll',function(){
// 	const parallax=this.document.querySelector('.parallax-img')
// 	let scrollPosition=window.pageYOffset;
// 	parallax.style.transform='translateY('+scrollPosition*.5+'px'
// })
// window.addEventListener('scroll',function(){
// 	const parallax=this.document.querySelector('.parallax-text-part')
// 	let scrollPosition=window.pageYOffset;
// 	parallax.style.transform='translateY('+scrollPosition*.2+'px'
// })


const loader=document.getElementById('lottie-loader');
const loaderwrap=document.getElementById('loader-wrap');
// window.onload()

// setTimeout(()=>{
// 	loader.classList.toggle('hide-lottie')
// 	loaderwrap.classList.toggle('hide-lottie-wrap')
// },2300)
// document.addEventListener("DOMContentLoaded", function() {
	setTimeout(()=>{

		loader.classList.toggle('hide-lottie')
		loaderwrap.classList.toggle('hide-lottie-wrap')
	},2700)
//   });






$('.team-and-active-cards').slick({
	slidesToShow: 4,
  slidesToScroll: 1,
//   autoplaySpeed: 1000,
  infinite: true,
//   autoplay: true, 
  pauseOnHover:false,
  pauseOnFocus:false,
  prevArrow:"<button type='button' class='slick-prev pull-left '><</button>",
  nextArrow:"<button type='button' class='slick-next pull-right'>></button>",
  responsive: [
    {
      breakpoint: 800,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1,
      }
    },
    {
      breakpoint: 400,
      settings: {
        slidesToShow: 1,
        // centerMode: true,
        autoplaySpeed: 4000,
        slidesToScroll: 1,
      }
    },
  ],
//   speed: 600,
//   arrows: false,
  });

  $('.testimonials-cards').slick({
	slidesToShow: 2,
  slidesToScroll: 1,
  pauseOnHover:false,
pauseOnFocus:false,
  autoplaySpeed: 2300,
  infinite: true,
  autoplay: true, 
   
  speed: 500,
  arrows: false,
  responsive: [
    {
      breakpoint: 800,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 1,
        // centerMode: true,
        autoplaySpeed: 4000,
        slidesToScroll: 1,
      }
    },
  ],
 
  });
	  