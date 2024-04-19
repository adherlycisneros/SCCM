// ABOUT US PAGE MEMBER CARDS//

// SHOW CARD BODY
$(document).ready(function() {
    $('.card').mouseenter(function() {
        var $card = $(this);
        $card.find('.member-details').fadeIn(); 
    });

    // HIDE CARD BODY
    $('.card').mouseleave(function() {
        var $card = $(this);
        $card.find('.member-details').fadeOut();
    });
});