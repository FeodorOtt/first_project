$(function(){
    var currency = json_crud('../api/currency/');

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
            width: '35%'
            }, {
            dataField: "latin_name",
            caption: formatMessage("latin_name"),
            width: '35%'
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
            useIcons: true,
            mode: "form",
            form: {
                minColWidth: 50,
                colCount: 2,
                focusStateEnabled: true
                // items: [{
                //     itemType: "group",
                //     caption: formatMessage("idCurrency"),
                // }]
            }
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
