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
              <h5 class="card-title">
                <b>Name: </b>{{ project.Project_Name }}
              </h5>
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
                <a data-bs-toggle="tooltip" data-bs-title="Default tooltip"
                  >(₹{{ project.Project_Budget }})</a
                >
              </p>
              <p><b>Date Created:</b> {{ project.Date_Created }}</p>
              <p><b>ETA: </b>{{ project.Project_Deadline }}</p>
              <p style="text-align: right; color: gray; font-size: small">
                <i><b>Tags: </b>{{ project.Project_Tags }}</i>
              </p>
            </div>
          </div>
        </div>
        <motion.div
          class="col-md-4"
          :initial="{ opacity: 0 }"
          :animate="{ opacity: 1 }"
        >
          <div
            class="card h-100 overflow-auto"
            style="overflow: scroll; min-height: 300px; max-height: 600px"
          >
            <div class="card-body">
              <h5 class="card-title text-center">
                <b>Chat </b>
                <p>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                  Nullam pharetra massa eu libero bibendum, non placerat elit
                  ullamcorper. Duis id ornare sem, eu facilisis justo. Nulla
                  risus turpis, suscipit vitae dolor ac, finibus pellentesque
                  diam. Vestibulum ut condimentum est. Quisque rhoncus elit ac
                  tincidunt sollicitudin. Proin sit amet ipsum sed ligula
                  sollicitudin accumsan nec sit amet ex. Phasellus faucibus
                  pretium purus, eget eleifend risus interdum vitae. Quisque
                  lacinia eget ipsum nec aliquet. Curabitur id consectetur urna,
                  ac fringilla erat. Donec finibus egestas ullamcorper. Lorem
                  ipsum dolor sit amet, consectetur adipiscing elit. Cras ornare
                  ligula sed augue posuere, eu pulvinar neque efficitur.
                  Phasellus at dignissim eros. Nullam scelerisque nec justo
                  viverra euismod. Proin non suscipit magna, vel commodo libero.
                  Fusce sapien ante, sagittis ac lectus sit amet, porttitor
                  lacinia leo. Curabitur consectetur dapibus metus eu accumsan.
                  Nullam ut blandit odio. Class aptent taciti sociosqu ad litora
                  torquent per conubia nostra, per inceptos himenaeos. Ut
                  ultrices mauris felis, et dignissim nibh rutrum vel. Donec
                  pulvinar rutrum justo eget fringilla. Nunc a erat sodales,
                  molestie justo in, lobortis massa. Etiam tincidunt massa non
                  facilisis bibendum. Suspendisse gravida mi dui, at porttitor
                  odio tempus in. Nullam elementum felis sit amet ante
                  consequat, eget vulputate mi porttitor. Mauris consectetur
                  porta mauris, in dapibus mi pharetra non. Duis a quam id magna
                  consectetur tincidunt eget sed elit. Mauris sit amet ligula
                  velit. Donec sem dolor, ornare ut sapien sit amet, varius
                  tincidunt ante. Phasellus euismod, tellus in feugiat
                  elementum, lectus mi aliquam magna, vel blandit turpis justo
                  at felis. Morbi dignissim sem a congue commodo. Quisque eros
                  erat, egestas et finibus non, suscipit at augue. Nullam
                  tincidunt lectus eu odio rhoncus egestas. Morbi dictum mauris
                  id lacus luctus malesuada. Curabitur diam turpis, commodo eu
                  ex at, venenatis finibus leo. Suspendisse quis arcu eu diam
                  pulvinar facilisis. Aliquam a purus mattis, molestie arcu
                  quis, interdum quam. In vel sapien metus. Ut molestie
                  imperdiet magna, quis elementum nulla. Nulla sagittis gravida
                  metus. Aliquam erat volutpat. Vestibulum ullamcorper nisi et
                  ipsum convallis accumsan. Pellentesque varius dolor vitae
                  finibus ultricies. Mauris risus nunc, interdum sed iaculis at,
                  ullamcorper non est. Vestibulum finibus pulvinar hendrerit.
                  Pellentesque habitant morbi tristique senectus et netus et
                  malesuada fames ac turpis egestas. Nulla consectetur nisl non
                  tincidunt condimentum. Suspendisse quis lorem eget dui
                  pellentesque sollicitudin et quis orci. Quisque ac tellus in
                  nulla vehicula commodo a ac est. Aenean nulla eros, ultricies
                  quis congue eu, vestibulum a nulla. Nullam est nunc, lacinia
                  eu ultrices at, luctus vitae ligula. Maecenas eu lorem
                  tristique, placerat dui at, feugiat justo. Nam bibendum
                  sagittis mauris, et pharetra massa cursus vel. Etiam aliquet
                  et leo eleifend laoreet. Donec ipsum ligula, posuere sit amet
                  gravida sit amet, rhoncus eget velit.
                </p>
              </h5>
            </div>
          </div>
        </motion.div>
        <div class="container py-3"></div>
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
    },
  },
};
</script>
