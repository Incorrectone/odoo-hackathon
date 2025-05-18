<template>
  <div>
    <div class="container py-3"></div>
    <div class="container">
      <div class="row">
        <div class="col-md-4">
          <img
            :src="`http://localhost:5000/static/uploads/profilepics/${user.filename}.${user.ProfilePIC}`"
            class="rounded img-fluid"
            alt="(No Profile Picture Found)"
          />
          <div v-if="isowner">
            <form @submit.prevent="submitForm">
              <div class="row">
                <div class="col-12">
                  <label class="form-label" for="Profile_Pic"
                    >Enter Profile Picture</label
                  >
                  <input
                    class="form-control"
                    id="inputProfilePic"
                    name="Profile_Pic"
                    required
                    type="file"
                    ref="profileImage"
                  />
                  <div class="invalid-feedback">
                    Please enter a valid Profile Pic.
                  </div>
                </div>
                <div class="col-12">
                  <label></label>
                  <input
                    class="btn btn-primary btn-block w-100 col-12"
                    id="Submit"
                    name="Submit"
                    type="submit"
                    value="Upload Profile Picture"
                  />
                </div>
              </div>
              <p v-if="error">{{ error }}</p>
            </form>
          </div>
        </div>
        <div class="col-md-8">
          <div class="row">
            <h2></h2>
            <hr />

            <dt class="col-sm-3">Mail:</dt>
            <dd class="col-sm-9">
              <em
                ><a :href="`mailto:${user.Mail}`">{{ user.Mail }}</a></em
              >
            </dd>

            <dt class="col-sm-3">About Me:</dt>
            <dd class="col-sm-9">
              <p>
                <em>{{ user.About_Me }}</em>
              </p>
            </dd>

            <dt class="col-sm-3 text-end"></dt>
            <dd class="col-sm-9 text-end small">- {{ user.Date_Created }}</dd>
            <hr />
          </div>
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
      user: {},
      isowner: false,
      error: "",
    };
  },
  mounted() {
    this.start();
  },
  computed: {
    userId() {
      return this.$route.params.id;
    },
  },
  created() {
    document.title = "Profile Page";
  },
  methods: {
    start() {
      axios
        .get(
          "http://localhost:5000/api/v1/user/".concat(this.userId).concat("/"),
          {
            headers: {
              token: localStorage.getItem("token"),
            },
          }
        )
        .then((res) => {
          console.log(res.data);
          this.user = res.data.userinfo;
          this.isowner = res.data.ownership;
        })
        .catch((err) => {
          console.log(err);
        })
        .finally((ress) => {
          console.log(ress);
        });
    },
    submitForm() {
      const files = this.$refs.profileImage.files;
      const formData = new FormData();

      formData.append("files", files[0]);

      axios
        .put("http://localhost:5000/api/v1/uploadprofile", formData, {
          headers: {
            "content-type": "multipart/form-data",
            token: localStorage.getItem("token"),
          },
        })
        .then((response) => {
          this.error = response.data.message;
          console.log("Upload successful", response);
        })
        .catch((error) => {
          this.error = error.data;
          console.error("Upload error", error);
        });
    },
  },
};
</script>
