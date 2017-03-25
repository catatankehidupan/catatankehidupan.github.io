$(".markdown").html(marked($("textarea").val()))

function shuffle(array) {
  var currentIndex = array.length, temporaryValue, randomIndex;

  // While there remain elements to shuffle...
  while (0 !== currentIndex) {

    // Pick a remaining element...
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;

    // And swap it with the current element.
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }

  return array;
}

// Used like so
post = shuffle(post);

$(".link1 div").html(post[0].judul)
$(".link1").attr("href", post[0].link)
$(".link2 div").html(post[1].judul)
$(".link2").attr("href", post[1].link)
$(".link3 div").html(post[2].judul)
$(".link3").attr("href", post[2].link)