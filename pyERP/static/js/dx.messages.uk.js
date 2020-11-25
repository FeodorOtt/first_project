/*!
* DevExtreme (dx.messages.uk.js)
* Version: 18.2.5
* Build date: Wed Jan 23 2019
*
* Copyright (c) 2012 - 2019 Developer Express Inc. ALL RIGHTS RESERVED
* Read about DevExtreme licensing here: https://js.devexpress.com/Licensing/
*/
"use strict";

! function(root, factory) {
    if ("function" === typeof define && define.amd) {
        define(function(require) {
            factory(require("devextreme/localization"))
        })
    } else {
        if ("object" === typeof module && module.exports) {
            factory(require("devextreme/localization"))
        } else {
            factory(DevExpress.localization)
        }
    }
}(this, function(localization) {
    localization.loadMessages({
        uk: {
            Yes: "Так",
            No: "Ні",
            Cancel: "Скасувати",
            Clear: "Очистити",
            Done: "Готово",
            Loading: "Завантажую...",
            Select: "Обрати...",
            Search: "Пошук",
            Back: "Назад",
            OK: "OK",
            "dxCollectionWidget-noDataText": "Немає даних для відтворення",
            "validation-required": "Поле має бути заповнено",
            "validation-required-formatted": "Має бути заповнено: {0}",
            "validation-numeric": "Значення має бути числом",
            "validation-numeric-formatted": "Значення поля {0} має бути числом",
            "validation-range": "Значение поля не входит в диапазон",
            "validation-range-formatted": "Значення поля {0} не входить у диапазон",
            "validation-stringLength": "Невірна довжина значення у полі",
            "validation-stringLength-formatted": "Невірна довжина значення у полі {0}",
            "validation-custom": "Неприпустиме значення",
            "validation-custom-formatted": "Неприпустиме значення: {0}",
            "validation-compare": "Значення полів не відповідають один одному",
            "validation-compare-formatted": "Значення поля {0} не відповідає",
            "validation-pattern": "Значення не відповідає шаблону",
            "validation-pattern-formatted": "Значення поля {0} не відповідає шаблону",
            "validation-email": "Неприпустиме значення email",
            "validation-email-formatted": "Неприпустиме значення {0}",
            "validation-mask": "Неприпустиме значення",
            "dxLookup-searchPlaceholder": "Мінімальна кільуість символів: {0}",
            "dxList-pullingDownText": "Підтягніть для оновлення...",
            "dxList-pulledDownText": "Відпустіть для оновлення...",
            "dxList-refreshingText": "Оновлення...",
            "dxList-pageLoadingText": "Завантаження...",
            "dxList-nextButtonText": "Далі",
            "dxList-selectAll": "Обрати всі",
            "dxListEditDecorator-delete": "Видалити",
            "dxListEditDecorator-more": "Ще",
            "dxScrollView-pullingDownText": "Підтягніть для оновлення...",
            "dxScrollView-pulledDownText": "Відпустіть для оновлення...",
            "dxScrollView-refreshingText": "Оновлення...",
            "dxScrollView-reachBottomText": "Завантаження...",
            "dxDateBox-simulatedDataPickerTitleTime": "Оберіть час",
            "dxDateBox-simulatedDataPickerTitleDate": "Оберіть дату",
            "dxDateBox-simulatedDataPickerTitleDateTime": "Оберіть дату та час",
            "dxDateBox-validation-datetime": "Значення має бути датою/часом",
            "dxFileUploader-selectFile": "Оберіть файл",
            "dxFileUploader-dropFile": "або Перетягніть файл сюди",
            "dxFileUploader-bytes": "байт",
            "dxFileUploader-kb": "кБ",
            "dxFileUploader-Mb": "МБ",
            "dxFileUploader-Gb": "ГБ",
            "dxFileUploader-upload": "Завантажити",
            "dxFileUploader-uploaded": "Завантажено",
            "dxFileUploader-readyToUpload": "Готово до завантаження",
            "dxFileUploader-uploadFailedMessage": "Завантаження не вдалося",
            "dxDataGrid-groupContinuedMessage": "Продовження з попередньої сторінки",
            "dxFileUploader-invalidFileExtension": "Неприпустиме розширення файлу",
            "dxFileUploader-invalidMaxFileSize": "Файл занадто великий",
            "dxFileUploader-invalidMinFileSize": "Файл занадто маленький",
            "dxRangeSlider-ariaFrom": "Від",
            "dxRangeSlider-ariaTill": "До",
            "dxSwitch-switchedOnText": "ВВІМК",
            "dxSwitch-switchedOffText": "ВИМК",
            "dxForm-optionalMark": "необов'язковий",
            "dxForm-requiredMessage": " Поле {0} має бути заповнено",
            "dxNumberBox-invalidValueMessage": "Значення має бути числом",
            "dxDataGrid-columnChooserTitle": "Обрання стовпців",
            "dxDataGrid-columnChooserEmptyText": "Перетягніть стовпець сюди, щоб сховати його",
            "dxDataGrid-groupContinuesMessage": "Продовження на наступній страниці",
            "dxDataGrid-groupHeaderText": "Групувати дані за цим стовцем",
            "dxDataGrid-ungroupHeaderText": "Розгрупувати дані за цим стовцем",
            "dxDataGrid-ungroupAllText": "Скинути групування",
            "dxDataGrid-editingEditRow": "Редагувати",
            "dxDataGrid-editingSaveRowChanges": "Зберегти",
            "dxDataGrid-editingCancelRowChanges": "Скасувати",
            "dxDataGrid-editingDeleteRow": "Видалити",
            "dxDataGrid-editingUndeleteRow": "Відновити",
            "dxDataGrid-editingConfirmDeleteMessage": "Вы впевнені, що хочете видалити цей запис?",
            "dxDataGrid-validationCancelChanges": "Скасувати зміни",
            "dxDataGrid-groupPanelEmptyText": "Перетягніть стовпець сюди, щоб згрупувати по ньому",
            "dxDataGrid-noDataText": "Немає даних",
            "dxDataGrid-searchPanelPlaceholder": "Шукати...",
            "dxDataGrid-filterRowShowAllText": "(Всі)",
            "dxDataGrid-filterRowResetOperationText": "Скинути",
            "dxDataGrid-filterRowOperationEquals": "Рівно",
            "dxDataGrid-filterRowOperationNotEquals": "Не рівно",
            "dxDataGrid-filterRowOperationLess": "Менше",
            "dxDataGrid-filterRowOperationLessOrEquals": "Менше або рівно",
            "dxDataGrid-filterRowOperationGreater": "Більше",
            "dxDataGrid-filterRowOperationGreaterOrEquals": "Більше або рівно",
            "dxDataGrid-filterRowOperationStartsWith": "Починаеться на",
            "dxDataGrid-filterRowOperationContains": "Містить",
            "dxDataGrid-filterRowOperationNotContains": "Не містить",
            "dxDataGrid-filterRowOperationEndsWith": "Закінчується на",
            "dxDataGrid-filterRowOperationBetween": "У диапазоні",
            "dxDataGrid-filterRowOperationBetweenStartText": "Початок",
            "dxDataGrid-filterRowOperationBetweenEndText": "Кінець",
            "dxDataGrid-applyFilterText": "Застосувати фільтр",
            "dxDataGrid-trueText": "Так",
            "dxDataGrid-falseText": "Ні",
            "dxDataGrid-sortingAscendingText": "Сортувати за зростанням",
            "dxDataGrid-sortingDescendingText": "Сортувати за спаданням",
            "dxDataGrid-sortingClearText": "Скинути сортування",
            "dxDataGrid-editingSaveAllChanges": "Зберегти зміни",
            "dxDataGrid-editingCancelAllChanges": "Скасувати зміни",
            "dxDataGrid-editingAddRow": "Додати строку",
            "dxDataGrid-summaryMin": "Мін: {0}",
            "dxDataGrid-summaryMinOtherColumn": "Мін по {1} : {0}",
            "dxDataGrid-summaryMax": "Макс: {0}",
            "dxDataGrid-summaryMaxOtherColumn": "Макс по {1} : {0}",
            "dxDataGrid-summaryAvg": "Серзнч: {0}",
            "dxDataGrid-summaryAvgOtherColumn": "Серзнч по {1} : {0}",
            "dxDataGrid-summarySum": "Сум: {0}",
            "dxDataGrid-summarySumOtherColumn": "Сум по {1} : {0}",
            "dxDataGrid-summaryCount": "Загалом: {0}",
            "dxDataGrid-columnFixingFix": "Закріпити",
            "dxDataGrid-columnFixingUnfix": "Откріпити",
            "dxDataGrid-columnFixingLeftPosition": "Ліворуч",
            "dxDataGrid-columnFixingRightPosition": "Праворуч",
            "dxDataGrid-exportTo": "Експортувати",
            "dxDataGrid-exportToExcel": "Експортувати в Excel файл",
            "dxDataGrid-excelFormat": "Excel файл",
            "dxDataGrid-selectedRows": "Обрані строки",
            "dxDataGrid-exportAll": "Экспортувати все",
            "dxDataGrid-exportSelectedRows": "Експортировати обрані строки",
            "dxDataGrid-headerFilterEmptyValue": "(Порожнє)",
            "dxDataGrid-headerFilterOK": "ОК",
            "dxDataGrid-headerFilterCancel": "Скасувати",
            "dxDataGrid-ariaColumn": "Стовпець",
            "dxDataGrid-ariaValue": "Значення",
            "dxDataGrid-ariaFilterCell": "Фільтр",
            "dxDataGrid-ariaCollapse": "Сгорнути",
            "dxDataGrid-ariaExpand": "Разгорнути",
            "dxDataGrid-ariaDataGrid": "Таблиця даних",
            "dxDataGrid-ariaSearchInGrid": "Шукати в таблиці даних",
            "dxDataGrid-ariaSelectAll": "Обрать все",
            "dxDataGrid-ariaSelectRow": "Обрати строку",
            "dxDataGrid-filterBuilderPopupTitle": "Конструктор фільтра",
            "dxDataGrid-filterPanelCreateFilter": "Створити фільтр",
            "dxDataGrid-filterPanelClearFilter": "Очистити",
            "dxDataGrid-filterPanelFilterEnabledHint": "Активувати фільтр",
            "dxTreeList-ariaTreeList": "Ієрархічна таблиця даних",
            "dxTreeList-editingAddRowToNode": "Додати",
            "dxPager-infoText": "Сторінка {0} з {1} (Загалом елементів: {2})",
            "dxPager-pagesCountText": "з",
            "dxPivotGrid-grandTotal": "Разом",
            "dxPivotGrid-total": "{0} Загалом",
            "dxPivotGrid-fieldChooserTitle": "Вибір полів",
            "dxPivotGrid-showFieldChooser": "Показати вибір полів",
            "dxPivotGrid-expandAll": "Розгорнути все",
            "dxPivotGrid-collapseAll": "Згорнути все",
            "dxPivotGrid-sortColumnBySummary": "Сортувати \"{0}\" по цієй колонці",
            "dxPivotGrid-sortRowBySummary": "Сортировать \"{0}\" по цьому рядку",
            "dxPivotGrid-removeAllSorting": "Скинути всі сортування",
            "dxPivotGrid-dataNotAvailable": "Н/Д",
            "dxPivotGrid-rowFields": "Поля рядків",
            "dxPivotGrid-columnFields": "Поля стовпців",
            "dxPivotGrid-dataFields": "Поля даних",
            "dxPivotGrid-filterFields": "Поля фільтрів",
            "dxPivotGrid-allFields": "Усі поля",
            "dxPivotGrid-columnFieldArea": "Перетягніть поля колонок cюди",
            "dxPivotGrid-dataFieldArea": "Перетягніть поля даних cюди",
            "dxPivotGrid-rowFieldArea": "Перетягніть поля рядків cюди",
            "dxPivotGrid-filterFieldArea": "Перетягніть поля фільтрів cюди",
            "dxScheduler-editorLabelTitle": "Назва",
            "dxScheduler-editorLabelStartDate": "Дата початку",
            "dxScheduler-editorLabelEndDate": "Дата завершення",
            "dxScheduler-editorLabelDescription": "Опис",
            "dxScheduler-editorLabelRecurrence": "Повторення",
            "dxScheduler-openAppointment": "Відкрити задачу",
            "dxScheduler-recurrenceNever": "Ніколи",
            "dxScheduler-recurrenceDaily": "Щодня",
            "dxScheduler-recurrenceWeekly": "Щотижня",
            "dxScheduler-recurrenceMonthly": "Щомісяця",
            "dxScheduler-recurrenceYearly": "Щорічно",
            "dxScheduler-recurrenceEvery": "Інтервал",
            "dxScheduler-recurrenceEnd": "Завершити повторення",
            "dxScheduler-recurrenceAfter": "Після",
            "dxScheduler-recurrenceOn": "Повторяти до",
            "dxScheduler-recurrenceRepeatDaily": "днів(дня)",
            "dxScheduler-recurrenceRepeatWeekly": "тижня(тижнів)",
            "dxScheduler-recurrenceRepeatMonthly": "місяця(місяців)",
            "dxScheduler-recurrenceRepeatYearly": "року(років)",
            "dxScheduler-recurrenceRepeatOnDate": "по дату",
            "dxScheduler-recurrenceRepeatCount": "повторень",
            "dxScheduler-switcherDay": "День",
            "dxScheduler-switcherWeek": "Тиждень",
            "dxScheduler-switcherWorkWeek": "Робочий тиждень",
            "dxScheduler-switcherMonth": "Місяць",
            "dxScheduler-switcherTimelineDay": "Хронологія дня",
            "dxScheduler-switcherTimelineWeek": "Хронологія тижня",
            "dxScheduler-switcherTimelineWorkWeek": "Хронологія робочого тижня",
            "dxScheduler-switcherTimelineMonth": "Хронологія місяця",
            "dxScheduler-switcherAgenda": "Розклад",
            "dxScheduler-allDay": "Увесь день",
            "dxScheduler-confirmRecurrenceEditMessage": "Ви хочете відредагувати тільки цю подію або всю серію?",
            "dxScheduler-confirmRecurrenceDeleteMessage": "Ви хочете видалити тільки цю подію або всю серію?",
            "dxScheduler-confirmRecurrenceEditSeries": "Усю серію",
            "dxScheduler-confirmRecurrenceDeleteSeries": "Усю серію",
            "dxScheduler-confirmRecurrenceEditOccurrence": "Тільки цю подію",
            "dxScheduler-confirmRecurrenceDeleteOccurrence": "Тільки цю подію",
            "dxScheduler-noTimezoneTitle": "Часовий пояс не обраний",
            "dxScheduler-moreAppointments": "і ще {0}",
            "dxCalendar-todayButtonText": "Сьогодня",
            "dxCalendar-ariaWidgetName": "Календар",
            "dxColorView-ariaRed": "Червоний",
            "dxColorView-ariaGreen": "Зелений",
            "dxColorView-ariaBlue": "Синій",
            "dxColorView-ariaAlpha": "Прозорість",
            "dxColorView-ariaHex": "Код кольору",
            "dxTagBox-selected": "{0} обрано",
            "dxTagBox-allSelected": "Обрано всі ({0})",
            "dxTagBox-moreSelected": "і ще {0}",
            "vizExport-printingButtonText": "Друк",
            "vizExport-titleMenuText": "Експорт/Друк",
            "vizExport-exportButtonText": "{0} файл",
            "dxFilterBuilder-and": "І",
            "dxFilterBuilder-or": "Або",
            "dxFilterBuilder-notAnd": "Не І",
            "dxFilterBuilder-notOr": "Не Або",
            "dxFilterBuilder-addCondition": "Додати умову",
            "dxFilterBuilder-addGroup": "Додати групу",
            "dxFilterBuilder-enterValueText": "<введіть значення>",
            "dxFilterBuilder-filterOperationEquals": "Рівно",
            "dxFilterBuilder-filterOperationNotEquals": "Не рівно",
            "dxFilterBuilder-filterOperationLess": "Менше",
            "dxFilterBuilder-filterOperationLessOrEquals": "Менше або рівно",
            "dxFilterBuilder-filterOperationGreater": "Більше",
            "dxFilterBuilder-filterOperationGreaterOrEquals": "Більше або рівно",
            "dxFilterBuilder-filterOperationStartsWith": "Починаеться з",
            "dxFilterBuilder-filterOperationContains": "Містить",
            "dxFilterBuilder-filterOperationNotContains": "Не Містить",
            "dxFilterBuilder-filterOperationEndsWith": "Закінчується на",
            "dxFilterBuilder-filterOperationIsBlank": "Порожнє",
            "dxFilterBuilder-filterOperationIsNotBlank": "Не порожнє",
            "dxFilterBuilder-filterOperationBetween": "У диапазоні",
            "dxFilterBuilder-filterOperationAnyOf": "Будь-який з",
            "dxFilterBuilder-filterOperationNoneOf": "Жоден з",
            "dxHtmlEditor-dialogColorCaption": "Змінити кольор тексту",
            "dxHtmlEditor-dialogBackgroundCaption": "Змінити колір фону",
            "dxHtmlEditor-dialogLinkCaption": "Додати посилання",
            "dxHtmlEditor-dialogLinkUrlField": "URL",
            "dxHtmlEditor-dialogLinkTextField": "Текст",
            "dxHtmlEditor-dialogLinkTargetField": "Відкрити у новому вікні",
            "dxHtmlEditor-dialogImageCaption": "Додати зображення",
            "dxHtmlEditor-dialogImageUrlField": "URL",
            "dxHtmlEditor-dialogImageAltField": "Альтернативний текст",
            "dxHtmlEditor-dialogImageWidthField": "Ширина (px)",
            "dxHtmlEditor-dialogImageHeightField": "Висота (px)",
            "dxHtmlEditor-heading": "Заголовок",
            "dxHtmlEditor-normalText": "Звичайний текст"
        }
    })
});
