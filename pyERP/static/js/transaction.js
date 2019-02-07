$(function(){

    var json_url = '../api/transaction/'

    var transaction = {
        store: new DevExpress.data.CustomStore({
            key: "id",
            // loadMode: "raw",
            load: function (loadOptions) {
                var d = $.Deferred();
                $.getJSON(json_url).done(function (result) {
                        d.resolve(result["objects"])
                        console.log(result["objects"][0]);
                    }
                );
                return d.promise();
            },

            byKey: function (key) {
                return $.getJSON(json_url + encodeURIComponent(key) + '/');
            },

            insert: function (values) {
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

            update: function (key, values) {
                var d = $.Deferred()
                $.ajax({
                    url: json_url + encodeURIComponent(key) + '/',
                    method: "PUT",
                    contentType: 'application/json',
                    data: JSON.stringify(values)
                });
                return d.promise();
            },

            remove: function (key) {
                var d = $.Deferred()
                $.ajax({
                    url: json_url + encodeURIComponent(key) + '/',
                    method: "DELETE",
                }).done(function () {
                    d.resolve(key)
                });
                return d.promise();
            }

        })
    }

  var client = {
      store: new DevExpress.data.CustomStore({
              key: "id",
              loadMode: "raw",
              load: function() {
                  var d = $.Deferred();
                  $.getJSON('../api/client/').done(function(result) {
                      return d.resolve(result["objects"]);
                  });
                  return d.promise();
              }
          }),
      sort: "name"
}

 var currency = {
     store: new DevExpress.data.CustomStore({
         key: "id",
         loadMode: "raw",
         load: function() {
             var d = $.Deferred();
             $.getJSON('../api/currency/').done(function(result) {
                      return d.resolve(result["objects"]);
                    });
             return d.promise();
         }
     }),
     sort: "ISO_char"
 }

 $("#gridContainer").dxDataGrid({
      dataSource: transaction,
      export: {
          enabled: true,
          fileName: "Transactions",
          allowExportSelectedData: true
      },
      allowColumnResizing: false,
      cacheEnabled: true,
      // columnResizingMode: "nextColumn",
      columnMinWidth: 50,
      rowAlternationEnabled: true,
      allowColumnReordering: true,
      hoverStateEnabled: true,
      stateStoring: {
          enabled: true,
          type: "localStorage",
          storageKey: "transaction"
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
                  dataField: "db_client_id",
                  caption: formatMessage("db_client_id"),
                  width: 125,
                  lookup: {
                    dataSource: client,
                    displayExpr: "name",
                    valueExpr: "id"
                  }
                },
                {
                  dataField: "cr_client_id",
                  caption: formatMessage("cr_client_id"),
                  width: 125,
                  lookup: {
                      dataSource: client,
                      displayExpr: "name",
                      valueExpr: "id"
                    }
                  },
                {
                  dataField: "amount",
                  caption: formatMessage("amount"),
                  alignment: 'right',
                  dataType: "number",
                  format: "#,##0.00"
                },
                {
                  dataField: "currency_id",
                  caption: formatMessage("currency_id"),
                  lookup: {
                    dataSource: currency,
                    displayExpr: "ISO_char",
                    valueExpr: "id"
                  }
                },
                {
                  dataField: "amount_e",
                  caption: formatMessage("amount_e"),
                  alignment: 'right',
                  dataType: "number",
                  format: "#,##0.00"
                },
                {
                  dataField: "payment_details",
                  caption: formatMessage("payment_details"),
                }
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
      // height: 600,
      showBorders: true,
      selection: {
          mode: "multiple",
          allowSelectAll: true
      },
      groupPanel: {
          visible: true,
      },
      grouping: {
          autoExpandAll: true,
          expandMode: 'rowClick',
          contextMenuEnabled: true,
      },
      // onContentReady: function() {
      //       var ColName = formatMessage("dxDataGrid-ariaColumn") + ' ' + formatMessage("amount");
      //       var ci = $("[aria-label='" + ColName + "']").attr("aria-colindex");
      //       var cid = $("[aria-label='" + ColName + "']").attr("id");
      //
      //       $('[aria-colindex='+ci+'] .dx-datagrid-summary-item').css("color", "#c56363");
      //       $('[aria-describedby='+cid+']').css("color", "#c56363");
      //
      //       ColName = formatMessage("dxDataGrid-ariaColumn") + ' ' + formatMessage("amount_e");
      //       ci = $("[aria-label='" + ColName + "']").attr("aria-colindex");
      //       cid = $("[aria-label='" + ColName + "']").attr("id");
      //
      //       $('[aria-colindex='+ci+'] .dx-datagrid-summary-item').css("color", "rgb(53, 62, 183)");
      //       $('[aria-describedby='+cid+']').css("color", "rgb(53, 62, 183)");
      //
      //       // $('.dx-datagrid-rowsview .dx-row.dx-group-row').css({
      //       //     'background-color': '#e7f4ff'
      //       // });
      //
      //   },
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
                  // displayFormat: "Всего: {0}"
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
                  alignByColumn: true,
                  // customizeText: function(cellInfo) {
                  //     $(cellInfo).css('background-color','red')
                  //     return cellInfo.value
                  // }
                },
               {
                  column: "payment_details",
                  summaryType: "count",
                  // displayFormat: "Всего: {0}",
                  alignByColumn: true
              }
          ]
      }
  });
});

