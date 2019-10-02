import React from "react";
import { Link } from "react-router-dom";

const Home = () => (
  <div>
    <h1>Basic React App</h1>
    <Link to="/about-us">Go to About Us</Link>
  </div>
);

export default Home;
