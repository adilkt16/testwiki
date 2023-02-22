$(document).ready(function(){


    $("div.first-visible").on("click",function(e){
        e.preventDefault();
        // $("div.first-invisible").toggleClass("view")
        $("div.first-invisible").css("display","inline-block")
        // $("div.first-invisible").css("display","unset")
        
        $("div.first-visible").css("display","none")
    })

    $("div.first-invisible").on("click",function(e){
        e.preventDefault();

        $("div.first-visible").css("display","inline-block")
        $("div.first-invisible").css("display","none")
    })

    ///till here it was for content small bar

    // now from here , it is individual contents
                    $("div.activeone").click(function() {
                        $("div.activeone div.clicked").slideToggle(500, function() {
                            
                        });
                        });

                    $("div.activethree").click(function() {
                        $("div.activethree div.clicked").slideToggle(500, function() {
                            
                        });
                        });

                        /////////////////////

                    $("a.copy-link").click(function (e) {
                        e.preventDefault();
                        console.log(window.location.href);
                        navigator.clipboard.writeText(window.location.href); //collecting to clipboard
                    });


                     ///below code is for search bar display and none
                    $("div.container-for-search-click").on("click",function(e){
                        e.preventDefault();
                        $("div.container").css("display","unset")
                        $("div.container-for-revert-click").css("display","unset")

                        $("div.container-for-search-click").css("display","none")
                        $("div.navbar").css("display","none")
                        $("div.main-heading").css("display","none")
                    })

                     ///below code is for revert bar display and none
                    $("div.container-for-revert-click").on("click",function(e){
                        e.preventDefault();
                        $("div.container").css("display","none")
                        $("div.container-for-revert-click").css("display","none")

                        $("div.container-for-search-click").css("display","unset")
                        $("div.navbar").css("display","unset")
                        $("div.main-heading").css("display","unset")
                    })

})

