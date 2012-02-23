//
// This plugin is used to edit the deco textile
//
// @author Jure Cerjak, Rok Garbas
// @version 1.0
// @licstart  The following is the entire license notice for the JavaScript
//            code in this page.
//
// Copyright (C) 2010 Plone Foundation
//
// This program is free software; you can redistribute it and/or modify it
// under the terms of the GNU General Public License as published by the Free
// Software Foundation; either version 2 of the License.
//
// This program is distributed in the hope that it will be useful, but WITHOUT
// ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
// FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
// more details.
//
// You should have received a copy of the GNU General Public License along with
// this program; if not, write to the Free Software Foundation, Inc., 51
// Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
//
// @licend  The above is the entire license notice for the JavaScript code in
//          this page.
//

/*jshint bitwise:true, curly:true, eqeqeq:true, immed:true, latedef:true,
  newcap:true, noarg:true, noempty:true, nonew:true, plusplus:true,
  regexp:true, undef:true, strict:true, trailing:true, browser:true */
/*global $:false, jQuery:false, alert:false */

(function ($) {
    "use strict";

    $.fn.editTextTile = function (options){

        // merge the defaults with the provided options
        options = $.extend({}, {
            mask_options:{},
        }, options);

        var el = $(this);

        // create the edit form from the template and display it
        var showEditForm = function(){
            var editFormOptions = {
              'title': "Title",
              'tile-content': el.html()
            };
            
            var editFormTemplate = $('#'+options.template_id).html();
            var editForm = Mustache.to_html(editFormTemplate, editFormOptions);
            var editDiv = $('<div/>').appendTo($('body'));
            editDiv.attr('id', 'text-tile-edit');
            editDiv.append(editForm);
            var topOffset = $('.text-tile').offset().top - $('.modal-header').outerHeight();
            editDiv.css({
                position: 'absolute',
                top: topOffset
            })

            // scroll to top
            if($('html, body').scrollTop() > topOffset){
                $('html, body').animate({scrollTop:topOffset}, 'fast');
            }
            // initialize tinymce
            tinyMCE.init({
                mode : "textareas",
                theme : "advanced",
                // Theme options
                theme_advanced_toolbar_location : "top"
            });
        };

        // place a white mask over the page
        $(document).mask(options.mask_options);

        // create and show the edit form
        showEditForm();

        // Close and cancel button handlers
        $('.close, .cancel').click(function() {
            $('div#text-tile-edit').remove();
            $.mask.close();
        });

        // Save button handler
        $('.save').click(function() {
            var content = tinyMCE.activeEditor.getContent({format:'raw'});
            $('.text-tile').html(content);
            $('div#text-tile-edit').remove();
            $.mask.close();
        });
    };
}(jQuery));