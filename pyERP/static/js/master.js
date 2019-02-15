function json_crud(json_url, url_search_params=['', '']){
    return new DevExpress.data.CustomStore({
        key: "id",
        // loadMode: "raw",
        load: function() {
            var d = $.Deferred();
            // $.getJSON(json_url).done(function(result) {
            $.getJSON(json_url+'?'+url_search_params[0]+url_search_params[1]).done(function (result) {
                        d.resolve(result["objects"]);
                        // console.log(result["objects"][0])
                    }
            );
            return d.promise();
        },

        byKey: function(key) {
            return $.getJSON(json_url + encodeURIComponent(key) + '/');
        },

        insert: function(values) {
            var d = $.Deferred()
            $.ajax({
                url: json_url,
                method: "POST",
                contentType: 'application/json',
                data: JSON.stringify(values)
            }).done(function () {
                      d.resolve(values)
                    })
            return d.promise();
        },

        update: function(key, values) {
            var d = $.Deferred()
            $.ajax({
                url: json_url + encodeURIComponent(key) + '/',
                method: "PUT",
                contentType: 'application/json',
                data: JSON.stringify(values)
            }).done(function () {
                      d.resolve(key)
                    });;
            return d.promise();
        },

        remove: function(key) {
            var d = $.Deferred()
            $.ajax({
                url: json_url + encodeURIComponent(key) + '/',
                method: "DELETE",
            }).done(function () {
                      d.resolve(key)
                    });
            return d.promise();
        }

    });
};


function json_read(json_url, sort_name = "name") {
    return {
        store: new DevExpress.data.CustomStore({
            key: "id",
            loadMode: "raw",
            load: function () {
                var d = $.Deferred();
                $.getJSON(json_url).done(function (result) {
                    return d.resolve(result["objects"]);
                });
                return d.promise();
            }
        }),
        sort: sort_name
    }
}