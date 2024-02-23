
/*------------------------------nav--------------------------*/
$("nav a").click(function(e){
    let ahref=$(this).attr("href")
    $("body,html").animate({scrollTop:$(ahref).offset().top-30},2000)
})
/*-----------------------------type script-------------------------------*/
var typed = new Typed('.typed', {
	strings: ['Explore our menu', 'place orders' ,'make reservations'],
	typeSpeed: 100,
	backspeed:100,
	loop:true
  });
/*------------------------Home ReserVation------------------------*/
$(".reserve").click(function(e){
    let ahref=$(this).attr("href")
    $("body,html").animate({scrollTop:$(ahref).offset().top-30},2000)
})
/*----------------------------nav scroll-------------------------*/
let about=$("#about").offset().top;
$(window).scroll(function(){
    let wscroll=$(window).scrollTop()
    if(wscroll>about-40) 
    {
	$("nav").css("backgroundColor","#fff");
	$("nav a").css("color","#000");
	$(".navbar-light .navbar-toggler").css("bg-dark");
	$("#up").fadeIn(200);
    }
    else 
    {
	$("#up").fadeOut(200);
    }
});
/*------------------------angle up------------------------------------*/
$("#up").click(function(e){
    $("body,html").animate({scrollTop:'0px'},2000)
})
