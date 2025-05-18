<template>
  <div class="container">
    <div class="container py-3"></div>
    <div class="">
      <a type="button" class="btn btn-success col-12" href="/createproject">
        Create New Project
      </a>
    </div>
    <div class="container py-3"></div>
    <div v-if="!(Projects == false)">
      <div v-for="(project, index) in Projects" :key="index">
        <div class="card" style="width: 18rem">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <h6 class="card-subtitle mb-2 text-body-secondary">
              Card subtitle
            </h6>
            <p class="card-text">
              Some quick example text to build on the card title and make up the
              bulk of the card’s content.
            </p>
            <a href="#" class="card-link">Card link</a>
            <a href="#" class="card-link">Another link</a>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <div class="alert alert-info" role="alert">
        You are not in any Projects currently!
      </div>
    </div>

    <p v-if="error" style="color: red">{{ error }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "DashboardPage",
  data() {
    return {
      Projects: {},
      error: "",
    };
  },
  created() {
    document.title = "Projects";
  },
  mounted() {
    this.start();
  },
  methods: {
    start() {
      axios
        .get("http://localhost:5000/api/v1/listprojects", {
          headers: {
            token: localStorage.getItem("token"),
          },
        })
        .then((res) => {
          this.Projects = res.data.projects;
          console.log(this.Projects);
        })
        .catch((err) => {
          console.log(err);
          this.error = err.response.data.message;
        });
    },
  },
};
</script>
