var has_next_page = true,
    entries_container = $('#entries_container'),
    entries_url = entries_container.data('entries'),
    custom_entries_url = entries_url.concat('?category_id=' + entries_container.data('category_id'));

var load_more = function (url) {
    $.ajax({
        url: url,
        type: "GET",

        success: function(html) {
            entries_container.append(html);
            has_next = window.has_next || false;
            if (!has_next) {
                $("#read-more-questions").hide();
            }
        }
    });
};

var next_page_number = 1;

$(function() {
    load_more(custom_entries_url);

    $("#read-more-questions").bind('click', function(e) {
        e.preventDefault();

        if (has_next) {
            next_page_number += 1;
            next_page_url = custom_entries_url.concat('&page=' + next_page_number);
            load_more(next_page_url);
        }
    });
});
