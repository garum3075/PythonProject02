$(function () {
    let btnhtml =
        `<button class="btn btn-gotop" id="gotop" data-target="body">
            <i class="fa-regular fa-circle-up fa-5x mb-1"></i><br><span class="h5 fw-900">Top</span>
        </button>`
    $("body").append(btnhtml)
    $(document).on("click", "#gotop", function () {
        $('html, body').animate({
            scrollTop: 0
        }, 50);
    })
});




