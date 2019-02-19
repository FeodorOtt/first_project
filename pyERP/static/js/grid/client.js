$(function(){
  var client = json_crud('../api/client/');

  var client_lu = json_read('../api/client/');
  var clienttype = json_read('../api/clienttypelocale/?locale='+locale);
  var clientcategory = json_read('../api/clientcategorylocale/?locale='+locale);
  var currency = json_read('../api/currency/', 'ISO_char');
  var user_ = json_read('../api/user/');

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
                  dataField: "responsible_client",
                  caption: formatMessage("responsible_client"),
                  lookup: {
                    dataSource: client_lu,
                    displayExpr: "name",
                    valueExpr: "resource_uri"
                  }
                }, {
                  dataField: "text_id",
                  caption: formatMessage("client_text_id")
                }, {
                  dataField: "type_id",
                  caption: formatMessage("type"),
                  lookup: {
                    dataSource: clienttype,
                    displayExpr: "name",
                    valueExpr: "client_type_id"
                  }
                }, {
                  dataField: "category_id",
                  caption: formatMessage("category"),
                  lookup: {
                    dataSource: clientcategory,
                    displayExpr: "name",
                    valueExpr: "client_category_id"
                  }
                }, {
                  dataField: "is_resident",
                  caption: formatMessage("is_resident"),
                }, {
                  dataField: "document",
                  caption: formatMessage("document"),
                  lookup: {
                      dataSource: [{
                          "id": 1,
                          "name": formatMessage("passport")
                      }, {
                          "id": 2,
                          "name": formatMessage("driver_license")
                      }],
                    displayExpr: "name",
                    valueExpr: "id"
                  }
                }, {
                  dataField: "document_data",
                  caption: formatMessage("document_data"),
                }, {
                  dataField: "contact_data",
                  caption: formatMessage("contact_data"),
                }, {
                  dataField: "add_info",
                  caption: formatMessage("addinfo"),
                }, {
                  dataField: "attracted_by",
                  caption: formatMessage("attracted_by"),
                  lookup: {
                      dataSource: client_lu,
                      displayExpr: "name",
                      valueExpr: "resource_uri"
                  }
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
                }, {
                  dataField: "status_id",
                  caption: formatMessage("status_id"),
                  lookup: {
                      dataSource: [{
                          "id": 1,
                          "name": formatMessage("active")
                      }, {
                          "id": 2,
                          "name": formatMessage("closed")
                      }, {
                          "id": 3,
                          "name": formatMessage("blocked")
                      }],
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
          useIcons: true,
          mode: "form",
          form: {
              minColWidth: 50,
              colCount: 2,
              showTitle: true,
              // title: 'QWERTY',
              focusStateEnabled: true,
              items: [{
                  itemType: "group",
                  caption: formatMessage("personal_data"),
                  items: [{
                    dataField: "name",
                    cssClass: 'ClientName'
                  }, {
                    dataField: "text_id"
                  }, {
                    dataField: "document"
                  }, {
                    dataField: "document_data",
                    editorOptions: {
                        height: 75
                    }
                  }, {
                    dataField: "contact_data",
                    editorOptions: {
                        height: 75
                    }
                  }, {
                    dataField: "add_info",
                    editorOptions: {
                        height: 75
                    }
                  }]
              }, {
              itemType: "group",
                  caption: formatMessage("options"),
                  items: [{
                        dataField: "type_id"
                      }, {
                        dataField: "category_id"
                      }, {
                        dataField: "responsible_client"
                      }, {
                        dataField: "is_resident"
                        // defaultvalue: true
                      }, {
                        dataField: "attracted_by"
                      }, {
                        dataField: "handle_time",
                        dataType: "datetime",
                        disabled: true,
                        // width: 50
                      }, {
                        dataField: "user_id",
                        disabled: true,
                        readOnly: true
                      }, {
                        dataField: "status_id",
                      }
                  ]
              }]
          }
      },
      onEditorPreparing: function (e) {
            if (e.dataField == "document_data"||e.dataField == "contact_data"||e.dataField == "add_info")
            e.editorName = "dxTextArea";
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
