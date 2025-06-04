<template>
  <div>
    <div class="container py-3"></div>
    <div v-if="error" class="alert alert-danger col-md-12" role="alert">
      {{ error }}
    </div>
    <div
      class="container col-md-5 bg-body-tertiary shadow p-5 border border-2 rounded border-dark"
      style="--bs-border-opacity: 0.5; --bs-bg-opacity: 0.05"
    >
      <form @submit.prevent="editproject" class="">
        <h1>Edit Project</h1>
        <hr />
        <div class="row g-2">
          <div class="col-md-8">
            <div class="input-group">
              <span class="input-group-text" id="basic-addon1"
                >Project Name</span
              >
              <input
                type="text"
                v-model="formData.Project_Name"
                class="form-control"
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
                type="text"
                v-model="formData.Project_Percentage"
                class="form-control"
                placeholder="Project-001"
                aria-label="Project Estimate"
                max="100"
                min="0"
                required
              />
              <div class="invalid-feedback">Please enter a valid Name.</div>
            </div>
          </div>
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
                >Project Status</span
              >
              <select
                class="form-select"
                aria-label="Large select example"
                v-model="formData.Project_Status"
              >
                <option value="Incomplete">Incomplete</option>
                <option value="On Hold">On Hold</option>
                <option value="Completed">Completed</option>
              </select>
              <div class="invalid-feedback">Please enter a valid Name.</div>
            </div>
          </div>
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

          <div class="col-12">
            <input
              class="btn btn-primary btn-block w-100"
              id="Submit"
              name="Submit"
              type="submit"
              value="Edit"
            />
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "EditProject",
  data() {
    return {
      error: "",
      formData: {
        Project_Name: "",
        Project_Status: "",
        Project_Percentage: "",
        Custom_Status: "",
        Project_Deadline: "",
        Project_Tags: "",
        Description: "",
      },
    };
  },
  mounted() {
    this.start();
  },
  computed: {
    ProjectID() {
      return this.$route.params.id;
    },
  },
  created() {
    document.title = "Edit Project Details";
  },
  methods: {
    start() {
      axios
        .get(
          "http://localhost:5000/api/v1/project/"
            .concat(this.ProjectID)
            .concat("/"),
          {
            headers: {
              token: localStorage.getItem("token"),
            },
          }
        )
        .then((res) => {
          this.formData.Project_Name = res.data.projectinfo.Project_Name;
          this.formData.Project_Status = res.data.projectinfo.Project_Status;
          this.formData.Project_Percentage =
            res.data.projectinfo.Project_Percentage;
          this.formData.Custom_Status = res.data.projectinfo.Custom_Status;
          this.formData.Project_Deadline = new Date(
            res.data.projectinfo.Project_Deadline
          )
            .toISOString()
            .slice(0, 10);
          this.formData.Project_Tags = res.data.projectinfo.Project_Tags;
          this.formData.Description = res.data.projectinfo.Description;
        })
        .catch((err) => {
          this.error = err.response.data.error;
          console.log(err);
        })
        .finally((ress) => {
          console.log(ress);
        });
    },
    editproject() {
      axios
        .post(
          "http://localhost:5000/api/v1/editproject/"
            .concat(this.ProjectID)
            .concat("/"),
          this.formData,
          {
            headers: {
              token: localStorage.getItem("token"),
            },
          }
        )
        .then((response) => {
          this.error = response.data.message;
          location.replace("/project/".concat(this.ProjectID).concat("/"));
        })
        .catch((error) => {
          this.error = error.response.data.message;
          console.error("Registration error:", error);
        });
    },
  },
};
</script>
