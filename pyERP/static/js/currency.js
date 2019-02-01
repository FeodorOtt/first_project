$(function(){

  var dictionary = {
    'en': {
      'name': 'Name',
      'short_name': 'Short Name',
      'ISO_digit': 'ISO digit',
      'ISO_char': 'ISO char',
      'status_id': 'Status'
    },
    'de': {
      'name': 'Name',
      'short_name': 'Kurzname',
      'ISO_digit': 'ISO Digit',
      'ISO_char': 'ISO Zeichen',
      'status_id': 'Status'
    },
    'ru': {
      'name': 'Название',
      'short_name': 'Короткое',
      'ISO_digit': 'ISO цифр.',
      'ISO_char': 'ISO симв.',
      'status_id': 'Статус'
    },
    'ua': {
      'name': 'Назва',
      'short_name': 'Коротка',
      'ISO_digit': 'ISO цифр.',
      'ISO_char': 'ISO симв.',
      'status_id': 'Статус'
    }
  };

  DevExpress.localization.loadMessages(dictionary);

  var formatMessage = DevExpress.localization.formatMessage;

  var currency = new DevExpress.data.DataSource()
  currency = 'api/'

$("#gridContainer").dxDataGrid({
      dataSource: currency,
      export: {
          enabled: true,
          fileName: "Currency",
          allowExportSelectedData: true
      },
      allowColumnResizing: false,
      allowColumnReordering: false,
      cacheEnabled: true,
      columnMinWidth: 50,
      rowAlternationEnabled: true,
      hoverStateEnabled: true,
      stateStoring: {
          enabled: true,
          type: "localStorage",
          storageKey: "currency"
      },
      loadPanel: {
        shading: true,
        height: 120
      },
      columns: [{
                  dataField: "name",
                  caption: formatMessage("name"),
                  width: '45%'
                }, {
                  dataField: "short_name",
                  caption: formatMessage("short_name"),
                  width: '25%'
                }, {
                  dataField: "ISO_digit",
                  caption: formatMessage("ISO_digit"),
                  width: '15%'
                }, {
                  dataField: "ISO_char",
                  caption: formatMessage("ISO_char"),
                  width: '15%'
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
          mode: "virtual"
      },
      showBorders: true,
      selection: {
          mode: "single"
      }
  });
  // refresh();
});
