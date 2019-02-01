$(function(){

  var dictionary = {
    'en': {
      'name': 'Name',
      'type': 'Type',
      'is_resident': 'Resident',
      'responsible_client': 'Responsible',
      'cr_client_id': 'Ct Client',
      'amount': 'Amount',
      'currency_id': 'Currency',
      'payment_details': 'Details',
      'transactions_of': 'Transactions of '
    },
    'de': {
      'name': 'Name',
      'type': 'Type',
      'is_resident': 'Resident',
      'responsible_client': 'Responsible',
      'cr_client_id': 'Ct Client',
      'amount': 'Betrag',
      'currency_id': 'Währung',
      'payment_details': 'Zahlungszweck',
      'transactions_of': 'Transaktionen '
    },
    'ru': {
      'name': 'Имя',
      'type': 'Тип',
      'is_resident': 'Резидент',
      'responsible_client': 'Ответственный',
      'cr_client_id': 'Клиент Кт',
      'amount': 'Сумма',
      'currency_id': 'Валюта',
      'payment_details': 'Примечание',
      'transactions_of': 'Транзакции '
    },
    'ua': {
      'name': "Ім'я",
      'type': 'Тип',
      'is_resident': 'Резидент',
      'responsible_client': 'Відповідальний',
      'cr_client_id': 'Клієнт Кт',
      'amount': 'Сума',
      'currency_id': 'Валюта',
      'payment_details': 'Призначення',
      'transactions_of': 'Транзакції '
    }
  };

  DevExpress.localization.loadMessages(dictionary);

  var formatMessage = DevExpress.localization.formatMessage;

  var client = new DevExpress.data.DataSource()
  client = 'api/'

  var client_lu = {
    store: new DevExpress.data.CustomStore({
      key: "id",
      loadMode: "raw",
      load: function() {
      return $.getJSON('api/');
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

 var transaction = {
     store: new DevExpress.data.CustomStore({
         key: "db_client_id",
         loadMode: "raw",
         load: function() {
             return $.getJSON('../transaction/api/');
         }
     }),
     sort: "ISO_char"
 }

$("#gridContainer").dxDataGrid({
      dataSource: client,
      keyExpr: "id",
      export: {
          enabled: true,
          fileName: "Clients",
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
          storageKey: "client"
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
                  dataField: "name",
                  caption: formatMessage("name"),
                  width: 125
                }, {
                  dataField: "type",
                  caption: formatMessage("type")
                }, {
                  dataField: "is_resident",
                  caption: formatMessage("is_resident"),
                }, {
                  dataField: "responsible_client",
                  caption: formatMessage("responsible_client"),
                  lookup: {
                    dataSource: client_lu,
                    displayExpr: "name",
                    valueExpr: "id"
                  }
                }],
        masterDetail: {
            enabled: true,
            template: function(container, options) {
                var currentClientData = options.data;

                $("<div>")
                    .addClass("master-detail-caption")
                    .text(formatMessage("transactions_of") + currentClientData.name + ':')
                    .appendTo(container);

                $("<div>")
                    .dxDataGrid({
                        columnAutoWidth: true,
                        showBorders: true,
                        columns: [
                        {
                          dataField: "cr_client_id",
                          caption: formatMessage("cr_client_id"),
                          width: 125,
                          lookup: {
                              dataSource: client_lu,
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
                          dataField: "payment_details",
                          caption: formatMessage("payment_details"),
                        },
                        ],
                        dataSource: new DevExpress.data.DataSource({
                             store: new DevExpress.data.CustomStore({
                                 key: "db_client_id",
                                 loadMode: "raw",
                                 load: function() {
                                     return $.getJSON('../transaction/api/');
                                 }
                             }),
                             filter: ["db_client_id", "=", currentClientData.id]
                        })
                    }).appendTo(container);
            }
        },
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
