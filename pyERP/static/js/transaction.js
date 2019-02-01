$(function(){

  var dictionary = {
    'en': {
      'db_client_id': 'Dt Client',
      'cr_client_id': 'Ct Client',
      'amount': 'Amount',
      'currency_id': 'Currency',
      'amount_e': 'Equivalent',
      'payment_details': 'Details'
    },
    'de': {
      'db_client_id': 'Dt Client',
      'cr_client_id': 'Ct Client',
      'amount': 'Betrag',
      'currency_id': 'Währung',
      'amount_e': 'gleichwertig',
      'payment_details': 'Zahlungszweck'
    },
    'ru': {
      'db_client_id': 'Клиент Дт',
      'cr_client_id': 'Клиент Кт',
      'amount': 'Сумма',
      'currency_id': 'Валюта',
      'amount_e': 'Эквивалент',
      'payment_details': 'Примечание'
    },
    'ua': {
      'db_client_id': 'Клієнт Дт',
      'cr_client_id': 'Клієнт Кт',
      'amount': 'Сума',
      'currency_id': 'Валюта',
      'amount_e': 'Еквивалент',
      'payment_details': 'Призначення'
    }
  };

  DevExpress.localization.loadMessages(dictionary);

  var formatMessage = DevExpress.localization.formatMessage;

  var transaction = new DevExpress.data.DataSource()
  transaction = 'api/'

  var client = {
    store: new DevExpress.data.CustomStore({
      key: "id",
      loadMode: "raw",
      load: function() {
      return $.getJSON('../client/api/');
      }
    }),
    sort: "name"
  }

 var currency = {
     store: new DevExpress.data.CustomStore({
         key: "id",
         loadMode: "raw",
         load: function() {
             return $.getJSON('../currency/api/');
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
          autoExpandAll: false,
          expandMode: 'rowClick',
          contextMenuEnabled: true,
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
  // refresh();
  //   $('.dx-datagrid-summary-item');
});
    // $('#Column Amount').attr("style", "text-align: left; color: red");
