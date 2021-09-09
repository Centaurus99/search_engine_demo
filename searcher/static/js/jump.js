$(function() {
    $('.pagination').each(function(index, e) {
        var input_div = $(e).find('.input');
        var page_input = $(e).find('.page_input');
        var jump_btn = $(e).find('.jump_btn');
        var page_max = page_input.attr('max')

        var check = function(val) {
            var reg = /^[1-9][0-9]*$/gi;
            if (!reg.test(val)) {
                return false;
            }
            val = parseInt(val)
            return (1 <= val) && (val <= page_max)
        }

        $(page_input).focus(function() {
            input_div.removeClass('error')
        });
        $(jump_btn).click(function() {
            input_div.removeClass('error')
            if (!check(page_input.val())) {
                input_div.addClass('error')
                input_div.transition({
                    animation: 'shake',
                    duration: '200ms'
                })
            } else {
                var query = window.location.search.substring(1);
                var key_values = query.split("&");
                var params = "?page=" + page_input.val();
                for (var i = 0; i < key_values.length; i++) {
                    if (key_values[i].split("=")[0] != "page") {
                        params += "&" + key_values[i]
                    }
                }
                window.location.href = params;
            }
        });
        $(page_input).keydown(function(key) {
            input_div.removeClass('error')
            if (key.keyCode == 13) {
                jump_btn.click();
            }
        });
    });
});