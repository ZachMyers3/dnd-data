export let API_URL = "";

if (process.env.NODE_ENV === "development") {
  API_URL = "http://localhost:8000/v1";
} else {
  API_URL = window.location.protocol + "//" + window.location.host + "/api/v1";
}
