function myfunction() {
    var get_email = document.getElementById('email').value;
    alert(get_email)
    frappe.call({
        method: 'myapp.www.example.get_details',
        type: "POST",
        args: {
            'get_email': get_email
        },



    });
}