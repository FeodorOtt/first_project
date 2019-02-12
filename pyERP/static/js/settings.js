///////////////////////////////////////////////Language Switch/////////////////////////////////////////////////////////////////////////
var locales = [
    { name: "English", value: "en" },
    { name: "Deutsch", value: "de" },
    { name: "Русский", value: "ru" },
    { name: "Українська", value: "ua" }
];
var locale = getLocale();
DevExpress.localization.locale(locale);

// DevExpress.config(
//   {
//     decimalSeparator: '.',
//     thousandsSeparator: ',',
//     forceIsoDateParsing: true
//   });



var selectLangBoxOptions = {
    inputAttr: { id: "selectLangInput" },
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
    var locale = localStorage.getItem("locale");
    return locale != null ? locale : "ru";
}

function setLocale(locale) {
    localStorage.setItem("locale", locale);
}

$("#selectLangBox").dxSelectBox(selectLangBoxOptions);

/////////////////////////////////////////////////Theme Switch///////////////////////////////////////////////////////////////////////
var themes = [
    { name: "Greenmist", value: "generic.greenmist" },
    { name: "Greenmist compact", value: "generic.greenmist.compact" },
    { name: "Light", value: "generic.light" },
    { name: "Light compact", value: "generic.light.compact" },
    // { name: "Dark", value: "generic.dark" },
    { name: "Dark compact", value: "generic.dark.compact" },
    // { name: "Carmine", value: "generic.carmine" },
    { name: "Carmine compact", value: "generic.carmine.compact" },
    // { name: "Softblue", value: "generic.softblue" },
    // { name: "Softblue compact", value: "generic.softblue.compact" },
    // { name: "Darkmoon", value: "generic.darkmoon" },
    { name: "Darkmoon compact", value: "generic.darkmoon.compact" },
    // { name: "Darkviolet", value: "generic.darkviolet" },
    { name: "Darkviolet compact", value: "generic.darkviolet.compact" },
    // { name: "Contrast", value: "generic.contrast" },
    { name: "Contrast compact", value: "generic.contrast.compact" },

    // { name: "Blue light", value: "material.blue.light" },
    // { name: "Blue dark", value: "material.blue.dark" },
    // { name: "Lime light", value: "material.lime.light" },
    // { name: "Lime dark", value: "material.lime.dark" },
    // { name: "Orange light", value: "material.orange.light" },
    // { name: "Orange dark", value: "material.orange.dark" },
    // { name: "Purple light", value: "material.purple.light" },
    // { name: "Purple dark", value: "material.purple.dark" },
    // { name: "Teal", value: "material.teal.light" },
    // { name: "Teal dark", value: "material.teal.dark" },
];
var theme = getTheme();
DevExpress.ui.themes.current(theme);

var selectThemeBoxOptions = {
    inputAttr: { id: "selectThemeInput" },
    dataSource: themes,
    displayExpr: "name",
    valueExpr: "value",
    value: theme,
    onValueChanged: changeTheme
};

function changeTheme(data) {
    setTheme(data.value);
    window.location.reload();
}

function getTheme() {
    var theme = window.localStorage.getItem("dx-theme") || "generic.greenmist.compact";
    return theme;
}

function setTheme(theme) {
    window.localStorage.setItem("dx-theme", theme);
}

$("#selectThemeBox").dxSelectBox(selectThemeBoxOptions);

