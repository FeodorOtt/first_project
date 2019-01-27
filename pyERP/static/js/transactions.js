$(function(){

 var arr = new DevExpress.data.DataSource()
 arr = 'api/'

 var cli = {
     store: new DevExpress.data.CustomStore({
         key: "id",
         loadMode: "raw",
         load: function() {
             // Returns an array of objects that have the following structure:
             // { id: 1, name: "John Doe" }
             return $.getJSON('clients/api/');
         }
     }),
     sort: "name"
 }

 var curr = {
     store: new DevExpress.data.CustomStore({
         key: "id",
         loadMode: "raw",
         load: function() {
             return $.getJSON('currency/api/');
         }
     }),
     sort: "ISO_char"
 }

    $("#gridContainer").dxDataGrid({
        dataSource: arr,
        allowColumnResizing: true,
        // columnResizingMode: "nextColumn",
        columnMinWidth: 50,
        rowAlternationEnabled: true,
        allowColumnReordering: true,
        columnChooser: {
            enabled: true,
            mode: "select"
        },
        columns: [{
                    dataField: "db_client_id",
                    caption: "Клиент Дт",
                    width: 125,
                    lookup: {
                      dataSource: cli,
                      displayExpr: "name",
                      valueExpr: "id"
                    }
                  },
                  {
                    dataField: "cr_client_id",
                    caption: "Клиент Кт",
                    width: 125,
                    lookup: {
                        dataSource: cli,
                        displayExpr: "name",
                        valueExpr: "id"
                      }
                    },
                  {
                    dataField: "amount",
                    caption: "Сумма",
                    alignment: 'right',
                    dataType: "number",
                    format: "#,##0.00"
                  },
                  {
                    dataField: "currency_id",
                    caption: "Валюта",
                    lookup: {
                      dataSource: curr,
                      displayExpr: "ISO_char",
                      valueExpr: "id"
                    }
                  },
                  {
                    dataField: "amount_e",
                    caption: "Экв.",
                    alignment: 'right',
                    dataType: "number",
                    format: "#,##0.00"
                  },
                  {
                    dataField: "payment_details",
                    caption: "Примечание",
                  },
                 ],
        filterRow: {
            visible: true
        },
        headerFilter: {
            visible: true
        },
        groupPanel: {
            visible: true
        },
        scrolling: {
            mode: "virtual"
        },
        height: 600,
        showBorders: true,
        selection: {
            mode: "multiple"
        },
        editing: {
            allowAdding: true,
            allowUpdating: true,
            allowDeleting: true
        },
        grouping: {
            autoExpandAll: false
        },
        summary: {
            totalItems: [{
                    column: "amount",
                    summaryType: "sum",
                    valueFormat: "#,##0.00",
                    displayFormat: "{0}"
                }, {
                    column: "amount_e",
                    summaryType: "sum",
                    valueFormat: "#,##0.00",
                    displayFormat: "{0}"
                }, {
                    column: "payment_details",
                    summaryType: "count",
                    displayFormat: "Всего: {0}"
                }
              ],
            groupItems: [{
                    column: "amount",
                    summaryType: "sum",
                    valueFormat: "#,##0.00",
                    displayFormat: "{0}",
                    alignByColumn: true
                }, {
                    column: "amount_e",
                    summaryType: "sum",
                    valueFormat: "#,##0.00",
                    displayFormat: "{0}",
                    alignByColumn: true
                  },
                 {
                    column: "payment_details",
                    summaryType: "count",
                    displayFormat: "Всего: {0}",
                    alignByColumn: true
                }
            ]
        }
    });
});
