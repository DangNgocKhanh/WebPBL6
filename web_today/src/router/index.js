import { createRouter, createWebHistory } from "vue-router";
import HomeLayout from "../layouts/HomeLayout.vue";
// import ProductLayout from "../layouts/ProductLayout.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      redirect: "/",
      component: HomeLayout,
      children: [
        {
          path: "/",
          component: () => import("../views/HomeView.vue"),
        },
        {
          path: "/:url",
          component: () => import("../views/HomeView.vue"),
        },
        {
          path: "/chi-tiet/:url",
          name: 'chi_tiet',
          component: () => import("../views/DetailView.vue"),
        },
        {
          path: "/gio-hang/",
          name: 'gio_hang',
          component: () => import("../views/CartView.vue"),
        },
        {
          path: "/thong-tin-tai-khoan/",
          name: 'thong_tin_tai_khoan',
          component: () => import("../views/InforView.vue"),
        },
        {
          path: "/don-hang-da-dat/",
          name: 'don-hang-da-dat',
          component: () => import("../views/OderView.vue"),
        },
        {
          path: "/loc/danh-muc/:url",
          name: 'loc-danh-muc',
          component: () => import("../views/FilterView.vue"),
        },
        {
          path: "/loc/quoc-gia/:url",
          name: 'loc-quoc-gia',
          component: () => import("../views/MadeView.vue"),
        },
        {
          path: "/loc/thuong-hieu/:url",
          name: 'loc-thuong-hieu',
          component: () => import("../views/TrameView.vue"),
        },
        {
          path: "/tim-kiem/san-pham/:url",
          name: 'tim-kiem-san-pham',
          component: () => import("../views/SearchView.vue"),
        },
      ],
    },
    // {
    //   path: "/",
    //   name: "loginregister",
    //   redirect: "/",
    //   component: LoginRegister,
    //   children: [
    //     {
    //       path: "/dang-nhap",
    //       component: () => import("../views/LoginRegister/LoginView.vue"),
    //     },
    //     {
    //       path: "/dang-ki",
    //       component: () => import("../views/LoginRegister/RegisterView.vue"),
    //     },
    //   ]
    // },
  ],
  scrollBehavior() {
    window.scrollTo(0, 0);
  },
});

export default router;
