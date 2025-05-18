<template>
  <div>
    <div class="container py-3"></div>
    <div
      class="container col-md-5 bg-body-tertiary shadow p-5 border border-2 rounded border-dark"
      style="--bs-border-opacity: 0.5; --bs-bg-opacity: 0.05"
    >
      <form @submit.prevent="register" class="">
        <h1>Register</h1>
        <hr />
        <div class="row">
          <div class="col-12">
            <label class="form-label" for="email">Email Address</label>
            <input
              v-model="formData.email"
              class="form-control"
              id="email"
              maxlength="255"
              minlength="1"
              name="email"
              placeholder="user@HSA.com"
              required
              type="text"
            />
            <div class="invalid-feedback">
              Please enter a valid email address.
            </div>
          </div>
          <div class="col-md-12">
            <label class="form-label" for="name">Name</label>
            <input
              v-model="formData.name"
              class="form-control"
              id="name"
              maxlength="255"
              minlength="2"
              name="name"
              required
              type="text"
            />
            <div class="invalid-feedback">Please enter a Name.</div>
          </div>
          <div class="col-md-6">
            <label class="form-label" for="password">Password</label>
            <input
              v-model="formData.password"
              class="form-control"
              id="password"
              maxlength="32"
              minlength="8"
              name="password"
              required
              type="password"
            />
            <div class="invalid-feedback">The Password is not valid.</div>
          </div>
          <div class="col-md-6">
            <label class="form-label" for="rePassword">Repeat Password</label>
            <input
              v-model="formData.rePassword"
              class="form-control"
              id="rePassword"
              maxlength="32"
              minlength="8"
              name="rePassword"
              required
              type="password"
            />
            <div class="invalid-feedback">The Password is not valid.</div>
          </div>
          <div class="col-12">
            <div class="form-check">
              <input
                v-model="formData.terms"
                class="form-check-input"
                id="terms"
                name="terms"
                required
                type="checkbox"
                value="y"
              />
              <label class="form-check-label" for="Terms">
                <label for="Terms">Agree To Terms and Conditions</label>
              </label>
            </div>
          </div>
          <div class="col-12">
            <label></label>
            <button
              class="btn btn-primary btn-block w-100 col-12"
              id="Submit"
              type="submit"
            >
              Sign Up
            </button>
          </div>
        </div>
      </form>
      <p v-if="error" style="color: red">{{ error }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "RegisterPage",
  created() {
    document.title = "Register!";
  },
  data() {
    return {
      error: "",
      formData: {
        email: "",
        password: "",
        rePassword: "",
        name: "",
        terms: false,
      },
    };
  },
  methods: {
    register() {
      axios
        .post("http://localhost:5000/api/v1/register", this.formData)
        .then((response) => {
          console.log("Registration successful:", response.data);
          this.error = response.data.message;
          location.replace("/login");
        })
        .catch((error) => {
          console.error("Registration error:", error);
        });
    },
  },
};
</script>

<style scoped>
.form-label {
  text-align: left;
}
</style>
