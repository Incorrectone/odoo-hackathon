import Vue from "vue";
import VueRouter from "vue-router";

import LandingPage from "@/components/LandingPage.vue";
import LoginPage from "@/components/LoginPage.vue";
import RegisterPage from "@/components/RegisterPage.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "LandingPage",
    component: LandingPage,
  },
  {
    path: "/login",
    name: "LoginPage",
    component: LoginPage,
  },
  {
    path: "/register",
    name: "RegisterPage",
    component: RegisterPage,
  },
  {
    path: "/logout",
    name: "LogoutPage",
    component: () => import("../components/LogoutPage.vue"),
  },
  {
    path: "/profile/:id",
    name: "ProfilePage",
    component: () => import("../components/ProfilePage.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
