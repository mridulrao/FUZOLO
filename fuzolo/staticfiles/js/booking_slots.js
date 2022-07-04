function add_to_list(id){
    if (parseInt(id) < 50){
        actual_id = id;
        slot_list[0].push(actual_id);
    }
    else if(parseInt(id) >= 50 && parseInt(id) < 99){
        actual_id = parseInt(id) - 49;
        slot_list[1].push(actual_id);
    }
    else{
        actual_id = parseInt(id) - 98;
        slot_list[2].push(actual_id);
    }
}

process_booked_slots = function(slots, day){
    for (let i = 0; i < slots.length; i++) {
        if(slots[i] != ','){
            var actual_slot = 0;
            if(day == 2){
                actual_slot = parseInt(slots[i]) + 49;
            }
            else if(day == 3){
                actual_slot = parseInt(slots[i]) + 98;
            }
            else{
                actual_slot = parseInt(slots[i]);
            }
            document.getElementById(actual_slot).disabled = true
            $('#' + actual_slot).addClass('answerBtnsSelected');
        }
    }
}

if(day1 == undefined){
    day1 = 'NIL';
}
else{
    //console.log(day1);
    //console.log(1);
    process_booked_slots(day1, 1);
}

if(day2 == undefined){
    day2 = 'NIL';
}
else{
    //console.log(day2);
    //console.log(2);
    process_booked_slots(day2, 2);
}

if(day3 == undefined){
    day3 = 'NIL';
}
else{
    //console.log(day3);
    //console.log(3)
    process_booked_slots(day3, 3)
}

function remove_from_list(id){
    if (parseInt(id) < 50){
        actual_id = id;
        slot_list[0].pop(actual_id);
    }
    else if(parseInt(id) >= 50 && parseInt(id) < 99){
        actual_id = parseInt(id) - 49;
        slot_list[1].pop(actual_id);
    }
    else{
        actual_id = parseInt(id) - 98;
        slot_list[2].pop(actual_id);
    }
}


function changeClass(id)
{

    if ($('#' + id).hasClass('answerBtnsSelected'))
    {
        $('#' + id).removeClass('answerBtnsSelected');
        slot_count = slot_count - 1;
        remove_from_list(id);
    }
    else
    {
        if(slot_count > 0){
            if(parseInt(id)-1 > 0 && parseInt(id)+1 < 148){
                var prev_id = parseInt(id) - 1;
                var next_id = parseInt(id) + 1;

                if ($('#' + prev_id).hasClass('answerBtnsSelected') || $('#' + next_id).hasClass('answerBtnsSelected')){
                    $('#' + id).addClass('answerBtnsSelected');  
                    slot_count = slot_count + 1;
                    add_to_list(id);
                    console.log(slot_list)
                }
                else{
                    alert("Only, continous slots can be booked");
                }
            }
            else if(parseInt(id)-1 == 0){
                var next_id = parseInt(id) + 1;
                if($('#' + next_id).hasClass('answerBtnsSelected')){
                    $('#' + id).addClass('answerBtnsSelected');  
                    slot_count = slot_count + 1;
                    add_to_list(id);
                    console.log(slot_list)
                }
                else{
                    alert("Only, continous slots can be booked");
                }
            }
            else if(parseInt(id)+1 == 148){
                var prev_id = parseInt(id) - 1;
                if($('#' + prev_id).hasClass('answerBtnsSelected')){
                    $('#' + id).addClass('answerBtnsSelected');  
                    slot_count = slot_count + 1;
                    add_to_list(id);
                    console.log(slot_list)
                }
                else{
                    alert("Only, continous slots can be booked");
                }
            }
        }  
        else{
            $('#' + id).addClass('answerBtnsSelected');  
            slot_count = slot_count + 1;
            add_to_list(id);
            console.log(slot_list);
        }
    }
}
