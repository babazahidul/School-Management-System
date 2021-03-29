$(document).ready(function(){
    $('.btn_cls').on('click', function(){
    var btn_property = $(this)
    var row = $(this).closest("tr");
    var roll = row.find(".std_roll").text();
    var cls = row.find(".std_class").text();
    api_url = "http://localhost:8000/api/attendance/"+ cls + '/' + roll;

    $.ajax({
        url: api_url,
        method: 'get',
        success: function(data){
            btn_property.addClass('btn btn-success')
            console.log("Success Status", data)
        },
        error: function(err){
            btn_property.addClass('btn btn-danger')
            console.log("errorssss", err)
        },
    });
    })
})