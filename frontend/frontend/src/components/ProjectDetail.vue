<template>
  <div>
    <div class="container py-3"></div>
    <div class="container">
      <div class="row">
        <div v-if="error" class="alert alert-danger col-md-12" role="alert">
          {{ error }}
        </div>
        <div class="col-md-8" style="height: fit-content">
          <div class="card">
            <div class="card-body">
              <h3 class="card-title">
                <b>Project Name: </b>{{ project.Project_Name }}
                <a
                  href=""
                  class=""
                  style="font-size: small; text-decoration: none; color: grey"
                  title="Budget Analytics"
                >
                  $
                </a>
              </h3>
              <p class="card-text">
                <b>User Role: </b>
                <span v-if="user_type == 1">Project Admin</span>
                <span v-else-if="user_type == 2">Project Manager</span>
                <span v-else-if="user_type == 3">Project Maintainer</span>
              </p>
              <p class="card-text">
                <b>Description: </b>{{ project.Description }}
              </p>
              <p>
                <b>Project: </b>{{ project.Project_Status }} ({{
                  project.Project_Percentage
                }}%) |
                {{ project.Custom_Status }}
              </p>
              <p>
                <b>Budget</b> ₹{{ project.Project_Budget_Remaining }}
                <a title="Total Budget">(₹{{ project.Project_Budget }})</a>
              </p>
              <p><b>Date Created:</b> {{ project.Date_Created }}</p>
              <p><b>ETA: </b>{{ project.Project_Deadline }}</p>
              <div class="row">
                <div class="col-md-4">
                  <span v-if="user_type == 1">
                    <router-link
                      :to="`/editproject/${project.ID}`"
                      class="btn btn-info w-100"
                    >
                      Edit Project Details
                    </router-link>
                  </span>
                </div>
                <div class="col-md-4">
                  <span v-if="user_type == 1">
                    <router-link
                      :to="`/FinancialRecord/${project.ID}`"
                      class="btn btn-success w-100"
                    >
                      Create New Record
                    </router-link>
                  </span>
                </div>
                <div class="col-md-4">
                  <p style="text-align: right; color: gray; font-size: small">
                    <i><b>Tags: </b>{{ project.Project_Tags }}</i>
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
        <motion.div
          class="col-md-4"
          :initial="{ opacity: 0 }"
          :animate="{ opacity: 1 }"
        >
          <div
            class="card overflow-auto h-100"
            style="overflow: scroll; min-height: 300px; max-height: 600px"
          >
            <div class="card-body">
              <h4 class="text-center card-title"><b>Chat</b></h4>
              <div class="row">
                <div
                  v-if="!(recent_chat = false)"
                  style="
                    border-style: solid;
                    border-color: rgba(100, 0, 0, 0) rgba(100, 100, 100, 1)
                      rgba(50, 50, 50, 0.1) rgba(255, 0, 0, 0);
                  "
                  class="col-12"
                >
                  [System] No Recent Chats
                </div>
                <div v-else></div>
                <div class="col-12">
                  <form style="">
                    <div class="row g-2">
                      <div class="col-10">
                        <div class="input-group">
                          <input
                            type="text"
                            class="form-control"
                            placeholder="Enter Message"
                          />
                        </div>
                      </div>
                      <motion.div
                        class="col-2"
                        :while-hover="{ scale: 1.1 }"
                        :while-press="{ scale: 0.9 }"
                      >
                        <div class="input-group">
                          <input
                            class="btn btn-primary btn-block w-100"
                            id="Submit"
                            name="Submit"
                            type="submit"
                            value="➤"
                          />
                        </div>
                      </motion.div>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </motion.div>
        <div class="container py-3"></div>
        <div class="col-md-6">
          <div
            class="card overflow-auto h-100"
            style="overflow: scroll; min-height: 300px; max-height: 600px"
          >
            <div class="card-body">
              <h4 class="text-center card-title">
                <b>Users in Project</b>
              </h4>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { motion } from "motion-v";
</script>

<script>
import axios from "axios";

export default {
  name: "ProjectDetails",
  data() {
    return {
      project: {},
      recent_chat: {},
      ismember: false,
      user_type: "",
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
          this.error = err.response.data.error;
          console.log(err);
        })
        .finally((ress) => {
          console.log(ress);
        });

      axios
        .get(
          "http://localhost:5000/api/v1/user_role/"
            .concat(this.ProjectID)
            .concat("/"),
          {
            headers: {
              token: localStorage.getItem("token"),
            },
          }
        )
        .then((res) => {
          this.user_type = res.data.user_type;
        })
        .catch((err) => {
          this.error = err.response.data.error;
          console.log(err);
        })
        .finally((ress) => {
          console.log(ress);
        });
    },
  },
};
</script>
