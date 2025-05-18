import Vue from "vue";
import VueRouter from "vue-router";

import LandingPage from "@/components/LandingPage.vue";
import LoginPage from "@/components/LoginPage.vue";
import RegisterPage from "@/components/RegisterPage.vue";
import DashboardPage from "@/components/DashboardPage.vue";

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
    path: "/dashboard",
    name: "DashboardPage",
    component: DashboardPage,
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
  {
    path: "/project/:id",
    name: "ProjectDetail",
    component: () => import("../components/ProjectDetail.vue"),
  },
  {
    path: "/createproject",
    name: "CreateProject",
    component: () => import("../components/CreateProject.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
