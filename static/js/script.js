$(document).ready(function(){
      $('.sidenav').sidenav();
      $('.modal').modal();


    // concept of validating form input field and showing error message taken from youtube video of The IT guy (https://www.youtube.com/watch?v=W4-5WM60gWg&t=121s)
    // Some of the codes were also taken and modified as per project requirements

      $("#error_img_url").hide();
      $("#error_job_type").hide();
      $("#error_company_name").hide();
      $("#error_cost").hide();
      $("#error_phone").hide();
      $("#error_email").hide();
      $ ("#error_desc").hide();

      var minLength = 5;
      var medLength = 15;
      var maxlength = 250;
      var error_img_url = false;
      var error_job_type = false;
      var error_company_name = false;
      var error_cost = false;
      var error_phone = false;
      var error_email = false;


      $("#company_name").focusout(function () {
            validate_company_name()
      });

      $("#job_type").focusout(function () {
            validate_jobtype();
      });


      $("#email").focusout(function () {
            validate_email();
      });

      $("#cost").focusout(function () {
            validate_cost();
      });

      $("#phone").focusout(function () {
            validate_phone_number();
      });

      $("#img_url").focusout(function () {
            validate_img_url();
      });

      $("#desc").focusout(function () {
        validate_desc();
  });
      // validate company name field in the form and show error message if length of input field is not within the range of 5 and 15
      function validate_company_name() {
            var company_name_length = $('#company_name').val().length;
           
            if ( company_name_length < minLength || company_name_length > medLength ) {
                  $("#error_company_name").html("*Minimum 5 and Maximum 15 charecters allowed ");
                  $("#error_company_name").show();
                  $("#company_name").css("border-bottom","2px solid #F90A0A");
                  error_company_name = true;
               } else {
                  $("#error_company_name").hide();
                  $("#company_name").css("border-bottom","2px solid #34F458");
               }
      }

      // validate job type field in the form and show error message if length of input field is not within the range of 5 and 15
      function validate_jobtype() {
            var job_type_length = $('#job_type').val().length;
            if ( job_type_length < minLength || job_type_length > medLength ) {
                  $("#error_job_type").html("*Minimum 5 and Maximum 15 charecters allowed ");
                  $("#error_job_type").show();
                  $("#job_type").css("border-bottom","2px solid #F90A0A");
                  error_job_type = true;
               } else {
                  $("#error_job_type").hide();
                  $("#job_type").css("border-bottom","2px solid #34F458");
               }
      }
      // validate contact no field in the form and show error message if length of input field is not within the range of 9 and 13
      function validate_phone_number() {
            var phone_length = $('#phone').val().length;
            if ( phone_length < 9 || phone_length > 13 ) {
                  $("#error_phone").html("*Phone no should be minimum 9 and maximum 13 numbers");
                  $("#error_phone").show();
                  $("#phone").css("border-bottom","2px solid #F90A0A");
                  error_phone = true;
               } else {
                  $("#error_phone").hide();
                  $("#phone").css("border-bottom","2px solid #34F458");
               }
      }
      // validate email field in the form and show error message if incorrect email format supplied
      function validate_email() {
            var pattern = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
            var email = $("#email").val();
            if (pattern.test(email) && email !== '') {
                  $("#error_email").hide();
                  $("#email").css("border-bottom", "2px solid #34F458");
            } else {
                  $("#error_email").html("*Please enter valid email");
                  $("#error_email").show();
                  $("#email").css("border-bottom", "2px solid #F90A0A");
                  error_email = true;
            }
      }
      // validate cost field in the form and show error message if length of input field is not within the range of 1 and 3
      function validate_cost() {
            var cost_length = $('#cost').val().length;
            if ( cost_length < 1 || cost_length > 3 ) {
                  $("#error_cost").html("*Charge can minimum 1 and maximum 3 numbers");
                  $("#error_cost").show();
                  $("#cost").css("border-bottom","2px solid #F90A0A");
                  error_cost = true;
               } else {
                  $("#error_cost").hide();
                  $("#cost").css("border-bottom","2px solid #34F458");
               }
      }
      // validate image URL field in the form and show error message if incorrect URL method used
      // URL must be start with https://
      function validate_img_url() {
            var img_url = $('#img_url').val();
            if (img_url && !img_url.match(/^http([s]?):\/\/.*/)) {
                  $("#error_img_url").html("*Please provide valid url");
                  $("#error_img_url").show();
                  $("#img_url").css("border-bottom","2px solid #F90A0A");
                  error_img_url = true;
                }else {
                  $("#error_img_url").hide();
                  $("#img_url").css("border-bottom","2px solid #34F458");
               }

      }
      // validate description field in the form and show error message if length of input field is not within the range of 20 and 250
      function validate_desc() {
        var desc_length = $('#desc').val().length;
        if ( desc_length < medLength || desc_length > maxlength){
              $("#error_desc").html("*Minimum 20 and Max 250 Characters allowed");
              $("#error_desc").show();
              $("#desc").css("border-bottom","2px solid #F90A0A");
              error_desc = true;
            } else {
              $("#error_desc").hide();
              $("#desc").css("border-bottom","2px solid #34F458");
           }
  }

});