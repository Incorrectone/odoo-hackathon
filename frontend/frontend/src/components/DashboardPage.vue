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
      <div class="row">
        <div v-for="(project, index) in Projects" :key="index" class="col-md-4">
          <div class="card">
            <div class="card-body">
              <h5 class="card-title">
                <b>Name: </b>{{ project.Project_Name }}
              </h5>
              <p class="card-text">
                <b>Description: </b>{{ project.Description }}
              </p>
              <p><b>Project: </b>{{ project.Project_Status }}</p>
              <p><b>Estimated Completed: </b>{{ project.Percentage }}</p>
              <p>
                {{ project.Date_Created }}
              </p>
              <router-link
                :to="`/project/${project.ID}`"
                class="btn btn-primary"
                >Project Page>></router-link
              >
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <div class="alert alert-info" role="alert">
        You are not in any Projects currently!
      </div>
    </div>

    <div v-if="error" class="alert alert-danger" role="alert">
      {{ error }}
    </div>
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
