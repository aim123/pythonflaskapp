	$(document).ready(function () {
    setInterval(ShowTime, 1000);
});

function ShowTime() {
    
    var TheDate = new Date();
    
    var TheHour = TheDate.getHours();
    var TheMinutes = TheDate.getMinutes();
    var TheSeconds = TheDate.getSeconds();
    var TheDay= TheDate.getDate();
    var TheMonth= (TheDate.getMonth()+1);
    var TheYear= TheDate.getFullYear();
    TheSeconds = (TheSeconds < 10) ? "0" + TheSeconds :  TheSeconds;
    
    var TheTime =  TheDay+"/"+TheMonth+"/"+ TheYear+ " "+ TheHour + ":" +TheMinutes + ":" + TheSeconds;
    
    $('#TheDate').html(TheTime);     
}