
$('.header_buttons img, .burger_close, .burger a').click(() => {
    $('.burger').toggleClass('show');
});
if (document.querySelector('.burger') != null) {
    modal('.burger_button', 'data-close', '.burger');
}

if (document.querySelector('.others') != null) {
    document.querySelectorAll('.others a').forEach((element) => {
        if (location.pathname.includes(encodeURIComponent(element.innerHTML))) {
            element.classList.add('active')
        }
    });
}

if (location.pathname.includes('brand')) {
    document.querySelector('.others.products').style.display = 'flex';
} else if (location.pathname.includes('harmful/items') || location.pathname.includes('harmful_page')) {
    document.querySelector('.others.harmful').style.display = 'flex';
} else if (location.pathname.includes('products') || location.pathname.includes('culture') || location.pathname.includes('harmful')) {
    document.querySelector('.others.all').style.display = 'flex';
} else if (location.pathname.includes('contacts') || location.pathname.includes('publication')) {
    document.querySelector('.others.company').style.display = 'flex';
} else {
    document.querySelector('.main').style.display = 'block';
}
window.onscroll = function() {
    let header = document.querySelector(".header_main .container");
    window.scrollY > 200 ? header.classList.add('blur') : header.classList.remove('blur');
}

// let baseUrl = window.location.protocol + "//" + window.location.host + window.location.pathname;
// let newUrl = baseUrl + '?utm_source=yandex&utm_medium=cpc&utm_campaign=%7Bcampaign_name_lat%7D&utm_content=%7Bad_id%7D&utm_term=%7Bkeyword%7D';
// history.pushState(null, null, newUrl);

let utms_names = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term'];

utms_names.forEach(name => {
    let utm_inputs = document.querySelectorAll(`.${name}`);
    utm_inputs.forEach(input => {
        input.value = new URL(window.location.href).searchParams.get(`${name}`);
    });
});  

$('.brand_others img, .brand_items a').click(() => {
    $('.brand_items').toggleClass('flex');
});
$('.weeds_links a').click(() => {
    $('.weeds_links').toggleClass('flex');
});
$('.weeds_others img').on( "click", function() {
  $( this ).parent().next().toggleClass('flex');
} );
$('.publications_others img').click(() => {
    $('.publications_links').toggleClass('flex');
});
$(window).on( "resize, scroll", () => {
    $('.brand_items').removeClass("flex")
    $('.weeds_links').removeClass("flex")
});

if (document.querySelector('.weather_slider') != null) {
    slider({
        containerSelector: '.weather_slider',
        slideSelector: '.weather_slide',
        nextSlideSelector: '.weather_next',
        prevSlideSelector: '.weather_prev',
        wrapperSelector: '.weather_slider',
        fieldSelector: '.weather_field',
        indicatorsClass: 'weather_indicators',
        swipe: true,
    });
}
if (document.querySelector('.weeds_slider') != null) {
    slider({
        containerSelector: '.weeds_descr_images_bottom',
        slideSelector: '.weeds_slide',
        nextSlideSelector: '.weeds_next',
        prevSlideSelector: '.weeds_prev',
        wrapperSelector: '.weeds_slider',
        fieldSelector: '.weeds_field',
        elementsPerPage: 2, 
        elementsPerPageMobile: 2,
        columnGap: 0.937,
        swipe: true,
    });

    let bottom_images = document.querySelectorAll('.weeds_slide img');

    bottom_images.forEach(image => {
        image.addEventListener('click', (e) => {
            let main_image = document.querySelector('.main_image');
            main_image.setAttribute('src', image.getAttribute('src'))
        });
    }); 
}

if (document.querySelector('.publications_slider') != null) {
    slider({
        containerSelector: '.publications_wrapper',
        slideSelector: '.publications_slide',
        wrapperSelector: '.publications_slider',
        fieldSelector: '.publications_field',
        indicatorsClass: 'publications_indicators',
        swipe: true,
    });
}

if (document.querySelector('.brand_tab') != null) {
    tabs('.brand_header', '.brand_tab', '.brand_headers', 'brand_tab_active');
}
if (document.querySelector('.culture_tab') != null) {
    tabs('.culture_header', '.culture_tab', '.culture_headers', 'culture_tab_active');
}

$("form").submit(function (event) {
    event.preventDefault();
    let name = event.target.classList.value.slice(0, -5);
    let formData = new FormData(document.querySelector(`.${name}_form`));
    sendPhp(name, formData);
});

function sendPhp(name, data) {
    $.ajax({
        url: `./php/send_${name}.php`,
        type: 'POST',
        cache: false,
        data: data,
        dataType: 'html',
        processData: false,
        contentType: false,
        success: function (data) {
            $(`.${name}_form`).trigger('reset');
        }
    });
}
