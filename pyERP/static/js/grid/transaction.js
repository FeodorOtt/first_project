$(function(){
    var initDate = new Date(Date.now());
    var firstDay = new Date(initDate.getFullYear(), initDate.getMonth(), 1);

    var url_search_params = ['&oper_date__gte=' + moment(firstDay).format('YYYY-MM-DD'), '&oper_date__lte=' + moment(Date.now()).format('YYYY-MM-DD')];

    var transaction = json_crud('../api/transaction/', url_search_params);

    var user_ = json_read('../api/user/');
    var client = json_read('../api/client/');
    var partition = json_read('../api/partition/');
    var currency = json_read('../api/currency/', 'ISO_char');

    $("#gridContainer").dxDataGrid({
      dataSource: {
          store: transaction
      },
      export: {
          enabled: true,
          fileName: "Transactions",
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
                  dataField: "id",
                  editorOptions: {
                      disabled: true
                  },
                  caption: formatMessage("transaction_id"),
//                  cssClass: 'TransactionColumnsStyle',
                  width: 100
                }, {
                  dataField: "parent_id",
                  caption: formatMessage("parent_id"),
                  width: 100
                }, {
                  dataField: "pattern_id",
                  caption: formatMessage("pattern_id"),
                  width: 100
                }, {
                  dataField: "oper_date",
                  dataType: "date",
                  caption: formatMessage("oper_date")
                }, {
                  dataField: "currency_rate",
                  caption: formatMessage("currency_rate"),
                  alignment: 'right',
                  dataType: "number",
                  format: "#,##0.00#"
                }, {
                  dataField: "db_client_id",
                  caption: formatMessage("db_client_id"),
                  width: 125,
                  lookup: {
                    dataSource: client,
                    displayExpr: "name",
                    valueExpr: "resource_uri"
                  }
                }, {
                  dataField: "db_account_id",
                  caption: formatMessage("db_account_id"),
                  width: 125,
                  // lookup: {
                  //   dataSource: client,
                  //   displayExpr: "name",
                  //   valueExpr: "resource_uri"
                  // }
                }, {
                  dataField: "cr_client_id",
                  caption: formatMessage("cr_client_id"),
                  width: 125,
                  lookup: {
                      dataSource: client,
                      displayExpr: "name",
                      valueExpr: "resource_uri"
                    }
                }, {
                  dataField: "cr_account_id",
                  caption: formatMessage("cr_account_id"),
                  width: 125,
                  // lookup: {
                  //   dataSource: client,
                  //   displayExpr: "name",
                  //   valueExpr: "resource_uri"
                  // }
                }, {
                  dataField: "amount",
                  // cssClass: 'transactionAmount',
                  editorOptions: {
                      // disabled: true,
                      width: "30%"
                  },
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
                  dataField: "exchange_income",
                  caption: formatMessage("exchange_income"),
                  alignment: 'right',
                  dataType: "number",
                  format: "#,##0.00"
                }, {
                  dataField: "exchange_amount",
                  caption: formatMessage("exchange_amount"),
                  alignment: 'right',
                  dataType: "number",
                  format: "#,##0.00"
                }, {
                  dataField: "exchange_currency",
                  caption: formatMessage("exchange_currency_id"),
                  lookup: {
                    dataSource: currency,
                    displayExpr: "ISO_char",
                    valueExpr: "resource_uri"
                  }
                }, {
                  dataField: "exchange_amount_e",
                  caption: formatMessage("exchange_amount_e"),
                  alignment: 'right',
                  dataType: "number",
                  format: "#,##0.00"
                }, {
                  dataField: "partition_id",
                  caption: formatMessage("partition_id"),
                  lookup: {
                    dataSource: partition,
                    displayExpr: "name",
                    valueExpr: "resource_uri"
                  }
                }, {
                  dataField: "bankimport_id",
                  caption: formatMessage("bankimport_id")
                }, {
                  dataField: "payment_details",
                  caption: formatMessage("payment_details"),
                }, {
                  dataField: "addinfo",
                  caption: formatMessage("addinfo"),
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
        onToolbarPreparing: function(e) {
            var dataGrid = e.component;

            e.toolbarOptions.items.unshift({
            //     location: "before",
            //     template: function(){
            //         return $("<div/>")
            //             .addClass("informer")
            //             .append(
            //                $("<h2 />")
            //                  .addClass("count")
            //                  .text(getGroupCount("currency")),
            //                $("<span />")
            //                  .addClass("name")
            //                  .text("Total Count")
            //             );
            //     }
            // }, {
            //     location: "before",
            //     widget: "dxSelectBox",
            //     options: {
            //         width: 200,
            //         items: [{
            //             value: "currency",
            //             text: "Grouping by Currency"
            //         }, {
            //             value: "db_client_id",
            //             text: "Grouping by Db Client"
            //         }],
            //         displayExpr: "text",
            //         valueExpr: "value",
            //         value: "currency",
            //         onValueChanged: function(e) {
            //             dataGrid.clearGrouping();
            //             dataGrid.columnOption(e.value, "groupIndex", 0);
            //             $(".informer .count").text(getGroupCount(e.value));
            //         }
            //     }
            // }, {
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
            }, {
                location: "after",
                widget: "dxDateBox",
                options: {
                    // icon: "refresh",
                    value: firstDay,
                    hint: formatMessage("begin_date"),
                    showClearButton: true,
                    type: 'date',
                    pickerType: 'calendar',
                    onValueChanged: function(e) {
                        // console.log(Date.now());
                        // console.log(firstDay);
                        try{
                            if (!e.value) {
                                url_search_params[0] = '';
                            }
                            else {
                                url_search_params[0] = '&oper_date__gte=' + moment(e.value).format('YYYY-MM-DD');
                            }
                        }
                        catch (e) {
                            url_search_params[0] = '';
                        }
                        finally {
                            dataGrid.refresh();
                            console.log(url_search_params);
                        }
                    }
                }
            }, {
                location: "after",
                widget: "dxDateBox",
                options: {
                    // icon: "refresh",
                    value: Date.now(),
                    hint: formatMessage("end_date"),
                    showClearButton: true,
                    type: 'date',
                    pickerType: 'calendar',
                    // onInitialized: function(e) {
                    //     e.value = Date.now();
                    // },
                    onValueChanged: function(e) {
                        // console.log(Date.now());
                        // console.log(firstDay);
                        try{
                            if (!e.value) {
                                url_search_params[1] = '';
                            }
                            else {
                                url_search_params[1] = '&oper_date__lte=' + moment(e.value).format('YYYY-MM-DD');
                            }
                        }
                        catch (e) {
                            url_search_params[1] = '';
                        }
                        finally {
                            dataGrid.refresh();
                            console.log(url_search_params);
                        }
                    }
                }
            });
        },
      // onContentReady: function(e){
      //     formInstance = e.component;
      // },
      // onShown: function(e){
      //     setTimeout(function(){
      //         e.component.getEditor('amount').focus();
      //       }, 100);
      // },

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
              items: [{
                  dataField: "id",
                // }, {
                //   dataField: "parent_id"
                }, {
                  dataField: "pattern_id"
                }, {
                  dataField: "oper_date",
                  dataType: "date"
                }, {
                  dataField: "currency_rate",
                }, {
                  dataField: "db_client_id",
                }, {
                  dataField: "db_account_id",
                }, {
                  dataField: "cr_client_id",
                }, {
                  dataField: "cr_account_id",
                }, {
                  itemType: "empty",
                }, {
                  itemType: "empty",
                }, {
                  dataField: "amount",
                  cssClass: 'transactionAmount'
                }, {
                  dataField: "currency_id",
                }, {
                  itemType: "empty",
                }, {
                  itemType: "empty",
                }, {
                  dataField: "amount_e",
                }, {
                  dataField: "exchange_income",
                }, {
                  dataField: "exchange_amount",
                }, {
                  dataField: "exchange_currency",
                }, {
                  dataField: "exchange_amount_e",
                }, {
                  dataField: "partition_id",
                }, {
                  dataField: "bankimport_id",
                }, {
                  dataField: "payment_details",
                }, {
                  dataField: "addinfo",
                }, {
                  dataField: "handle_time",
                }, {
                  dataField: "user_id",
                }, {
                  dataField: "status_id",
                }
               ]
          }
      },
      onEditorPreparing: function (e) {
            if (e.dataField == "amount"||e.dataField == "amount_e"||e.dataField == "exchange_amount"||e.dataField == "exchange_amount_e")
            e.editorName = "dxNumberBox";
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
      onContentReady: function() {
            var ColName = formatMessage("dxDataGrid-ariaColumn") + ' ' + formatMessage("amount");
            var ci = $("[aria-label='" + ColName + "']").attr("aria-colindex");
            var cid = $("[aria-label='" + ColName + "']").attr("id");

            // $('[role="columnheader"]').css("font-size", "10px");

            $('[aria-colindex='+ci+'] .dx-datagrid-summary-item').css("color", "#c56363");
            $('[aria-describedby='+cid+']').css("color", "#c56363");

            ColName = formatMessage("dxDataGrid-ariaColumn") + ' ' + formatMessage("amount_e");
            ci = $("[aria-label='" + ColName + "']").attr("aria-colindex");
            cid = $("[aria-label='" + ColName + "']").attr("id");

            $('[aria-colindex='+ci+'] .dx-datagrid-summary-item').css("color", "rgb(53, 62, 183)");
            $('[aria-describedby='+cid+']').css("color", "rgb(53, 62, 183)");

            // $('.dx-datagrid-rowsview .dx-row.dx-group-row').css({
            //     'background-color': '#e7f4ff'
            // });

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
});

