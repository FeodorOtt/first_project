$(function(){
    // var initDate = new Date(Date.now());
    // var url_search_params = ['&oper_date__gte=' + moment(firstDay).format('YYYY-MM-DD'), '&oper_date__lte=' + moment(Date.now()).format('YYYY-MM-DD')];

    var account = json_crud('../api/account/');

    var balance_account = json_read('../api/balanceaccount/');
    var saldo_type = json_read('../api/accountsaldotype/');
    var acc_type = json_read('../api/accounttypelocale/?locale='+locale);
    var acc_category = json_read('../api/accountcategorylocale/?locale='+locale);
    var client = json_read('../api/client/');
    var bank = json_read('../api/bank/');
    var currency = json_read('../api/currency/', 'ISO_char');
    var user_ = json_read('../api/user/');
    // var partition = json_read('../api/partition/');

    $("#gridContainer").dxDataGrid({
      dataSource: {
          store: account
      },
      export: {
          enabled: true,
          fileName: "Accounts",
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
          storageKey: "account"
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
                //   dataField: "id",
                //   editorOptions: {
                //       disabled: true
                //   },
                // }, {
                  dataField: "number",
                  caption: formatMessage("number"),
                  alignment: 'left',
                  width: 100
                }, {
                  dataField: "client_id",
                  caption: formatMessage("client_id"),
                  width: 125,
                  lookup: {
                    dataSource: client,
                    displayExpr: "name",
                    valueExpr: "resource_uri"
                  }
                }, {
                  dataField: "balance_account_id",
                  caption: formatMessage("balance_account_id"),
                  width: 125,
                  lookup: {
                    dataSource: balance_account,
                    displayExpr: "assignment",
                    valueExpr: "resource_uri"
                  }
                }, {
                  dataField: "index",
                  caption: formatMessage("index")
                }, {
                  dataField: "saldo_type_id",
                  caption: formatMessage("saldo_type_id"),
                  width: 125,
                  lookup: {
                    dataSource: saldo_type,
                    displayExpr: "short_name",
                    valueExpr: "resource_uri"
                  }
                }, {
                  dataField: "type_id",
                  caption: formatMessage("type"),
                  width: 125,
                  lookup: {
                    dataSource: acc_type,
                    displayExpr: "name",
                    valueExpr: "account_type_id"
                  }
                }, {
                  dataField: "category_id",
                  caption: formatMessage("category"),
                  width: 125,
                  lookup: {
                    dataSource: acc_category,
                    displayExpr: "name",
                    valueExpr: "account_category_id"
                  }
                }, {
                  dataField: "bank_id",
                  caption: formatMessage("bank_id"),
                  width: 125,
                  lookup: {
                    dataSource: bank,
                    displayExpr: "name",
                    valueExpr: "resource_uri"
                  }
                }, {
                  dataField: "assignment",
                  caption: formatMessage("assignment"),
                }, {
                  dataField: "begin_date",
                  dataType: "date",
                  caption: formatMessage("begin_date")
                }, {
                  dataField: "end_date",
                  dataType: "date",
                  caption: formatMessage("end_date")
                }, {
                  dataField: "parent_client_id",
                  caption: formatMessage("parent_client_id"),
                  width: 125,
                  lookup: {
                    dataSource: client,
                    displayExpr: "name",
                    valueExpr: "resource_uri"
                  }
                }, {
                  dataField: "sync_partition_flag",
                  caption: formatMessage("sync_partition_flag"),
                }, {
                  dataField: "handle_time",
                  editorOptions: {
                      disabled: true
                  },
                  dataType: "datetime",
                  caption: formatMessage("handle_time"),
                  width: 50,
                }, {
                  dataField: "user_id",
                  editorOptions: {
                      disabled: true
                  },
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
                          "name": formatMessage("opened")
                      }, {
                          "id": 2,
                          "name": formatMessage("active")
                      }, {
                          "id": 3,
                          "name": formatMessage("closed")
                      }],
                    displayExpr: "name",
                    valueExpr: "id"
                  }
        }],
        masterDetail: {
            enabled: true,
            // showBorders: true,
            template: function(container, options) {
                var currentAccData = options.data;

                $("<div>")
                    .addClass("master-detail-caption")
                     .text(formatMessage("account_mov") + currentAccData.number + ':')
                    .appendTo(container);

                $("<div>")
                    .dxDataGrid({
                        columnAutoWidth: true,
                        showBorders: true,
                        columns: [{
                          dataField: "id",
                        }, {
                          dataField: "transaction_id",
                          visible: false,
                          caption: formatMessage("transaction_id"),
                        }, {
                          dataField: "order_id",
                          caption: formatMessage("order_id"),
                        }, {
                          dataField: "partition_id",
                          caption: formatMessage("partition_id"),
                        }, {
                          dataField: "db_client_id",
                          caption: formatMessage("db_client_id"),
                          lookup: {
                            dataSource: client,
                            displayExpr: "name",
                            valueExpr: "resource_uri"
                          }
                        }, {
                          dataField: "db_account_id",
                          caption: formatMessage("db_account_id"),
                          // lookup: {
                          //   dataSource: client,
                          //   displayExpr: "name",
                          //   valueExpr: "resource_uri"
                          // }
                        }, {
                          dataField: "cr_client_id",
                          caption: formatMessage("cr_client_id"),
                          lookup: {
                              dataSource: client,
                              displayExpr: "name",
                              valueExpr: "resource_uri"
                            }
                        }, {
                          dataField: "cr_account_id",
                          caption: formatMessage("cr_account_id"),
                          // lookup: {
                          //   dataSource: client,
                          //   displayExpr: "name",
                          //   valueExpr: "resource_uri"
                          // }
                        }, {
                          dataField: "amount",
                          caption: formatMessage("amount"),
                          alignment: 'right',
                          dataType: "number",
                          format: "#,##0.00"
                        }, {
                          dataField: "currency_id",
                          caption: formatMessage("currency_id"),
                          lookup: {
                            dataSource: currency,
                            displayExpr: "ISO_char",
                            valueExpr: "resource_uri"
                          }
                        }, {
                          dataField: "amount_e",
                          caption: formatMessage("amount_e"),
                          alignment: 'right',
                          dataType: "number",
                          format: "#,##0.00"
                        }, {
                          dataField: "handle_time",
                          editorOptions: {
                              disabled: true
                          },
                          dataType: "datetime",
                          caption: formatMessage("handle_time"),
                          // re
                        }, {
                          dataField: "user_id",
                          editorOptions: {
                              disabled: true
                          },
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
                                  "name": formatMessage("posted")
                              }, {
                                  "id": 2,
                                  "name": formatMessage("postponed")
                              }, {
                                  "id": 3,
                                  "name": formatMessage("reversed")
                              }],
                            displayExpr: "name",
                            valueExpr: "id"
                          }
                        }],
                        dataSource: {
                             store: new DevExpress.data.CustomStore({
                                 key: "id",
                                 loadMode: "raw",
                                 load: function() {
                                          var d = $.Deferred();
                                          $.getJSON('../api/transactiondetail/?db_account_id=' + currentTransData.id).done(function(result) {
                                                      d.resolve(result["objects"]);
                                                      // console.log(result["objects"][0])
                                                  }
                                          );
                                          return d.promise();
                                       }
                             }),
                             filter: ["resource_uri", "=", currentTransData.transaction_id]
                        }
                    }).appendTo(container);
            }
        },
        onToolbarPreparing: function(e) {
            var dataGrid = e.component;

            e.toolbarOptions.items.unshift({
                location: "before",
                widget: "dxButton",
                options: {
                    text: formatMessage("collapse_all"),
                    width: 100,
                    onClick: function(e) {
                        var expanding = e.component.option("text") === formatMessage("expand_all");
                        dataGrid.option("grouping.autoExpandAll", expanding);
                        e.component.option("text", expanding ? formatMessage("collapse_all") : formatMessage("expand_all"));
                    }
                }
            }, {
                location: "after",
                widget: "dxButton",
                options: {
                    icon: "refresh",
                    hint: formatMessage("refresh"),
                    onClick: function() {
                        dataGrid.refresh();
                    }
                }
            });
        },
      editing: {
          allowAdding: true,
          allowUpdating: true,
          allowDeleting: true,
          useIcons: true,
          mode: "popup",
          // activeStateEnabled: true,
          form: {
              minColWidth: 50,
              colCount: 2,
              focusStateEnabled: true,
              showTitle: true,
              onShowing: function(e){
                  e.component.option("title", "Тип транзакции: -----");
              },
              // items: [{
              //   dataField: "number",
              // }, {
              //   dataField: "client_id",
              // }, {
              //   dataField: "balance_account_id",
              // }, {
              //   dataField: "index",
              // }, {
              //   dataField: "saldo_type_id",
              // }, {
              //   dataField: "type_id",
              // }, {
              //   dataField: "category_id",
              // }, {
              //   dataField: "bank_id",
              // }, {
              //   dataField: "assignment",
              // }, {
              //   dataField: "begin_date",
              // }, {
              //   dataField: "end_date",
              // }, {
              //   dataField: "parent_client_id",
              // }, {
              //   dataField: "sync_partition_flag",
              // }, {
              //   dataField: "handle_time",
              // }, {
              //   dataField: "user_id",
              // }, {
              //   dataField: "status_id",
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
      groupPanel: {
          visible: true,
      },
      grouping: {
          allowCollapsing: true,
          autoExpandAll: true,
          expandMode: 'rowClick',
          contextMenuEnabled: true,
      },
        // onRowInserted: function(e) {
        //   selectRowsByIndexes([1]);
        //   console.log(e.component);
        // },
      summary: {
          totalItems: [],
          groupItems: []
      }
    });
});
