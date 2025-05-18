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
            <router-link to="/login" class="nav-link">Login</router-link>
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
export default {
  name: "NavigationBar",
};
</script>
