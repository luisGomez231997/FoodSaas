import React, { useState } from "react";

//Componente para ilustrar el cambio de opción.
import Stepper from "react-stepper-horizontal";

//Componentes locales.
import Shop from "./marketservice/Shop";
import Payment from "./marketservice/Payment";
import EditShop from "./marketservice/EditShoping";
import Cofirmation from "./marketservice/Confirmation";

//Imagenes de los clientes.
import kokoriko from "../assets/images/kokoriko.jpg";
import dominos from "../assets/images/dominos.png";

//peticiones http.
import Axios from "axios";

//Componente Para la venta de productos.
function MarketServices(props) {
  //Propiedades.
  const { subdomain } = props;
  //Estado.
  const [active_step, setActiveStep] = useState(0);
  const [products, setProducts] = useState(null);

  //instancia mentodos.
  const getData = async () => {
    if (!products) {
      await Axios.get(
        "http://" + subdomain + ".localhost:8000/api/products/list"
      )
        .then((res) => {
          if (res.status === 200) {
            console.log("Datos cargados:", res.data);
            setProducts(res.data);
          } else {
            console.log("Datos no cargados");
          }
        })
        .catch((err) => {
          console.log(err);
        });
    }
  };
  //invoca el metodo.
  getData();
  //renderiza el componente.


  return (
    <div className="container">
      <div className="row text-center">
        <Stepper
          steps={[
            { title: "Selecciona tus productos" },
            { title: "Personaliza tu compra" },
            { title: "Confirma el envio a tu domicilio" },
            { title: "Efectua tu compra" },
          ]}
          activeStep={active_step}
        />
        <div className="col-12">
          <img
            src={subdomain === "kokoriko" ? kokoriko : dominos}
            style={{
              height: "300px",
              width: "400px",
              margin: "auto",
            }}
            alt="sample_photo"
          />
        </div>
      </div>
      {active_step === 0 ? (
        <Shop products={products} />
      ) : active_step === 1 ? (
        <EditShop />
      ) : active_step === 2 ? (
        <Cofirmation />
      ) : (
        <Payment />
      )}
    </div>
  );
}

export default MarketServices;