
  //fakeloader
  $(document).ready(function(){
    $.fakeLoader({
      timeToHide:2200,
      bgColor:"#3b5998",
      // spinner:"spinner1",
      //spinner:"spinner2",
      // spinner:"spinner3",
      // spinner:"spinner4",
      //spinner:"spinner5",
      //spinner:"spinner6",
      spinner:"spinner7"
    });
  });



  window.replainSettings = { id: '22a79ec8-f81f-421c-a2af-f8fa85717e37' };
  (function(u){var s=document.createElement('script');s.async=true;s.src=u;
  var x=document.getElementsByTagName('script')[0];x.parentNode.insertBefore(s,x);
  })('https://widget.replain.cc/dist/client.js');



  // Crol to top
  var $btnTop = $(".btn-top");
  $(window).on("scroll",function(){
    if($(window).scrollTop() >= 20)
    {
      $btnTop.fadeIn();
    }
    else{
      $btnTop.fadeOut();
    }
  });
  $btnTop.on("click",function(){
    $("html,body").animate({scrollTop:0},1200)
  });



  $(document).ready(function(){
    // invoke the carousel
        $('#myCarousel').carousel({
          interval:6000
        });
    
    // scroll slides on mouse scroll 
    $('#myCarousel').bind('mousewheel DOMMouseScroll', function(e){
    
            if(e.originalEvent.wheelDelta > 0 || e.originalEvent.detail < 0) {
                $(this).carousel('prev');
          
          
            }
            else{
                $(this).carousel('next');
          
            }
        });
    
    //scroll slides on swipe for touch enabled devices 
    
       $("#myCarousel").on("touchstart", function(event){
     
            var yClick = event.originalEvent.touches[0].pageY;
          $(this).one("touchmove", function(event){
    
            var yMove = event.originalEvent.touches[0].pageY;
            if( Math.floor(yClick - yMove) > 1 ){
                $(".carousel").carousel('next');
            }
            else if( Math.floor(yClick - yMove) < -1 ){
                $(".carousel").carousel('prev');
            }
        });
        $(".carousel").on("touchend", function(){
                $(this).off("touchmove");
        });
    });
        
    });
    //animated  carousel start
    $(document).ready(function(){
    
    //to add  start animation on load for first slide 
    $(function(){
        $.fn.extend({
          animateCss: function (animationName) {
            var animationEnd = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
            this.addClass('animated ' + animationName).one(animationEnd, function() {
              $(this).removeClass(animationName);
            });
          }
        });
           $('.item1.active img').animateCss('slideInDown');
           $('.item1.active h2').animateCss('zoomIn');
           $('.item1.active p').animateCss('fadeIn');
           
    });
      
    //to start animation on  mousescroll , click and swipe
    
    
     
         $("#myCarousel").on('slide.bs.carousel', function () {
        $.fn.extend({
          animateCss: function (animationName) {
            var animationEnd = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
            this.addClass('animated ' + animationName).one(animationEnd, function() {
              $(this).removeClass(animationName);
            });
          }
        });
      
    // add animation type  from animate.css on the element which you want to animate
    
        $('.item1 img').animateCss('slideInDown');
        $('.item1 h2').animateCss('zoomIn');
        $('.item1 p').animateCss('fadeIn');
        
        $('.item2 img').animateCss('zoomIn');
        $('.item2 h2').animateCss('swing');
        $('.item2 p').animateCss('fadeIn');
        
        $('.item3 img').animateCss('fadeInLeft');
        $('.item3 h2').animateCss('fadeInDown');
        $('.item3 p').animateCss('fadeIn');
        });
    });
    
