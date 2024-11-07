

let index_landPage = 0;    
let landPage = document.querySelector(".landpage");
let pointers = document.querySelectorAll(".pointer");

function changeLandPage(){

    pointers[index_landPage].classList.toggle("active");
    
    if(index_landPage >= 2)
    {
        index_landPage = -1;
    }

    index_landPage = index_landPage + 1;
    landPage.style.backgroundImage = `url(${photos[index_landPage]})`;
    pointers[index_landPage].classList.toggle("active");
}


setInterval(changeLandPage, 7000);




//client
let flagParaClient = 0;
let clientBtns = document.querySelectorAll('.client .btn');


//medicin
function addMedicin(){
        document.querySelector(".medicin .intial-para").classList.toggle("hide");
        document.querySelector(".add-medicin-form").classList.toggle("hide");
}

function onaddMedicin(){
    document.querySelector(".medicin .intial-para").classList.toggle("hide");
    document.querySelector(".one-medicin-form").classList.toggle("hide");
}
//bill
function inputHandel(selectorSection, selectorInputForm){
    document.querySelector(`.${selectorSection} .intial-para`).classList.toggle("hide");
    document.querySelector(`.${selectorInputForm}`).classList.toggle("hide");
}