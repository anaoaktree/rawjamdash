


/*=============================================================
    Authour URI: www.binarycart.com
    License: Commons Attribution 3.0

    http://creativecommons.org/licenses/by/3.0/

    100% To use For Personal And Commercial Use.
    IN EXCHANGE JUST GIVE US CREDITS AND TELL YOUR FRIENDS ABOUT US
   
    ========================================================  */


(function ($) {
    var mainApp = {

        main_fun: function () {
            /*====================================
            METIS MENU 
            ======================================*/
            $('#main-menu').metisMenu();

            /*====================================
              LOAD APPROPRIATE MENU BAR
           ======================================*/
            $(window).bind("load resize", function () {
                if ($(this).width() < 768) {
                    $('div.sidebar-collapse').addClass('collapse')
                } else {
                    $('div.sidebar-collapse').removeClass('collapse')
                }
            });

            var pathname = window.location.pathname;

            switch(pathname):
                case '/':
                    $('.menu-item').removeClass('active-menu');
                    $('.menu-item-one').addClass('active-menu');
                    break;
                case '/tables/':
                    $('.menu-item').removeClass('active-menu');
                    $('.menu-item-two').addClass('active-menu');
                    break;
        }
    }

    // Initializing ///

    $(document).ready(function () {
        mainApp.main_fun();
    });

}(jQuery));
