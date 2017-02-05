var availableTags = [
    "ActionScript",
];

$(function() {


    
    
    fetch('/api/major')
    .then(function (response) {
        var majors = response.body['major'];
        $( "#major-select" ).autocomplete({
            source: availableTags
        });
    });

    fetch('/api/option')
    .then(function (response) {
        var options = response.body['option'];
        $( "#option-select" ).autocomplete({
            source: availableTags
        });
    });
});