$(".show__marks").on("click", function () {
    $(this).parent().find(".marks__all").toggle();
});

$(".blocks").on("click", function () {
    window.location = $(this).find("a").attr('href');
});

//$('.dropdown-toggle').dropdown();

$('.js_form_submit').on('submit', function (e){
    e.preventDefault();

    //Валидация
    var isLetters = false;
    var isNotInRange = false;
    arrayOfMarks = $(this).find('input[type=number]');
    arrayOfMarks.each(function(){ if (isNaN($(this).val())) isLetters=true;
    else if (($(this).val() > 10 || $(this).val() < 1)) isNotInRange=true;
    });
    if (isLetters || isNotInRange){
        swal({
            title: "Оценка не поставлена",
            text: "Проверьте правильность ввода!",
            type: "error"
            })
    }

    else{
        var newThis = $(this);
        swal({
            title: "Оценка поставлена",
            text: "Оценка успешно поставлена",
            type: "success"
            },
            function () {newThis[0].submit()});
    }

});



$('.marks__form').submit(function(){
  // location.href = 'teachers_rating_chart.html';
    return false;
});