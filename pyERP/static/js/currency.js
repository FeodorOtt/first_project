$(function(){

    var json_url = '../api/currency/'

    var currency = new DevExpress.data.CustomStore({
        key: "id",
        // loadMode: "raw",
        load: function(loadOptions) {
            var d = $.Deferred();
            $.getJSON(json_url, {
                // // Passing settings to the server

                // filter: loadOptions.filter ? JSON.stringify(loadOptions.filter) : "", // Pass if filtering is remote
                // sort: loadOptions.sort ? JSON.stringify(loadOptions.sort) : "",       // Pass if sorting is remote
                // // Pass if paging is remote
                // skip: loadOptions.skip,     // The number of records to skip
                // take: loadOptions.take,     // The number of records to take
                // requireTotalCount: loadOptions.requireTotalCount,   // A flag telling the server whether
                //                                                     // the total count of records (totalCount) is required
                // group: loadOptions.group ? JSON.stringify(loadOptions.group) : "", // Pass if grouping is remote
                // totalSummary: loadOptions.totalSummary ? JSON.stringify(loadOptions.totalSummary) : "", // Pass if summary is calculated remotely
                // groupSummary: loadOptions.groupSummary ? JSON.stringify(loadOptions.groupSummary) : "" // Pass if grouping is remote and summary is calculated remotely

                }).done(function(result) {
                        d.resolve(result["objects"], {
                        // totalCount: result["objects"].totalCount // The count of received records; needed if paging is enabled
                //         summary: result["objects"].summary        // Needed if summary is calculated remotely
                    });
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
            // }, {
            // type: "buttons",
            // buttons: ["edit", "delete", {
            //     text: "My Command",
            //     // icon: "/url/to/my/icon.ico",
            //     hint: "My Command",
            //     onClick: function (e) {
            //             var ds = dxDataGrid("getDataSource");
            //             ds.reload();
            //         }
            //     }]
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
