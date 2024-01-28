//alert("register.js")

//整个网页都加载完毕后，再执行的的
$(function(){
    $("#captcha-btn").click(function(event){
        event.preventDefault();

        var email = $("input[name='email']").val();

        $.ajax({
            url: "captcha/email?email=" + email,
            method: "GET",
            success: function(result) {
                var code = result['code'];
                if(code == 200){
                    alert("Validation Code sending Success");
                } else {
                    alert(result['message']);
                }
            },
            error: function(error) {
                console.log(error);
            }
        })
    });
});
