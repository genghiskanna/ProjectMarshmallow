/**
 * Created by nishaanthftw on 22/02/17.
 */

$(document).on('submit','#engine_form',function(e){
   e.preventDefault();
   $.ajax({
       type: 'POST',
       url:'process/',
       data:{
           product_name:$('#product_name').val(),
           product_feature:$('#product_feature').val(),
           tweet_limit:$('#tweet_limit').val();
           csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val();
       },
       success:function(){
           alert("success");
       }
   })
});
