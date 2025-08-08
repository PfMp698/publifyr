
$(document).ready(function () {
  /* header */
  var $toggler = $('.navbar-toggler');
  var $nav = $('.nav');
  var $navItems = $('.nav-item a');
  var $body = $('body');

  $toggler.on('click', function() {
    $(this).toggleClass('active');
    $nav.toggleClass('active');
    $body.toggleClass('no-scroll');
  });

  $navItems.on('click', function() {
    if ($(window).width() <= 991) {
      $toggler.removeClass('active');
      $nav.removeClass('active');
      $body.removeClass('no-scroll');
    }
  });

  $(window).on('resize', function() {
    if ($(this).width() > 991) {
      $toggler.removeClass('active');
      $nav.removeClass('active');
      $body.removeClass('no-scroll');
    }
  });
  /* header */

  /* author-testimonial*/
  $(".author-testimonials").slick({
    dots: false,
    arrows: false,
    slidesToShow: 3,
    slidesToScroll: 1,
    responsive: [
      {
        breakpoint: 1200,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1,
        }
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
    ]
  });
  /* author-testimonial*/



});