
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
   
    document.getElementById('initText').innerHTML = 
        '<p class="chatbotContent">' + initMessage + ' </p>'
    // $('#chat-time').append(getTime());
    // document.getElementsByClassName('input-block').scrollIntoView(false);

}


initMessage()


function getBotResponse(userText){
    let botResponse = userText;
    let botHtml = 
    '<li  class="chatbot__entity">' + 
    '<p class="chatbotContent ">' + botResponse + '</p></li>' ;
    $('#chatbody__list').append(botHtml);
    document.getElementById('inputBlock').scrollIntoView(true);

}

function SendMessage(){
    let userMessage = $('#userText').val().trim();
    if (userMessage){
        let sendHtml = 
        '<li  class="user__entity">' + 
        '<p class="userContent ">' + userMessage + '</p></li>' ;
        $("#userText").val("");
        $('#chatbody__list').append(sendHtml);

        document.getElementById('inputBlock').scrollIntoView(true);

        setTimeout( ()=>{
            getBotResponse(userMessage)
        },0
        )
    }
}

$('#inputBlock__sendBtn').on('click',function(){
    console.log('asdf')
    SendMessage();
})


$('#userText').on('keypress', function(e){
    if(e.which == 13){ 
        SendMessage()
    }
})