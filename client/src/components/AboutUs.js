import React from "react";
import { Link } from "react-router-dom";
import Axios from "@/apiClient/Axios";

// Example stateful component
export default class AboutUs extends React.Component {
  state = { isLoading: true };

  componentDidMount() {
    // Example API request
    Axios.get("/example_endpoint")
      .then(response =>
        this.setState({
          response: response.examples[0]
            ? response.examples[0].string_field
            : "No Response Data",
        })
      )
      .catch(() => {
        this.setState({
          response: "Something went wrong. Please try again later.",
        });
      })
      .finally(() => {
        this.setState({
          isLoading: false,
        });
      });
  }

  renderFetchedData() {
    return this.state.isLoading ? (
      <p>Loading...</p>
    ) : (
      <p>{this.state.response}</p>
    );
  }

  render() {
    return (
      <div>
        <h1>About Us</h1>
        {this.renderFetchedData()}
        <Link to="/">Go to Home</Link>
      </div>
    );
  }
}
