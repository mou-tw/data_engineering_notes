
function getTime(){
    let dt = new Date();
    h = dt.getHours();
    m = dt.getMinutes();

    if (h <10){
        h = "0" + h;
    }

    if (m<10){
        m = "0" +m;
    }
    return h + ":"  + m
}

function initMessage(){
    let initMessage = "Ask Me somthing................................. "
    document.getElementById('initmessage').innerHTML = 
        '<span>' + initMessage + ' </span>'
    $('#chat-time').append(getTime());
    // document.getElementsByClassName('input-block').scrollIntoView(false);

}


initMessage()


function getBotResponse(userText){
    
    let botResponse = userText;
    let botHtml = '<p class="chatbottext "><span>' + botResponse + ' </span></p>';
    
    $('#chatbdy').append(botHtml);
    document.getElementById('bottom').scrollIntoView(true);

}

function SendMessage(){
    let userMessage = $('#userText').val().trim();

    if (userMessage){
        let sendHtml = '<p class="usertext "><span>' + userMessage + ' </span></p>'
        
        $("#userText").val("");
        $('#chatbdy').append(sendHtml);

        document.getElementById('bottom').scrollIntoView(true);

        setTimeout( ()=>{
            getBotResponse(userMessage)
        },0
        )
    }
}

$('#send-btn').on('click',function(){
    console.log('asdf')
    SendMessage();
})


$('#userText').on('keypress', function(e){
    if(e.which == 13){ 
        SendMessage()
    }
})