$(document).on('submit', 'form.dynamic-form', function(form) {
      var $form = $(form);
        $.ajax({
                type: form.method,
                url: form.action,
                data: $form.serialize(),
          });
});
