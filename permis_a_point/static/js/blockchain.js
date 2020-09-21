$(function(){
    var sizeTheOverlays = function() {
        $(".overlay").resize().each(function() {
        var h = $(this).parent().outerHeight();
        var w = $(this).parent().outerWidth();
        $(this).css("height", h);
        $(this).css("width", w);
        });
    };

    sizeTheOverlays();

    var width = $(window).width();
    $(window).resize(function(){
        if($(this).width() != width){
            width = $(this).width();
            sizeTheOverlays();
        }
    });

    $(".bloc").mouseover(()=>{
        $(".overlay").css({opacity:1})
    })

    $(".bloc").mouseout(()=>{
        $(".overlay").css({opacity:0})
    })

 });
