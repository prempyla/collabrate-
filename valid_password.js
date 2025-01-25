function validateAndModifyPassword(password) {
    let uppercase=false;
    let lowercase=false;
    let digit=false;
    let special=false;
    let isValid=true;
    let isLength=true;
    let new_str=""
    if (password.length<8) {
        isLength=false;
    }
        for (let i=0; i<password.length; i++) {
        if (password[i]>="A" && password[i]<="Z") {
            uppercase=true;
            new_str+=password[i].toLowerCase();
        } else if (password[i]>="a" && password[i]<="z") {
            lowercase=true;
            new_str+=password[i].toUpperCase();
        } else if (password[i]>="0" && password[i]<="9") {
            digit=true;
            new_str+=password[i]
        } else if (password[i]=="!" || password[i]=="@" || password[i]=="#" || password[i]=="$" || password[i]=="%"|| password[i]=="^" || password[i]=="&" || password[i]=="*" ) {
            special=true;
            new_str+=password[i]
        } else {
            isValid=false;
        }
    }
    
    if (uppercase==false || lowercase==false || digit==false|| special==false || isValid==false || isLength==false) {
        console.log("Invalid password")
    } else {
        console.log(new_str)
    }
}
