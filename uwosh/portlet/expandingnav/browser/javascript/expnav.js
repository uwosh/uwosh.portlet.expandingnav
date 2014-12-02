jQuery(document).ready(function(){

    jQuery(".expNavTree").click(function (e) {
       jQuery(e.target).children(".navTree").slideToggle("slow");
    });

});
