$(function(){

    var json_url = '../api/client/'

    var client = new DevExpress.data.CustomStore({
        key: "id",
        // loadMode: "raw",
        load: function() {
            var d = $.Deferred();
            $.getJSON(json_url).done(function(result) {
                        d.resolve(result["objects"]);
                        // console.log(result["objects"][0])
                    }
            );
            return d.promise();
        },

        byKey: function(key) {
            return $.getJSON(json_url + encodeURIComponent(key) + '/');
        },

        insert: function(values) {
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

        update: function(key, values) {
            var d = $.Deferred()
            $.ajax({
                url: json_url + encodeURIComponent(key) + '/',
                method: "PUT",
                contentType: 'application/json',
                data: JSON.stringify(values)
            }).done(function () {
                      d.resolve(key)
                    });;
            return d.promise();
        },

        remove: function(key) {
            var d = $.Deferred()
            $.ajax({
                url: json_url + encodeURIComponent(key) + '/',
                method: "DELETE",
            }).done(function () {
                      d.resolve(key)
                    });
            return d.promise();
        }

    });

  var client_lu = {
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
     sort: "ISO_char"
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

  var transaction = {
     store: new DevExpress.data.CustomStore({
         key: "id",
         loadMode: "raw",
         load: function() {
             var d = $.Deferred();
             $.getJSON('../api/transaction/').done(function(result) {
                      return d.resolve(result["objects"]);
                    });
             return d.promise();
         }
     }),
     sort: "ISO_char",
     // filter: ["db_client_id", "=", currentClientData.id]

 }

$("#gridContainer").dxDataGrid({
        dataSource: {
            store: client
        },
      // keyExpr: "id",
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
                  // dataField: "id",
                // }, {
                  dataField: "name",
                  caption: formatMessage("name"),
//                  cssClass: 'ClientName',
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
                    valueExpr: "resource_uri"
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
                              dataSource: client,
                              displayExpr: "name",
                              valueExpr: "resource_uri"
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
                            valueExpr: "resource_uri"
                          }
                        },
                        {
                          dataField: "payment_details",
                          caption: formatMessage("payment_details"),
                        },
                        ],
                        dataSource: {
                             store: new DevExpress.data.CustomStore({
                                 key: "db_client_id",
                                 loadMode: "raw",
                                 load: function() {
                                          var d = $.Deferred();
                                          $.getJSON('../api/transaction/').done(function(result) {
                                                      d.resolve(result["objects"]);
                                                      // console.log(result["objects"][0])
                                                  }
                                          );
                                          return d.promise();
                                       }
                             }),
                             filter: ["db_client_id", "=", currentClientData.resource_uri]
                        }
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
