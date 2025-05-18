<template>
  <nav
    class="navbar navbar-expand-lg bg-body-tertiary sticky-top"
    data-bs-theme="dark"
  >
    <div class="container">
      <router-link class="navbar-brand" to="/">
        <img src="http://localhost:8080/favicon.svg" alt="" width="35" />
        SynergySphere
      </router-link>

      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarScroll"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarScroll">
        <ul
          class="navbar-nav me-auto my-2 my-lg-0 navbar-nav-scroll"
          style="--bs-scroll-height: 100px"
        >
          <li class="nav-item">
            <router-link to="/" class="nav-link">Home</router-link>
          </li>

          <li class="nav-item dropdown" v-if="authenticated">
            <a
              class="nav-link dropdown-toggle"
              href="#"
              role="button"
              data-bs-toggle="dropdown"
            >
              {{ username }}
            </a>
            <ul class="dropdown-menu">
              <li>
                <router-link :to="`/dashboard`" class="dropdown-item"
                  >Projects</router-link
                >
              </li>
              <li>
                <router-link :to="`/tasks`" class="dropdown-item"
                  >Projects</router-link
                >
              </li>
              <li>
                <router-link :to="`/profile/${userID}`" class="dropdown-item"
                  >Profile</router-link
                >
              </li>
              <li v-if="isadmin">
                <a class="dropdown-item" href="/summary">Summary</a>
              </li>
              <li>
                <router-link to="/logout" class="dropdown-item"
                  >Logout</router-link
                >
              </li>
            </ul>
          </li>
          <li class="nav-item" v-else>
            <router-link :to="`/login`" class="nav-link">Login</router-link>
          </li>
        </ul>
        <!-- <form class="d-flex" method="GET" action="/services">
          <input
            class="form-control me-2"
            type="search"
            placeholder="Search Services"
            name="browse_services"
          />
          <button class="btn btn-outline-info" type="submit" name="search">
            Search
          </button>
        </form> -->
      </div>
    </div>
  </nav>
</template>

<script>
import axios from "axios";

export default {
  name: "NavigationBar",
  data() {
    return {
      authenticated: false,
      isadmin: false,
      userID: "",
      username: "",
    };
  },
  created() {
    this.isAuthenticated();
  },
  methods: {
    isAuthenticated() {
      if (!localStorage.getItem("token")) {
        this.authenticated = false;
      } else {
        axios
          .get("http://localhost:5000/api/v1/navdetail", {
            headers: {
              token: localStorage.getItem("token"),
            },
          })
          .then((res) => {
            this.userID = res.data.userID;
            this.username = res.data.username;
            this.authenticated = Boolean(res.data.authen);
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
  },
};
</script>
