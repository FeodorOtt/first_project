    var dictionary = {
        'en': {
            //Welcome page and Nave bar
            'idMain': 'Main',
            'idTransaction': 'Transactions',
            'idClient': 'Clients',
            'idCurrency': 'Currency',
            'idLogout': 'Logout',
            'idAbout': 'About',
            'idLogin': 'Login',
            'idGetStarted': ' to get started!',
            'idWelcome': 'Welcome to ',
            'idAppName': '<b>pyERP</b>',
            'idLang': 'Language',
            'idTheme': 'Theme',
            //Transaction
            'db_client_id': 'Dt Client',
            'cr_client_id': 'Ct Client',
            'amount': 'Amount',
            'currency_id': 'Currency',
            'amount_e': 'Equivalent',
            'payment_details': 'Details',
            //Client
            'name': 'Name',
            'type': 'Type',
            'is_resident': 'Resident',
            'responsible_client': 'Responsible',
            'cr_client_id': 'Ct Client',
            'amount': 'Amount',
            'currency_id': 'Currency',
            'payment_details': 'Details',
            'transactions_of': 'Transactions of ',
            //Currency
            'short_name': 'Short Name',
            'ISO_digit': 'ISO digit',
            'ISO_char': 'ISO char',
            'status_id': 'Status'
        },
        'de': {
            //Welcome page and Nave bar
            'idMain': 'Main',
            'idTransaction': 'Transaktionen',
            'idClient': 'Kunden',
            'idCurrency': 'Währung',
            'idLogout': 'Ausloggen',
            'idAbout': 'Über',
            'idLogin': 'Einloggen',
            'idWelcome': 'Willkommen bei ',
            'idAppName': '<b>pyERP</b>',
            'idLang': 'Sprache',
            'idTheme': 'Thema',
            //Transactions
            'db_client_id': 'Dt Client',
            'cr_client_id': 'Ct Client',
            'amount': 'Betrag',
            'currency_id': 'Währung',
            'amount_e': 'Gleichwertig',
            'payment_details': 'Zahlungszweck',
            //Client
            'name': 'Name',
            'type': 'Type',
            'is_resident': 'Resident',
            'responsible_client': 'Responsible',
            'cr_client_id': 'Ct Client',
            'amount': 'Betrag',
            'currency_id': 'Währung',
            'payment_details': 'Zahlungszweck',
            'transactions_of': 'Transaktionen ',
            //Currency
            'short_name': 'Kurzname',
            'ISO_digit': 'ISO Digit',
            'ISO_char': 'ISO Zeichen',
            'status_id': 'Status'
        },
        'ru': {
            //Welcome page and Nave bar
            'idMain': 'Главная',
            'idTransaction': 'Транзакции',
            'idClient': 'Клиенты',
            'idCurrency': 'Валюта',
            'idLogout': 'Выйти',
            'idAbout': 'О...',
            'idLogin': 'Войти',
            'idWelcome': 'Добро пожаловать в ',
            'idAppName': '<b>pyERP</b>',
            'idLang': 'Язык',
            'idTheme': 'Тема',
            //Transactions
            'db_client_id': 'Клиент Дт',
            'cr_client_id': 'Клиент Кт',
            'amount': 'Сумма',
            'currency_id': 'Валюта',
            'amount_e': 'Эквивалент',
            'payment_details': 'Примечание',
            //Client
            'name': 'Название (Имя)',
            'type': 'Тип',
            'is_resident': 'Резидент',
            'responsible_client': 'Ответственный',
            'cr_client_id': 'Клиент Кт',
            'amount': 'Сумма',
            'currency_id': 'Валюта',
            'payment_details': 'Примечание',
            'transactions_of': 'Транзакции ',
            //Currency
            'short_name': 'Короткое',
            'ISO_digit': 'ISO цифр.',
            'ISO_char': 'ISO симв.',
            'status_id': 'Статус'
        },
        'ua': {
            //Welcome page and Nave bar
            'idMain': 'Головна',
            'idTransaction': 'Транзакції',
            'idClient': 'Клієнти',
            'idCurrency': 'Валюта',
            'idLogout': 'Вийти',
            'idAbout': 'Про...',
            'idLogin': 'Увійти',
            'idWelcome': 'Ласкаво просимо до ',
            'idAppName': '<b>pyERP</b>',
            'idLang': 'Мова',
            'idTheme': 'Тема',
            //Transactions
            'db_client_id': 'Клієнт Дт',
            'cr_client_id': 'Клієнт Кт',
            'amount': 'Сума',
            'currency_id': 'Валюта',
            'amount_e': 'Еквивалент',
            'payment_details': 'Призначення',
            //Client
            'name': "Назва (Ім'я)",
            'type': 'Тип',
            'is_resident': 'Резидент',
            'responsible_client': 'Відповідальний',
            'cr_client_id': 'Клієнт Кт',
            'amount': 'Сума',
            'currency_id': 'Валюта',
            'payment_details': 'Призначення',
            'transactions_of': 'Транзакції ',
            //Currency
            'short_name': 'Коротка',
            'ISO_digit': 'ISO цифр.',
            'ISO_char': 'ISO симв.',
            'status_id': 'Статус'
        }
      };

    DevExpress.localization.loadMessages(dictionary);

    var formatMessage = DevExpress.localization.formatMessage;

    $('#idMain').text(formatMessage('idMain'));
    $('#idTransaction').text(formatMessage('idTransaction'));
    $('#idClient').text(formatMessage('idClient'));
    $('#idCurrency').text(formatMessage('idCurrency'));
    $('#idLogout').text(formatMessage('idLogout'));
    $('#idAbout').text(formatMessage('idAbout'));
    $('.idLogin').text(formatMessage('idLogin'));
    $('#idWelcome').html(formatMessage('idWelcome') + formatMessage('idAppName'));
    $('#idLang').text(formatMessage('idLang'));
    $('#idTheme').text(formatMessage('idTheme'));
