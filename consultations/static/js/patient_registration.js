$(document).ready(function () {
    $('#modalPacientePossuiCadastro').modal({backdrop: 'static', keyboard: false}); 
});

$(document).ready(function(){
    $("#search_term").on("keyup", function() {
            var value = $(this).val().toLowerCase();
            $("#tablePacientePossuiCadastro tr").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
});

$(document).ready(function() {
    $(".next-modal").click(function() {
        var pathname = window.location.pathname;
        var first_name = $(this).data("patient-first_name");
        var last_name = $(this).data("patient-last_name");
        var birthdate = $(this).data("patient-birthdate");
        var id = $(this).data("patient-id");

        $("#patient-first_name").html(first_name);
        $("#patient-last_name").html(last_name);
        $("#patient-birthdate").html(birthdate);
        $("#update-patient-button").attr("href", pathname + "atualizar-existente/" + id + "/");
        $("#keep-patient-button").attr("href", pathname + "usar-existente/" + id + "/");

        $('#modalPacientePossuiCadastro').modal('hide');
        $('#modalAtualizarDadosPaciente').modal({backdrop: 'static', keyboard: false});
    });
});

$(document).ready(function($) {
    $(".table-row").click(function() {
        window.document.location = $(this).data("href");
    });
});
