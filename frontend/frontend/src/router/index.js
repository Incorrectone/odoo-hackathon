import { createRouter, createWebHistory } from "vue-router";

import LandingPage from "@/components/LandingPage.vue";
import LoginPage from "@/components/LoginPage.vue";
import RegisterPage from "@/components/RegisterPage.vue";
import DashboardPage from "@/components/DashboardPage.vue";

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
    path: "/FinancialRecord/:id",
    name: "FinancialRecord",
    component: () => import("../components/FinancialRecord.vue"),
  },
  {
    path: "/project/:id",
    name: "ProjectDetail",
    component: () => import("../components/ProjectDetail.vue"),
  },
  {
    path: "/editproject/:id",
    name: "EditProject",
    component: () => import("../components/EditProject.vue"),
  },
  {
    path: "/createproject",
    name: "CreateProject",
    component: () => import("../components/CreateProject.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
