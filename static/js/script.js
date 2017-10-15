$(function(){

  $(".comment_btn").hover(function(){
    $( this ).toggleClass("fa fa-commenting-o");
    $( this ).toggleClass("fa fa-comment-o");
  });

  $(".comment_btn").click(function(){
    var id = $( this ).attr('value');
    if ($("#" + id).css("display")=="none") {
      $("#" + id).css("display","block");
      var div_height = parseInt($("#" + id).closest(".post_div").css("height"));
      $("#" + id).closest(".post_div").css("height", div_height + 50);
    }else{
      $("#" + id).css("display","none");
      $("#" + id).closest(".post_div").css("height","100%");
    }
  });


  $(".img_post").dblclick(function(){
    //animaatio sydän
    //if ($( this ).closest("i").attr("class")=="unlike_btn"){
    //  console.log("unlike'd");
    //  $( this ).closest("i").removeClass("fa-heart unlike_btn").addClass("fa-heart-o like_btn");
    //}else if ($( this ).closest("i").attr("class")=="like_btn") {
    //  console.log("like'd");
    //  $(this).removeClass("fa-heart-o like_btn").addClass("fa-heart unlike_btn");
    //}else{
    //  console.log("feil");
    //}
    var type = $(this).closest("a").attr("class");
    alert(type);
    //var post_id = $( this ).attr("value");
    //var csrftoken = getCookie("csrftoken");
    //like(post_id, csrftoken);
  });


  $(".fa.fa-heart-o.like_btn").one("click", function(){
    $(this).removeClass("fa-heart-o like_btn").addClass("fa-heart unlike_btn");
    var post_id = $( this ).closest("h3").attr("value");
    var csrftoken = getCookie('csrftoken');
    like(post_id, csrftoken);
  });


  $(".fa.fa-heart.unlike_btn").one("click", function(){
    $(this).removeClass("fa-heart unlike_btn").addClass("fa-heart-o like_btn");
    var post_id = $( this ).closest("h3").attr("value");
    var csrftoken = getCookie('csrftoken');
    like(post_id, csrftoken);
  });


  $(".alert-success").fadeTo(2000, 500).slideUp(500, function(){
    $(".alert-success").slideUp(500);
  });

  $(".alert-danger").fadeTo(2000, 500).slideUp(500, function(){
    $(".alert-danger").slideUp(500);
  });


  function like(post_id, csrftoken){
    $.ajax({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      },
      url : "../../like/" + post_id + "/", // the endpoint
      type : "POST", // http method

      success : function(){
        console.log("success!");
      }
    });
  }



  function csrfSafeMethod(method) {
      // these HTTP methods do not require CSRF protection
      return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


});
