
selectElement = function(){
    let element = document.getElementById('slot_len')
    return element.value
}

loadFrame = function(id){
    var data = {'Duration': selectElement()};
    console.log(data)
    $.post(URL, data, function(responce){
        if(typeof localStorage.getItem('starterVID') != 'undefined'){
            let iframe = document.getElementById('starterVID')
            iframe.contentWindow.location.reload()
        }
    });
}

if(typeof localStorage.getItem('starterVID') != 'undefined'){
	let iframe = document.getElementById('starterVID')
    iframe.contentWindow.location.reload()
}

  