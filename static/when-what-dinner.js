$(function() {
    $('button').click(function() {
        var user = $('#txtDate').val();
        var pass = $('#txtDinner').val();
        $.ajax({
            url: '/',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
