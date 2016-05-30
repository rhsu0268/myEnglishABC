console.log("Loading saved sentence");

$( '.success' ).click(function() {
	//console.log("say was clicked!");
	console.log("say was clicked!");
	//console.log(this.id);

	var button_id = this.id;
	console.log(button_id);

	var csrftoken = getCookie('csrftoken');
    
	$.ajax({
    	url: "/dictionary/sayWord/",
    	type: "POST",
    	data: { sentence_id: button_id, 
            csrfmiddlewaretoken: csrftoken
    }
  	}).done(function(data) {
    	console.log("success");
    	//alert(data);
    	console.log(data);


        window.location.href = 'https://translate.google.com/translate_tts?ie=UTF-8&q=' + data + '&tl=en&client=tw-ob';
  	}); 
    
});

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}