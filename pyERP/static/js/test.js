$(function() {

    var json_url = '../api/currency/1';

    function return_struct() {
                var d = $.Deferred()
                $.getJSON(json_url).done(function(result) {
                    return d.resolve(result["objects"]);
            });
            return d.promise()
        };


    // jsonBody = jQuery.parseJSON(ready_json);
    // var jsonBody = JSON.stringify(ready_json);

    // var jsonBody = ready_json.success;

    console.log(return_struct());
    // console.log(ready_json);
    // console.log(jsonBody);

})