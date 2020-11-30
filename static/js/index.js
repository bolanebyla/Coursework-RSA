// генерация
$(document).ready(function () {
    $("#generate_btn").click(
        function () {
            sendAjaxForm_generation('result_form', 'key_generation_form', '/api/generate_values');
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
            $('#result_of_generation').html('Ошибка. Данные не отправлены.');
        }
    });
}

///////////////////////

// кодирование
$(document).ready(function () {
    $("#encrypt_btn").click(
        function () {
            sendAjaxForm_encrypt('result_of_encrypt', 'encrypt_form', '/api/encrypt');
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
            $('#result_of_encrypt').html('Ошибка. Данные не отправлены.');
        }
    });
}

//////////////////

// декодирование
$(document).ready(function () {
    $("#decrypt_btn").click(
        function () {
            sendAjaxForm_decrypt('result_of_decrypt', 'decrypt_form', '/api/decrypt');
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
            $('#result_of_decrypt').html('Ошибка. Данные не отправлены.');
        }
    });
}