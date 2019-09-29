
;function click_action_info(id){
    var x=id
    $.get("/box_request/get_boxapitime/",
                {
                    id: x,
                },
                function (result) {
                    alert(result.message);
                });
    }