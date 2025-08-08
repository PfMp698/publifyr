// JavaScript Document
$(document).ready(function() {
	/* navigation */
	$(".hamburger").click(function(){
		$(this).toggleClass("is-active");
	  });
	document.addEventListener('click',function(e){
		/* Hamburger menu */
		if(e.target.classList.contains('hamburger-toggle')){
			e.target.children[0].classList.toggle('active');
		}
	});
	$(".navbar-toggler").click(function () {
		$("html").toggleClass("nav-menu-open overflow-hidden");
	});
	$(".close").click(function () {
		$("html").toggleClass("nav-menu-open overflow-hidden");
	});
	/* navigation */

	/*carousel */
	$('.carousel').slick({
		dots: false,
		arrows: false,
		infinite: true,
		autoplay: true,
		autoplaySpeed: 2000,
		speed: 600,
		slidesToShow: 3,
		slidesToScroll: 1,
		responsive: [
			{
				breakpoint: 992,
				settings: {
					slidesToShow: 2,
					slidesToScroll: 1
				}
			},
		]
	});
	/* lazyload */
	var myLazyLoad = new LazyLoad();
	myLazyLoad.update();
	/* lazyload */
	/* OFI Browser */
	objectFitImages();
});

