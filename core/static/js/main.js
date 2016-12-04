/**
 * Created by danilakimov on 18.11.16.
 */

$(".show__marks").on("click", function () {
    $(this).parent().find(".marks__all").toggle();
});

$(".blocks").on("click", function () {
    window.location = $(this).find("a").attr('href');
});

//$('.dropdown-toggle').dropdown();

$('.js__mark_submit').click(function (e){
    e.preventDefault();
    var newThis = $(this);
    swal({
        title: "Оценка поставлена",
        text: "Оценка успешно поставлена",
        type: "success",
    }, function () {
        window.location = newThis.attr('href');
    });
});

//$( "#marks__form" ).validate({
//  rules: {
//    orator: {
//      required: true,
//        min: {
//            param: 0
//        },
//        max: {
//          param: 10
//        },
//        errorPlacement: function (error, element) {
//            element.attr("placeholder", error.text());
//        },
//        submitHandler: function (form) { // for demo
//            alert('valid form submitted'); // for demo
//            return false; // for demo
//        }
//    }
//  }
//});
//
//$


//$('.marks__form').validate({ // initialize the plugin
//        rules: {
//            data_input: {
//                required: true,
//                    min:{
//                        param:0
//                    },
//                    max:{
//                        param:10
//                    }
//            }
//        },
//        errorPlacement: function (error, element) {
//            element.attr("placeholder", error.text());
//        }
//    });

$('.marks__form').submit(function(){
  location.href = 'teachers_rating_chart.html';
    return false;
});