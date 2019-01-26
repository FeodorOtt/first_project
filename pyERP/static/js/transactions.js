$(function(){
    $("#gridContainer").dxDataGrid({
        dataSource: '/static/json/arr.json',
        columns: [{
                    dataField: "db_client_id",
                  },
                  {
                    dataField: "amount",
                  },
                  {
                    dataField: "payment_details",
                  },
                 ],
        showBorders: true,
        editing: {
            allowAdding: true,
            allowUpdating: true,
            allowDeleting: true
        },
    });
});
