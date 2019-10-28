import axios from "axios";

export default axios.create({
  // TODO: Replace with env variable
  baseURL: "http://localhost:5000/api",
});
