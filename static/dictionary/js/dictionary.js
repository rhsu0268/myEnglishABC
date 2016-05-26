console.log("On the dictionary page!");
console.log("TEST");

console.log("TEST 2");
console.log("Hello");


var sentence;

$( "#translate_text" ).click(function() {
	console.log("Translate button is clicked!");

  $('#result').html('');
  $('#blank-error-message').css('display',"none");

	sentence = $('#sentence').val();
	console.log(sentence);
	if (!sentence || sentence == "" || sentence == "Enter your sentence here.")
	{
		console.log("Please enter some text!");
    $('#blank-error-message').css('display',"inline");
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

   			$('#result').append("<ul id='sentence_list'>");

   			$.each( data.data.translations, function( i, item ) {
        		//$( "<img>" ).attr( "src", item.media.m ).appendTo( "#images" );
        		console.log(item);
            var id = makeId();
            console.log(id);

        		$("#result").append("<li class='translation' >" + item.translatedText + "</li>");
            //$("#result").append("<li>" + item.translatedText + "<button type='button'" + "class='button' id='" + id + "'" + ">" + "Save" + "</button></li>");
      		});

        $('#result').append("</ul>");


        $('#save_word').css('visibility',"visible");
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

function saveSentence(id)
{
  console.log("saveSentence");
  console.log(id);
  var id = id.getAttribute("id");
  console.log(id);
  //window.location.href = 'saveSentence/' + id;

}

var csrftoken = getCookie('csrftoken');
$( '#save_word' ).click(function() {

  console.log("SAVE BUTTON CLICKED!");
  if (chinese_text == "")
  {
    return;
  }

  var chinese_text = $( ".translation").text();
  console.log(chinese_text);
  console.log(sentence);

  $.ajax({

    url: "/dictionary/saveWord/",
    type: "POST",
    data: { text: sentence, 
            chinese_text: chinese_text,
            csrfmiddlewaretoken: csrftoken
    }

  }).done(function(data) {
    console.log("success");
    alert(data);

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


