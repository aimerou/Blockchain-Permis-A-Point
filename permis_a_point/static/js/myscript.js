$(function() {

    $("#home").hide();
    $("body").hide().fadeIn(800,()=>{
        $("#home").slideDown(800);
    });

    $("#more").hide();
    $("#btnless").hide();
    $("#btnmore").click(()=>{
        $("#more").show();
        $("#btnless").show();
        $("#btnmore").hide();
    })
    $("#btnless").click(()=>{
        $("#more").hide();
        $("#btnmore").show();
        $("#btnless").hide();
    })

    /**
    * Smooth scrolling to a specific element
    **/
    function scrollTo( target ) {
        if( target.length ) {
            target.hide();
            target.slideDown(1000);
            $("html, body").animate( { scrollTop: target.offset().top }, 400);
        }
    }

    $("#btnpermis").click(()=>{
        scrollTo( $("#permis") );
    })
    
    $("#btninfractions").click(()=>{
        scrollTo( $("#infractions") );
    })

    $("#btnhome").click(()=>{
        scrollTo( $("#home") );
    })
});
