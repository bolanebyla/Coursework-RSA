// вадидация формы
function formValid(form) {

    var hasEmpty = false;
    // Перебираем все поля формы
    $('form#' + form).find('input').each(function () {
        if ($(this).prop('required')) {
            // если поле обязательное, но пустое, то hasEmpty становится true
            hasEmpty = hasEmpty || !$(this).val();
        }
    });
    if (hasEmpty) {
        return false;
    } else {
        return true;
    }

}

// генерация
$(document).ready(function () {
    $("#generate_btn").click(
        function () {

            if (formValid('key_generation_form')) {
                // Здесь делаем отправку
                sendAjaxForm_generation('result_form', 'key_generation_form', '/api/generate_values');
            } else {
                $('#result_of_generation').html('Ошибка. Не заполнены обязательные поля!');
            }

            return false;
        }
    );
});

function sendAjaxForm_generation(result_of_generation, key_generation_form, url) {
    $.ajax({
        url: url, //url страницы
        type: "POST", //метод отправки
        dataType: "html", //формат данных
        data: $("#" + key_generation_form).serialize(),  // Сеарилизуем объект
        success: function (response) { //Данные отправлены успешно
            result = $.parseJSON(response);

            $('#result_of_generation').html(
                '<h3>Открытый ключ</h3>e = ' + result.e + ' n = ' + result.n + '<br>' + '<h3>Секретный ключ</h3>d = ' + result.d + ' n = ' + result.n + '<br><br>');
        },
        error: function (response) { // Данные не отправлены
            $('#result_of_generation').html('Ошибка. Данные не сгенирированы.');
        }
    });
}

///////////////////////

// кодирование
$(document).ready(function () {
    $("#encrypt_btn").click(
        function () {

            if (formValid('encrypt_form')) {
                // Здесь делаем отправку
                sendAjaxForm_encrypt('result_of_encrypt', 'encrypt_form', '/api/encrypt');
            } else {
                $('#result_of_encrypt').html('Ошибка. Не заполнены обязательные поля!');
            }
            return false;
        }
    );
});

function sendAjaxForm_encrypt(result_of_encrypt, encrypt_form, url) {
    $.ajax({
        url: url, //url страницы
        type: "POST", //метод отправки
        dataType: "html", //формат данных
        data: $("#" + encrypt_form).serialize(),  // Сеарилизуем объект
        success: function (response) { //Данные отправлены успешно
            result = $.parseJSON(response);
            $('#result_of_encrypt').html(
                '<h3>Результат</h3>' + result.encrypted_data + '<br><br>');
        },
        error: function (response) { // Данные не отправлены
            $('#result_of_encrypt').html('Ошибка. Не удалось зашифровать.');
        }
    });
}

//////////////////

// декодирование
$(document).ready(function () {
    $("#decrypt_btn").click(
        function () {

            if (formValid('decrypt_form')) {
                // Здесь делаем отправку
                sendAjaxForm_decrypt('result_of_decrypt', 'decrypt_form', '/api/decrypt');
            } else {
                $('#result_of_decrypt').html('Ошибка. Не заполнены обязательные поля!');
            }
            return false;
        }
    );
});

function sendAjaxForm_decrypt(result_of_encrypt, decrypt_form, url) {
    $.ajax({
        url: url, //url страницы
        type: "POST", //метод отправки
        dataType: "html", //формат данных
        data: $("#" + decrypt_form).serialize(),  // Сеарилизуем объект
        success: function (response) { //Данные отправлены успешно
            result = $.parseJSON(response);
            $('#result_of_decrypt').html(
                '<h3>Результат</h3>' + result.decrypted_data + '<br><br>');
        },
        error: function (response) { // Данные не отправлены
            $('#result_of_decrypt').html('Ошибка. Не удалось расшифровать.');
        }
    });
}