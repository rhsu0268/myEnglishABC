console.log("On the dictionary page!");

$( "#translate_text" ).click(function() {
	console.log("Translate button is clicked!");

	var sentence = $('#sentence').val();
	console.log(sentence);
	if (!sentence || sentence == "" || sentence == "Enter your sentence here.")
	{
		console.log("Please enter some text!");
		return;
	}
	else 
	{
  		var translateAPI = "https://www.googleapis.com/language/translate/v2?key=AIzaSyDyXIh9jVvbng3U7mmnte1yGoEsLYB4RmA&source=en&target=zh-TW&q=" + sentence;
  		$.getJSON( translateAPI, {
    	
    		//format: "json"
  		})
    	.done(function( data ) {
   			console.log(data);

   			$.each( data.data.translations, function( i, item ) {
        		//$( "<img>" ).attr( "src", item.media.m ).appendTo( "#images" );
        		console.log(item);
      		});
    	});
    }
	
});