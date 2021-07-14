function val_pass(){
    if(document.getElementbyId("psw")[0].value != document.getElementbyId("psw-repeat")[0].value){
        document.getElementbyId('psw').innerHTML='wrong';
    }else{
        document.getElementbyId('psw').innerHTML='continue';
    }
}
