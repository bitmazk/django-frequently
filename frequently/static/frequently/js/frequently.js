function getCSRFToken() {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, 10) == ('csrftoken' + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(10));
                break;
            }
        }
    }
    return cookieValue;
}

function initializeForm() {
    var formSeclector = '[data-class="frequently-form"]';
    $(formSeclector.concat(' input[type="submit"]')).click(function(e) {
        e.preventDefault();
        $('ul.errors').remove();
        var form = $(this).closest(formSeclector),
            questionData = {};

        questionData['name'] = $(form).find('#id-name').val();
        questionData['submitted_by'] = $(form).find('#id-submitted_by').val();
        questionData['question'] = $(form).find('#id-question').val();
        questionData['csrfmiddlewaretoken'] = getCSRFToken();

        $.ajax({
            url: $(form).attr("action"),
            type: "POST",
            data: questionData,

            success: function (json) {
                $(form).trigger('reset');
                $(form).find('#question-notification').show();
            },

            error: function (xhr, errmsg, err) {
                var resp = $.parseJSON(xhr.responseText);

                for (var prop in resp) {
                    var errors = $("<ul class='errors'></ul>"),
                        fieldSelector = formSeclector + ' #id-'.concat(prop),
                        errorItem = $("<li>" + resp[prop] + "</li>");
                    errors.append(errorItem);

                    if ($(fieldSelector).length != 0) {
                        errors.insertAfter($(fieldSelector));
                    } else {
                        $('#non-field-errors').html(errors);
                    }
                }
            }
        });
        return false;
    });
}

$(function(){
    initializeForm();
});



