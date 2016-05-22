console.log("Loading saved sentence");

$( '.success' ).click(function() {
	console.log("say was clicked!");
	console.log("say was clicked!");
	console.log(this.id);

	var button_id = this.id;
	console.log(button_id);

	$.ajax({

    	url: "/dictionary/sayWord/",
    	type: "POST",
    	data: { id: button_id, 
            csrfmiddlewaretoken: csrftoken
    }

  	}).done(function(data) {
    	console.log("success");
    	alert("success");

  	}); 

});