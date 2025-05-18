<template>
  <div>
    <div class="container py-3"></div>
    <div class="container">
      <div class="row">
        <div class="col-md-3">
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
            </div>
          </div>
        </div>
        <div class="col-md-9">
          <form @submit.prevent="submitForm" enctype="multipart/form-data">
            <h3>Add Maintainers:</h3>
            <div class="row">
              <div class="col-12">
                <label class="form-label" for="Service">Service</label>
                <select
                  class="form-control"
                  id="inputService"
                  name="Service"
                  v-model="newpeople.User_ID"
                >
                  <option
                    v-for="people in freepeople"
                    :key="people.ID"
                    :value="people.ID"
                  >
                    {{ people.Name }} [{{ people.ID }}]
                  </option>
                </select>
                <div class="invalid-feedback">Please Pick a Person.</div>
              </div>
              <br /><br />
              <div class="col-12">
                <label></label>
                <input
                  class="btn btn-primary btn-block w-100 col-12"
                  id="Submit"
                  name="Submit"
                  type="submit"
                  value="Book"
                />
              </div>
            </div>
          </form>
        </div>
        <div class="container py-3"></div>
        <div class="col-md-12">
          <h3>Already Assinged:</h3>
          <ol>
            <li v-for="(people, index) in already_as" :key="index">
              {{ people.Name }} || {{ people.Mail }}
            </li>
          </ol>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ProfilePage",
  data() {
    return {
      project: {},
      recent_chat: {},
      newpeople: {
        User_ID: "",
        Project_ID: "",
      },
      freepeople: {},
      already_as: {},
      ismember: false,
      error: "",
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
    document.title = "Project Detail";
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
          console.log(res.data);
          this.project = res.data.projectinfo;
          this.ismember = true;
        })
        .catch((err) => {
          console.log(err);
        })
        .finally((ress) => {
          console.log(ress);
        });

      axios
        .get(
          "http://localhost:5000/api/v1/listpeople/"
            .concat(this.ProjectID)
            .concat("/")
        )
        .then((res) => {
          console.log(res.data);
          this.freepeople = res.data.freepeople;
          this.already_as = res.data.already_as;
        })
        .catch((err) => {
          console.log(err);
        })
        .finally((ress) => {
          console.log(ress);
        });
    },
    submitForm() {
      this.newpeople.Project_ID = this.ProjectID;
      axios
        .put("http://localhost:5000/api/v1/addassignee/", this.newpeople, {
          headers: {
            token: localStorage.getItem("token"),
          },
        })
        .then((res) => {
          console.log(res.data);
        })
        .catch((err) => {
          console.log(err.data);
        });
    },
  },
};
</script>
