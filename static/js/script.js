var cards = document.getElementsByClassName("card__description");
for (var i = 0; i < cards.length; i++) {
    console.log(i)
    var sliced = cards[i].innerText.slice(0,256);
    if (sliced.length < cards[i].innerText.length) {
        sliced += '...';
    }
    cards[i].innerText = sliced
}
