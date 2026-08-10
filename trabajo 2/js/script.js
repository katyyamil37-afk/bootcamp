
let saldo = Number(localStorage.getItem("saldo"));

if (!saldo) {
  saldo = 100000;
  localStorage.setItem("saldo", saldo);
}

function mostrarSaldo() {
  $(".saldo").text("$" + saldo.toLocaleString("es-CL"));
}

$(document).ready(function () {
  mostrarSaldo();

  
  $("#bienvenida").hide().fadeIn(1000);


  $("#loginForm").submit(function (evento) {
    evento.preventDefault();

    let correo = $("#correo").val();
    let clave = $("#clave").val();

    if (correo !== "" && clave !== "") {
      window.location.href = "menu.html";
    } else {
      $("#mensajeLogin")
        .removeClass("d-none")
        .text("Debe completar todos los campos.");
    }
  });

  
  $("#depositForm").submit(function (evento) {
    evento.preventDefault();

    let monto = Number($("#montoDeposito").val());

    if (monto > 0) {
      saldo = saldo + monto;
      localStorage.setItem("saldo", saldo);
      mostrarSaldo();

      $("#mensajeDeposito")
        .removeClass("d-none alert-danger")
        .addClass("alert-success")
        .text("Depósito realizado correctamente.");

      $("#montoDeposito").val("");
    } else {
      $("#mensajeDeposito")
        .removeClass("d-none alert-success")
        .addClass("alert-danger")
        .text("Ingrese un monto válido.");
    }
  });

  
  $("#agregarContacto").click(function () {
    let nombre = $("#nuevoContacto").val();

    if (nombre !== "") {
      $("#contacto").append("<option value='" + nombre + "'>" + nombre + "</option>");
      $("#nuevoContacto").val("");

      $("#mensajeEnvio")
        .removeClass("d-none alert-danger")
        .addClass("alert-success")
        .text("Contacto agregado correctamente.");
    }
  });

 
  $("#sendForm").submit(function (evento) {
    evento.preventDefault();

    let contacto = $("#contacto").val();
    let monto = Number($("#montoEnvio").val());

    if (contacto !== "" && monto > 0 && monto <= saldo) {
      saldo = saldo - monto;
      localStorage.setItem("saldo", saldo);
      mostrarSaldo();

      $("#mensajeEnvio")
        .removeClass("d-none alert-danger")
        .addClass("alert-success")
        .text("Transferencia realizada a " + contacto + ".");

      $("#montoEnvio").val("");
    } else {
      $("#mensajeEnvio")
        .removeClass("d-none alert-success")
        .addClass("alert-danger")
        .text("Revise el contacto, el monto o el saldo disponible.");
    }
  });

  
  $("#filtro").change(function () {
    let tipo = $(this).val();

    if (tipo === "todos") {
      $(".movimiento").show();
    } else {
      $(".movimiento").hide();
      $("." + tipo).show();
    }
  });
});
