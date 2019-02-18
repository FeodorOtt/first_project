$(function(){
    var bank = json_crud('../api/bank/');
    var country = json_read('../api/country/');
    var user_ = json_read('../api/user/');

$("#gridContainer").dxDataGrid({
        dataSource: {
            store: bank
        },
      // keyExpr: "id",
      export: {
          enabled: true,
          fileName: "Banks",
          allowExportSelectedData: true
      },
      allowColumnResizing: true,
      cacheEnabled: true,
      // columnResizingMode: "nextColumn",
      columnMinWidth: 50,
      rowAlternationEnabled: true,
      allowColumnReordering: true,
      hoverStateEnabled: true,
      stateStoring: {
          enabled: true,
          type: "localStorage",
          storageKey: "bank"
      },
      loadPanel: {
        shading: true,
        height: 120
      },
      columnChooser: {
          enabled: true,
          mode: "select"
      },
      columns: [{
                  // dataField: "id",
                // }, {
                  dataField: "name",
                  caption: formatMessage("name"),
//                  cssClass: 'ClientName',
                  width: 125
                }, {
                  dataField: "text_id",
                  caption: formatMessage("text_id")
                }, {
                  dataField: "country_id",
                  showClearButton: true,
                  caption: formatMessage("country"),
                  lookup: {
                    dataSource: country,
                    displayExpr: formatMessage("country_lu_field"),
                    valueExpr: "resource_uri"
                  }
                }, {
                  dataField: "contact_data",
                  caption: formatMessage("contact_data"),
                }, {
                  dataField: "handle_time",
                  dataType: "datetime",
                  caption: formatMessage("handle_time"),
                  width: 50,
                }, {
                  dataField: "user_id",
                  caption: formatMessage("user_id"),
                  lookup: {
                    dataSource: user_,
                    displayExpr: "username",
                    valueExpr: "resource_uri"
                  }
                }],
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
          showScrollbar: "never"
      //     scrollByThumb: true,
      //      mode: "infinite"
      //     useNative: false
      },
      paging: {
          enabled: false
          // pageSize: 5
      },
      // pager: {
      //     showPageSizeSelector: true,
      //     allowedPageSizes: [5, 10, 20],
      //     showInfo: true,
      //     showNavigationButtons: true
      // },
      width: 1200,
      height: 600,
      showBorders: true,
      selection: {
          mode: "multiple",
          allowSelectAll: true
      },
      // groupPanel: {
      //     visible: false,
      // },
      // grouping: {
          // autoExpandAll: false,
      //     expandMode: 'rowClick',
      //     contextMenuEnabled: true,
      // },
  });
  // refresh();
});
