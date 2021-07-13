function val_pass(){
    if(document.getElementbyId("psw")[0].value != document.getElementbyId("psw-repeat")[0].value){
        document.getElementbyId('psw').innerHTML='wrong';
    }else{
        document.getElementbyId('psw').innerHTML='continue';
    }
}
function val_log(){
    if(document.getElementbyId("log")[0].value != document.getElementbyId("#")[0].value){
        document.getElementbyId('log').innerHTML='continue';
    }else{
        document.getElementbyId('log').innerHTML='wrong';
    }
}
