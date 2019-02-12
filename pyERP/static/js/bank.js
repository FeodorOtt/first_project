$(function(){

    var json_url = '../api/bank/'

    var bank = new DevExpress.data.CustomStore({
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

 var country = {
     store: new DevExpress.data.CustomStore({
         key: "id",
         loadMode: "raw",
         load: function() {
             var d = $.Deferred();
             $.getJSON('../api/country/').done(function(result) {
                      return d.resolve(result["objects"]);
                    });
             return d.promise();
         }
     }),
     sort: "name"
 }

  var user_ = {
      store: new DevExpress.data.CustomStore({
              key: "id",
              loadMode: "raw",
              load: function() {
                  var d = $.Deferred();
                  $.getJSON('../api/user/').done(function(result) {
                      return d.resolve(result["objects"]);
                  });
                  return d.promise();
              }
          }),
      sort: "name"
}
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
                  caption: formatMessage("text")
                }, {
                  dataField: "country_id",
                  caption: formatMessage("country"),
                  lookup: {
                    dataSource: country,
                    displayExpr: "name",
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
