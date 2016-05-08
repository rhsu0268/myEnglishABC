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

   			$('#result').append("<ul id='sentence_list'></ul>");

   			$.each( data.data.translations, function( i, item ) {
        		//$( "<img>" ).attr( "src", item.media.m ).appendTo( "#images" );
        		console.log(item);
            var id = makeId();
            console.log(id);

        		$("#result").append("<li>" + item.translatedText + "<button type='button'" + "class='button' id='" + id + "'" + "onClick='saveSentence(this.id)'>" + "Save" + "</a></li>");

      		});
    	});
    }
	
});


function makeId()
{
  var text = "";
  var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

  for (var i = 0; i < 5; i++)
  {
    text += possible.charAt(Math.floor(Math.random() * possible.length));
  }
  return text;
}

function saveSentence(button_id)
{
  console.log("saveSentence");
  window.location.href = '/saveSentence/' + button_id;

}