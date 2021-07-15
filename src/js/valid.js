function val_pass(){
    if(document.getElementbyId("password")[0].value != document.getElementbyId("psw-repeat")[0].value){
        document.getElementbyId('password').innerHTML='wrong';
    }else{
        document.getElementbyId('password').innerHTML='continue';
    }
}
