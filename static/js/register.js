//alert("register.js")

function bindEmailCaptchaClick(){
    $("#captcha-btn").click(function(event){
        //$this means current buttom and object of jquery 
        var $this = $(this);
        //prevent default event
        event.preventDefault();

        var email = $("input[name='email']").val();
        console.log("Email:", email); // Add this line to log the email value
        $.ajax({
            url: "captcha/email?email=" + email,
            method: "GET",
            success: function(result) {
                var code = result['code'];
                if(code == 200){
                    var countdown = 5;
                    //开始倒计时之前，就取消按钮的点击事件
                    $this.off("click");
                    var timer = setInterval(function (){
                        $this.text(countdown);
                        countdown -= 1;
                        if(countdown <= 0){
                            clearInterval(timer);
                            $this.text("获取验证码");
                            bindEmailCaptchaClick();
                        }
                    }, 1000);
                    //alert("Email verification code sent successfully.");
                } else {
                    alert(result['message']);
                }
            },
            error: function(error) {
                console.log(error);
            }
        })
    });
}


//整个网页都加载完毕后，再执行的的
$(function(){
    bindEmailCaptchaClick();
});
