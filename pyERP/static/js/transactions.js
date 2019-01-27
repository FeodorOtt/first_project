$(function(){
 var arr = new DevExpress.data.DataSource()
 // cli = 'clients/api/'
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

    $("#gridContainer").dxDataGrid({
        dataSource: arr,
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
                    dataField: "amount",
                    caption: "Сумма",
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
                valueFormat: "currency",
                // displayFormat: ',0.00;-,0.00'
            }],
            groupItems: [{
                    column: "amount",
                    summaryType: "sum",
                    valueFormat: "currency",
                }, {
                    summaryType: "count"
                }
            ]
        }
    });
});
