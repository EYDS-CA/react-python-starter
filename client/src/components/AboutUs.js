import React from "react";
import { Link } from "react-router-dom";
import Axios from "@/apiClient/Axios";

// Example stateful component
// Example API request
export default class AboutUs extends React.Component {
  state = { isLoading: true };

  componentDidMount() {
    Axios.get("/example_endpoint")
      .then(response =>
        this.setState({
          response: response.examples[0] && response.examples[0].string_field,
          isLoading: false,
        })
      )
      .catch(console.error);
  }

  render() {
    return (
      <div>
        <h1>About Us</h1>
        {this.state.isLoading ? (
          <p>Loading...</p>
        ) : (
          <p>{this.state.response}</p>
        )}
        <Link to="/">Go to Home</Link>
      </div>
    );
  }
}
