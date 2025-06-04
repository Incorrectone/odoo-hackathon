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

        <div class="row">
          <div class="col-md-8">
            <div class="input-group">
              <span class="input-group-text" id="basic-addon1"
                >Project Name</span
              >
              <input
                type="text"
                v-model="formData.Project_Name"
                class="form-control"
                placeholder="Project-001"
                aria-label="Project Name"
                id="Project_Name"
                name="Project_Name"
                required
              />
              <div class="invalid-feedback">Please enter a valid Name.</div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="input-group">
              <span class="input-group-text" id="basic-addon1">Estimate</span>
              <input
                type="number"
                v-model="formData.Project_Percentage"
                class="form-control"
                placeholder="Project-001"
                aria-label="Project Estimate"
                required
              />
              <div class="invalid-feedback">Please enter a valid Name.</div>
            </div>
          </div>
          <p></p>

          <div class="col-md-6">
            <div class="input-group">
              <span class="input-group-text">Deadline</span>
              <input
                type="date"
                class="form-control"
                :min="min_Date"
                v-model="formData.Project_Deadline"
                required
              />
              <div class="input-group-addon">
                <span class="glyphicon glyphicon-th"></span>
              </div>
            </div>
          </div>

          <div class="col-md-6">
            <div class="input-group">
              <span class="input-group-text" id="basic-addon1"
                >Project Budget</span
              >
              <input
                type="text"
                v-model="formData.Project_Budget"
                class="form-control"
                aria-label="Project Budget"
                required
              /><span class="input-group-text" id="basic-addon2">₹</span>
              <div class="invalid-feedback">Please enter a Valid Budget.</div>
            </div>
          </div>

          <p></p>
          <div class="col-md-12">
            <div class="input-group">
              <span class="input-group-text" id="basic-addon1">Tags:</span>
              <input
                type="text"
                v-model="formData.Project_Tags"
                class="form-control"
                placeholder="C++, Python, Vue.JS..."
                aria-label="Project Tags"
                required
              />
              <div class="invalid-feedback">Please enter Tags.</div>
            </div>
          </div>
          <p></p>

          <div class="col-md-12">
            <div class="input-group">
              <span class="input-group-text" id="basic-addon1"
                >Custom Status:</span
              >
              <input
                type="text"
                v-model="formData.Custom_Status"
                class="form-control"
                aria-label="Project Status"
                required
              />
              <div class="invalid-feedback">Please enter a Status.</div>
            </div>
          </div>
          <p></p>

          <div class="col-md-12">
            <div class="input-group">
              <span class="input-group-text">Description</span>
              <textarea
                class="form-control"
                aria-label="With textarea"
                id="Description"
                v-model="formData.Description"
                name="Description"
                required
              ></textarea>
            </div>
          </div>
          <p></p>

          <div class="col-12">
            <input
              class="btn btn-primary btn-block w-100"
              id="Submit"
              name="Submit"
              type="submit"
              value="Create"
            />
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
  data() {
    return {
      formData: {
        Project_Name: "",
        Description: "",
        Project_Budget: 0,
        Project_Tags: "",
        Project_Deadline: "",
        Custom_Status: "Actively Hiring!",
        Project_Percentage: 0,
      },
      min_Date: new Date().toISOString().split("T")[0],
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
