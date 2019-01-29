$(function(){

  var dictionary = {
    'en': {
      'name': 'Name',
      'type': 'Type',
      'is_resident': 'Resident',
      'responsible_client': 'Responsible'
    },
    'de': {
      'name': 'Name',
      'type': 'Type',
      'is_resident': 'Resident',
      'responsible_client': 'Responsible'
    },
    'ru': {
      'name': 'Имя',
      'type': 'Тип',
      'is_resident': 'Резидент',
      'responsible_client': 'Ответственный'
    },
    'ua': {
      'name': "Ім'я",
      'type': 'Тип',
      'is_resident': 'Резидент',
      'responsible_client': 'Відповідальний'
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

$("#gridContainer").dxDataGrid({
      dataSource: client,
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
      groupPanel: {
          visible: false,
      },
      scrolling: {
          mode: "virtual"
      },
      showBorders: true,
      selection: {
          mode: "multiple",
          allowSelectAll: true
      },
      // grouping: {
          // autoExpandAll: false,
      //     expandMode: 'rowClick',
      //     contextMenuEnabled: true,
      // },
  });
});
