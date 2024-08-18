// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();


//  owl carousel script
$(".owl-carousel").owlCarousel({
    loop: true,
    margin: 20,
    nav: true,
    navText: [],
    autoplay: true,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1
        },
        1000: {
            items: 2
        }
    }
});

//    end owl carousel script 



/** google_map js **/
function iniciarMap(){
    var coord = {lat:-33.6250491 ,lng: -70.6319384};
    var map = new google.maps.Map(document.getElementById('map'),{
      zoom: 15,
      center: coord
    });
    var marker = new google.maps.Marker({
      position: coord,
      map: map
    });
}

function confimarEliminar(id) {
    Swal.fire({
        title: "Estás Seguro?",
        text: "Esto no se puede revertir!",
        icon: "error",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Si, elimina"
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire({

            title: "Eliminado!",
            text: "Eliminado correctamente.",
            icon: "success"
          }).then(function() {
            window.location.href = "delete/" + id + "/";
          });
        }
      });
}