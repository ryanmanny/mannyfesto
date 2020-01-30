function momentConvert() {
    let divs = $('.moment-convert').text(function(index, oldText) {
        return moment(oldText).format('LLL');
    });
}

function momentConvertDuration() {
    let divs = $('.moment-convert-duration').text(function(index, oldText) {
        return moment(oldText).fromNow();
    });
}
