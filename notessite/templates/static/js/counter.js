$(function() {
$(".read_symbols").after("<div class='write_symbols'></div>");
        $('.read_symbols').keyup(function() {
            var curLength = $(this).val().length;
            if (curLength < 0) curLength = 0;
            $(this).next('.write_symbols').html(curLength + ' symbols written');
        });
    })(jQuery);
