/**
 * Created by ysw on 2017-03-08.
 */
$(function(){
    $("#drawer_tack").click(function() {
        if ($(".mdl-layout__drawer").hasClass("active")) {
            $(".mdl-layout__drawer").removeClass("active");
            $("layout").removeClass("mdl-layout--fixed-drawer")
        } else {
            $(".mdl-layout__drawer").addClass("active");
            $("layout").addClass("mdl-layout--fixed-drawer")
            $(".mdl-layout__drawer").removeClass("is-visible").attr("aria-hidden", true);
            $(".mdl-layout__obfuscator ").removeClass("is-visible");
        }
    });
})