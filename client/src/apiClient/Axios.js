import axios from "axios";

const instance = axios.create({
  baseURL: "http://localhost:5000/api",
});

instance.interceptors.response.use(
  // Automatically unpack the successful response
  response => response.data,
  // Automatically log a failed response and then pass it along
  error => {
    console.error(error);
    return Promise.reject(error);
  }
);

export default instance;
