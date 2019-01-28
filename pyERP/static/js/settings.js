DevExpress.config(
  {
    decimalSeparator: ',',
    thousandsSeparator: ' '
  }
);

var locales = [
    { name: "English", value: "en", lang: "Language" },
    { name: "Deutsch", value: "de", lang: "Language" },
    { name: "Русский", value: "ru", lang: "Язык" },
    { name: "Українська", value: "ua", lang: "Мова" }
];
var locale = getLocale();
DevExpress.localization.locale(locale);

var selectBoxOptions = {
    inputAttr: { id: "selectInput" },
    dataSource: locales,
    displayExpr: "name",
    valueExpr: "value",
    value: locale,
    onValueChanged: changeLocale
};

function changeLocale(data) {
    setLocale(data.value);
    document.location.reload();
}

function getLocale() {
    var locale = sessionStorage.getItem("locale");
    return locale != null ? locale : "en";
}

function setLocale(locale) {
    sessionStorage.setItem("locale", locale);
}

$("#selectBox").dxSelectBox(selectBoxOptions);
