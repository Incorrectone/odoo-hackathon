<template>
  <div>
    <div class="container py-3"></div>
    <div
      class="container col-md-4 bg-body-tertiary shadow p-4 border border-2 rounded border-dark"
      style="--bs-border-opacity: 0.5; --bs-bg-opacity: 0.05"
    >
      <form
        method="POST"
        action=""
        class=""
        enctype="multipart/form-data"
        @submit.prevent="login"
      >
        <h1>Login</h1>
        <hr />
        <div class="form-outline mb-4 form-floating">
          <input
            class="form-control"
            id="usermail"
            maxlength="255"
            minlength="1"
            name="Mail"
            placeholder="Email address"
            required
            type="text"
            value=""
            v-model="usermail"
          />
          <label for="Mail">Email Address</label>
          <div class="invalid-feedback">
            Please enter a valid email address.
          </div>
        </div>

        <div class="mb-4 form-floating">
          <input
            class="form-control"
            id="password"
            maxlength="32"
            minlength="8"
            name="Password"
            placeholder="Password"
            required
            type="password"
            value=""
            v-model="password"
          />
          <label for="Password">Password</label>
          <div class="invalid-feedback">Please enter a password.</div>
        </div>

        <div class="row mb-4">
          <div class="col d-flex justify-content-center">
            <div class="form-check">
              <input
                checked
                class="form-check-input"
                id="login_remember"
                name="Remember_me"
                type="checkbox"
                value="y"
                v-model="rememberme"
              />
              <label class="form-check-label" for="Remember_me"
                >Remember Me</label
              >
            </div>
          </div>
        </div>

        <input
          class="btn btn-primary btn-block w-100"
          id="Submit"
          name="Submit"
          type="submit"
          value="Sign In"
        />
      </form>
      <p>
        <router-link
          class="link-offset-2 link-underline link-underline-opacity-0 link-underline-opacity-100-hover fw-bold"
          to="/register"
          >New? Register!</router-link
        >
      </p>

      <div v-if="error" class="alert alert-danger" role="alert">
        {{ error }}
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      usermail: "",
      password: "",
      rememberme: "",
      error: "",
    };
  },
  created() {
    document.title = "Login";
  },
  methods: {
    async login() {
      let axiosConfig = {
        headers: {
          "Access-Control-Allow-Origin": "*",
        },
      };
      axios
        .post(
          "http://localhost:5000/api/v1/login",
          {
            usermail: this.usermail,
            password: this.password,
            rememberme: this.rememberme,
          },
          axiosConfig
        )
        .then((res) => {
          console.log(res.data);
          localStorage.setItem("token", res.data.token);
          location.replace("/dashboard");
        })
        .catch((err) => {
          this.error = err.response.data.message;
        });
    },
  },
};
</script>
