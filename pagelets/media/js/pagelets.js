jQuery(function() {

    function setEditor(popup) {
        var value = popup.find('>:selected').val();
        var parent_form = popup.parents('form');
        var content_field_name = popup.attr('name').replace(/type$/, 'content');
        var content_field = parent_form.find('textarea[name=' + content_field_name + ']');
        if (value == 'wymeditor') {
            content_field.wymeditor({
                updateSelector: "input:submit",
                updateEvent: "click",
            });
        } else {
            content_field.siblings('div.wym_box').remove();
            content_field.css('display', 'inline');
        }
    }
    jQuery('#pagelet-form select[name=type],' +
           'body.pagelets-pagelet.change-form select[name=type],' +
           'body.pagelets-page.change-form select[name$=type]').change(function(event) {
        var popup = $(this);
        setEditor(popup);
    }).each(function (i, elem) {
        setEditor($(elem));
    });
    
});