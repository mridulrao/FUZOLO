SetDate = function(){
    var date = document.getElementById("my_date_picker");
    document.getElementById("date_submit").value = date.value;
    document.getElementById("date_submit").disabled = false;
}

ReloadSlots = function(){
    var ifr = document.getElementById('slots_frame');
    ifr.src = ifr.src;
}