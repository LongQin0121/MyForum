//alert("register.js")
//整个网页都加载完毕后，再执行的的
$(function(){
    $("#captcha-btn").click(function(event){
        //prevent default event
        event.preventDefault();

        var email = $("input[name = 'email']").val();
        alert(email);//print it out
    });
});