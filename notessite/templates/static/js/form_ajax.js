var frm = $('.note_form');
    frm.submit(function (ev) {
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: frm.serialize(),
            dataType: 'json',
            success: function (data) {
                frm.find('.error').remove();
                if (data['result'] == 'success') {
                    alert('Note was added');
                }
                else if (data['result'] == 'error') {
                    for (var k in data['response']) {
                        $('#id_'+k).before('<div class="error">' + data['response'][k] + '</div>');
                    }
            }
        }
        });
        ev.preventDefault();
    });
