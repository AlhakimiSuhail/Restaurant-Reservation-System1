function restaurantFields() {
    var restaurantFieldsDiv = document.getElementById("restaurantFields");
    var restaurantRadioButton = document.getElementById("restaurant");
    if(restaurantRadioButton.checked){
        restaurantFieldsDiv.style.display="inline";
        document.getElementById("restaurantName").setAttribute("required", "");
        document.getElementById("restaurantDescription").setAttribute("required", "");
        document.getElementById("restaurantLocation").setAttribute("required", "");
    }
    else{
        restaurantFieldsDiv.style.display="none";
        document.getElementById("restaurantName").removeAttribute("required");
        document.getElementById("restaurantDescription").removeAttribute("required");
        document.getElementById("restaurantLocation").removeAttribute("required");
    }
    
}