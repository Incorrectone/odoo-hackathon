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
      <form @submit.prevent="createrecord" class="">
        <h1>Create New Record</h1>
        <hr />
        <div class="row g-2">
          <div class="col-md-8">
            <div class="input-group">
              <span class="input-group-text" id="basic-addon1">Reason</span>
              <input
                type="text"
                v-model="formData.Reason"
                class="form-control"
                aria-label="Record Reason"
                id="Record Reason"
                required
              />
              <div class="invalid-feedback">Please enter a valid Name.</div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="input-group">
              <span class="input-group-text" id="basic-addon1"
                >Expense Type</span
              >
              <select
                class="form-select"
                aria-label="Additon"
                v-model="formData.Type"
              >
                <option value="0" selected>Budget Increment</option>
                <option value="1">Expense</option>
              </select>
              <div class="invalid-feedback">Please enter a valid Name.</div>
            </div>
          </div>
          <div class="input-group">
            <span class="input-group-text" id="basic-addon1">Amount</span>
            <input
              type="text"
              v-model="formData.Amount"
              class="form-control"
              aria-label="Amount"
              id="Record Amount"
              required
            />
          </div>
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
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "FinancialRecord",
  data() {
    return {
      error: "",
      formData: {
        Type: "",
        Amount: "",
        Reason: "",
      },
    };
  },
  mounted() {},
  methods: {
    createrecord() {
      axios
        .post(
          "http://localhost:5000/api/v1/financialrecord/"
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
  computed: {
    ProjectID() {
      return this.$route.params.id;
    },
  },
  created() {
    document.title = "Edit Project Details";
  },
};
</script>
