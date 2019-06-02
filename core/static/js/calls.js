function clock() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('clock').innerHTML = h + ":" + m + ":" + s;
    var t = setTimeout(clock, 500);
};

function checkTime(i) {
    if (i < 10) {i = "0" + i};  // Add zero in front of numbers < 10
    return i;
};

function playSound() {
    var sound = document.getElementById("audio");

    // Show loading animation.
    var playPromise = sound.play();

    if (playPromise !== undefined) {
        playPromise.then(_ => {
        // Automatic playback started!
        // Show playing UI.
        })
        .catch(error => {
        // Auto-play was prevented
        // Show paused UI.
        });
    }
}

var last_call = null;

function checkChanges() {

    $.ajax({
        url: '/chamadas/checar-mudancas/',
        success: function(data) {

            if(last_call == null) {
                if(last_call != data['calls'][0].time) {
                    last_call = data['calls'][0].time;
                    playSound();
                }
            }

            if(last_call != data['calls'][0].time) {
                last_call = data['calls'][0].time;
                playSound();
            }

            // Last patient
            if(data['calls'][0].patient != null && data['calls'][0].type != null) {
                $('#patient-name-last').html(data['calls'][0].patient.toUpperCase());
                $('#patient-type-last').html(data['calls'][0].type.toUpperCase());
            }
            else {
                $('#patient-name-last').html(data['calls'][0].patient);
                $('#patient-type-last').html(data['calls'][0].type);
            }
            $('#patient-location-last').html(data['calls'][0].location);

            if(data['calls'][0].type == 'CONSULTA') {
                $('#patient-location-type-last').html('Sala');
            }
            else if(data['calls'][0].type == 'CADASTRAMENTO') {
                $('#patient-location-type-last').html('Guichê');
            }
    
            // Patient 1
            $('#patient-name-1').html(data['calls'][0].patient);
            $('#patient-type-1').html(data['calls'][0].type);
            $('#patient-location-1').html(data['calls'][0].location);

            // Patient 2
            $('#patient-name-2').html(data['calls'][1].patient);
            $('#patient-type-2').html(data['calls'][1].type);
            $('#patient-location-2').html(data['calls'][1].location);

            // Patient 3
            $('#patient-name-3').html(data['calls'][2].patient);
            $('#patient-type-3').html(data['calls'][2].type);
            $('#patient-location-3').html(data['calls'][2].location);

            // Patient 4
            $('#patient-name-4').html(data['calls'][3].patient);
            $('#patient-type-4').html(data['calls'][3].type);
            $('#patient-location-4').html(data['calls'][3].location);

            // Patient 5
            $('#patient-name-5').html(data['calls'][4].patient);
            $('#patient-type-5').html(data['calls'][4].type);
            $('#patient-location-5').html(data['calls'][4].location);
        }
    });
    setTimeout(checkChanges, 1000);
};

$(document).ready(function () {
    checkChanges();
    clock();
});
