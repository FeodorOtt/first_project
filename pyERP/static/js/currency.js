$(function(){

    var json_url = '../api/currency/'

    var currency = new DevExpress.data.CustomStore({
        key: "id",
        // loadMode: "raw",
        load: function(loadOptions) {
            var d = $.Deferred();
            $.getJSON(json_url).done(function(result) {
                d.resolve(result["objects"]);
            });
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

    $("#gridContainer").dxDataGrid({
        dataSource: {
            store: currency
        },
        export: {
            enabled: true,
            fileName: "Currency",
            allowExportSelectedData: true
        },
        allowColumnResizing: false,
        allowColumnReordering: false,
        cacheEnabled: true,
        columnMinWidth: 50,
        rowAlternationEnabled: true,
        hoverStateEnabled: true,
        stateStoring: {
            enabled: true,
            type: "localStorage",
            storageKey: "currency"
        },
        loadPanel: {
            shading: true,
            height: 120
        },
        columns: [{
            // dataField: "id",
            // }, {
            dataField: "name",
            caption: formatMessage("name"),
            width: '45%'
            }, {
            dataField: "short_name",
            caption: formatMessage("short_name"),
            width: '25%'
            }, {
            dataField: "ISO_digit",
            caption: formatMessage("ISO_digit"),
            width: '15%'
            }, {
            dataField: "ISO_char",
            caption: formatMessage("ISO_char"),
            width: '15%'
            },
        ],
        editing: {
            allowAdding: true,
            allowUpdating: true,
            allowDeleting: true,
            useIcons: true
        },
        filterRow: {
            filterEnabled: true,
            visible: true
        },
        filterPanel: {
            visible: true
        },
        headerFilter: {
            visible: true,
            allowSearch: true
        },
        scrolling: {
            mode: "virtual"
        },
        showBorders: true,
        selection: {
          mode: "single"
        }
    });

});
