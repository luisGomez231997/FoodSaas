/*!

=========================================================
* Paper Dashboard React - v1.1.0
=========================================================

* Product Page: https://www.creative-tim.com/product/paper-dashboard-react
* Copyright 2019 Creative Tim (https://www.creative-tim.com)

* Licensed under MIT (https://github.com/creativetimofficial/paper-dashboard-react/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import React from "react";
import ReactDOM from "react-dom";
// import { createBrowserHistory } from "history";
// import { Router, Route, Switch, Redirect } from "react-router-dom";
import * as serviceWorker from "./serviceWorker.js";

import "bootstrap/dist/css/bootstrap.css";
// import "assets/scss/paper-dashboard.scss?v=1.1.0";
// import "assets/demo/demo.css";

import "assets/css/paper-dashboard.css";
import "assets/css/paper-dashboard.css.map";
import "assets/css/paper-dashboard.min.css";


import "assets/css/index.css";
import "perfect-scrollbar/css/perfect-scrollbar.css";
import "assets/css/animate.css";
import "assets/css/login.css";

import App from 'App.js';

ReactDOM.render(<App />, document.getElementById('root'));
serviceWorker.register();