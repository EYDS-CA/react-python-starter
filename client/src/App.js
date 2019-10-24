import React from "react";
import { BrowserRouter } from "react-router-dom";
import Routes from "@/Routes";
import "@/styles/index.scss";

const App = () => (
  <BrowserRouter>
    <Routes />
  </BrowserRouter>
);

export default App;
