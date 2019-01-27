var arr = new DevExpress.data.DataSource()
arr = 'api/'

$(function(){
    $("#gridContainer").dxDataGrid({
        dataSource: arr,
        // columns: [{
        //             dataField: "db_client_id",
        //           },
        //           {
        //             dataField: "amount",
        //           },
        //           {
        //             dataField: "payment_details",
        //           },
        //          ],
        showBorders: true,
        editing: {
            allowAdding: true,
            allowUpdating: true,
            allowDeleting: true
        },
    });
});
