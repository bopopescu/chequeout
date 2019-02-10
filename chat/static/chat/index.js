function addMessage(e) {
    $("#submit-form").submit(function(e){
        var formData = $('#submit-form').serializeArray()
        var nameElement = document.getElementById("name")
        form.setAttribute('value', '')
        console.log(formData)
        e.preventDefault()
    })
}
