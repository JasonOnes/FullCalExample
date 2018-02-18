
// {/* <button onclick="myFunction()">food</button> */}

// THE FOLLOWING IS FROM RICKS HARRY POTTER PROMPT 
function myFunction() {
    var txt;
    var recipe = prompt("What's for dinner", "search");
    if (recipe == null || recipe == "") {
        txt = "User cancelled the prompt.";
    } else {
        txt = "You want " + recipe + " for dinner?";
    }
    document.getElementById("pop-up-confirm").innerHTML = txt;
}