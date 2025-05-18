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
        @submit.prevent="createproject"
      >
        <h2>Create Project</h2>
        <hr />

        <div class="input-group mb-3">
          <span class="input-group-text" id="basic-addon1">Project Name:</span>
          <input
            type="text"
            v-model="formData.Project_Name"
            class="form-control"
            placeholder="Project-001"
            aria-label="Username"
            aria-describedby="basic-addon1"
            id="Project_Name"
            name="Project_Name"
          />
        </div>

        <div class="input-group">
          <span class="input-group-text">Description</span>
          <textarea
            class="form-control"
            aria-label="With textarea"
            id="Description"
            v-model="formData.Description"
            name="Description"
          ></textarea>
        </div>
        <br />
        <input
          class="btn btn-primary btn-block w-100"
          id="Submit"
          name="Submit"
          type="submit"
          value="Create"
        />
      </form>

      <p v-if="error" style="color: red">{{ error }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      formData: {
        Project_Name: "",
        Description: "",
      },
      error: "",
    };
  },
  created() {
    document.title = "Create Project";
  },
  methods: {
    async createproject() {
      let axiosConfig = {
        headers: {
          "Access-Control-Allow-Origin": "*",
          token: localStorage.getItem("token"),
        },
      };
      axios
        .post(
          "http://localhost:5000/api/v1/createproject",
          this.formData,
          axiosConfig
        )
        .then((res) => {
          console.log(res.data);
          location.replace("/dashboard");
        })
        .catch((err) => {
          this.error = err.response.data.message;
        });
    },
  },
};
</script>
