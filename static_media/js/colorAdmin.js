(function($) {
    $(document).ready(function($) {
    	
    	var x =$("#id_color option").size();
        for (i = 0; i < x; i++) { 
		   $("#id_color option[value="+i+"]").css({"background-color":$("#id_color option[value="+i+"]").text(), "color":$("#id_color option[value="+i+"]").text()});
		}

		 $( "#id_color" )
		  .change(function () {
		    var str = "";
		    $( "#id_color option:selected" ).each(function() {
		      str += $( this ).text() + " ";
		    });
		    $( "#id_color" ).css({"background-color": str, "color": str});
		  })
		  .change();

		  $("#id_color option[value='']").css({"background-color": "#fff", "color": "#fff"});
    });
})(jQuery || django.jQuery);

/*(function($) {
    $(document).ready(function($) {
    	var color
        $('#id_color').css("background-color", "yellow");
    });
})(jQuery || django.jQuery);*/