function setEditor(popup) {
    var value = popup.val();
    var parent_form = popup.parents('form');
    var content_field_name = popup.attr('name').replace(/type$/, 'content');
    var content_field = parent_form.find('textarea[name=' + content_field_name + ']');

    var uninstaller = setEditor.uninstallers[content_field.data('pagelet-type')] || function(){};
    var installer = setEditor.installers[value] || function(){};

    uninstaller(value, parent_form, content_field_name, content_field);
    installer(value, parent_form, content_field_name, content_field);
    content_field.data('pagelet-type', value);
}
setEditor.installers = {}
setEditor.uninstallers = {}

setEditor.installers['wymeditor'] = function(value, form, field_name, field) {
    field.wymeditor({
        updateSelector: "input:submit",
        updateEvent: "click",
    });
}
setEditor.uninstallers['wymeditor'] = function(value, form, field_name, field) {
    jQuery.each(WYMeditor.INSTANCES, function() {
      if(this._element.attr('name') == field.attr('name')){
          this.update();
          $(this._box).remove();
          $(this._element).show();
          $(this._options.updateSelector).unbind(this._options.updateEvent);
          delete this;
      }
    });
    field.siblings('div.wym_box').remove();
    field.css('display', 'inline');
}

jQuery(function($) {
    function install_editor(popup) {
        var empty_form = $(popup).parents('div.empty-form');
        if (empty_form.length == 0) {
            setEditor($(popup));
        }
    }
    var select = $('form').on('change', '[name$=type]', function() {
        install_editor($(this));
    });
    $('form [name$=type]').each(function (i) {
        install_editor($(this));
    });
});
