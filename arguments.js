
function addTogether(x) {
  
    var args = Array.prototype.slice.call(arguments);

    function validNumber(test){
        if (typeof test !== 'number'){
            return false;
        }else{
            return true;
        }
    }

    if(args.length >=2){
        if(validNumber(args[0]) && validNumber(args[1])){
          
            return args[0] + args[1];
        }
    }else{
        if(!validNumber(args[0])){
            //if not a valid number
            return undefined;
        }else{
            return function(newNumber){
                if(validNumber(newNumber)){
                    return args[0] + newNumber;
                }else{
                    return undefined;
                }

            };
        }
    }
 
}

//addTogether(2,3);
addTogether(2)(3)
//addTogether(2)([3])