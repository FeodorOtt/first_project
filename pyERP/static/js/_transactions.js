// var arr = [{
//     "db_client_id": "Bentonville",
//     "amount": "10000.05",
//     "payment_details": "702 SW 8th Street",
// }, {
//   "db_client_id": "ZZZwwwZZZ",
//   "amount": "550000.00",
//   "payment_details": "test info",
// }, {
//   "db_client_id": "ZZZwwwZZZ",
//   "amount": "65000.00",
//   "payment_details": "test info",
// }, {
//   "db_client_id": "ZZZwwwZZZ",
//   "amount": "250100.00",
//   "payment_details": "test info",
// }]
//

var arr = new DevExpress.data.DataSource()
  arr = 'api/'

$(function(){
    $("#gridContainer").dxDataGrid({
        dataSource: '/static/json/arr.json',
        columns: [{
                    dataField: "db_client_id",
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
        // filterRow: {
        //     visible: true
        // },
        // headerFilter: {
        //     visible: true
        // },
        // groupPanel: {
        //     visible: true
        // },
        // scrolling: {
        //     mode: "virtual"
        // },
        // height: 600,
        showBorders: true,
        editing: {
            allowAdding: true,
            allowUpdating: true,
            allowDeleting: true
        },
        // grouping: {
        //     autoExpandAll: false
        // },
        // summary: {
        //     totalItems: [{
        //         column: "amount",
        //         summaryType: "sum"
        //     }],
        //     groupItems: [{
        //             column: "amount",
        //             summaryType: "sum"
        //         }, {
        //             summaryType: "count"
        //         }
        //     ]
        // }
    });
});
