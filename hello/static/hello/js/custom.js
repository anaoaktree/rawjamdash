


/*=============================================================
    Authour URI: www.binarycart.com
    License: Commons Attribution 3.0

    http://creativecommons.org/licenses/by/3.0/

    100% To use For Personal And Commercial Use.
    IN EXCHANGE JUST GIVE US CREDITS AND TELL YOUR FRIENDS ABOUT US
   
    ========================================================  */


(function ($) {
    "use strict";
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

            /**
             * Menu items.
             */
            var href = window.location.href;

            $('.menu-item').each(function(item) {

                if(href.indexOf(item.props('href')) != -1) {
                    $(item).addClass('active-menu');
                }
            });

            initialization: function () {
                mainApp.main_fun();

            }

        }
    }

    // Initializing ///

    $(document).ready(function () {
        mainApp.main_fun();
    });

}(jQuery));
