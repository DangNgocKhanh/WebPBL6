<template>
  <div class="w-[100%] bg-red-500 shadow-md">
    <nav class="bg-gray-800">
      <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
        <div class="relative flex h-16 items-center justify-between">
          <div class="absolute inset-y-0 left-0 flex items-center sm:hidden">
            <!-- Mobile menu button-->
            <button
              type="button"
              class="relative inline-flex items-center justify-center rounded-md p-2 text-gray-400 hover:bg-gray-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
              aria-controls="mobile-menu"
              aria-expanded="false"
            >
              <span class="absolute -inset-0.5"></span>
              <span class="sr-only">Open main menu</span>
              <!--
              Icon when menu is closed.
  
              Menu open: "hidden", Menu closed: "block"
            -->
              <svg
                class="block h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                aria-hidden="true"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"
                />
              </svg>
              <!--
              Icon when menu is open.
  
              Menu open: "block", Menu closed: "hidden"
            -->
              <svg
                class="hidden h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                aria-hidden="true"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M6 18L18 6M6 6l12 12"
                />
              </svg>
            </button>
          </div>
          <div
            class="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start"
          >
            <div class="flex flex-shrink-0 items-center">
              <img
                class="h-8 w-auto"
                src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500"
                alt="Your Company"
              />
            </div>
            <div class="hidden sm:ml-6 sm:block">
              <div class="flex space-x-4" style="font-size: 20px">
                <!-- Current: "bg-gray-900 text-white", Default: "text-gray-300 hover:bg-gray-700 hover:text-white" -->
                <a
                  href="/"
                  class="text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-sm font-medium"
                  :class="{
                    'bg-gray-900': counter.Path_Route.path === '/',
                  }"
                  >Trang chủ</a
                >
                <router-link
                  v-for="(i, index) in counter.danh_muc_danh_sach"
                  :to="'/loc/danh-muc/' + i.Name"
                  :key="index"
                  v-on:click="this.counter.F_loc_san_pham(i.Name, '', '')"
                  class="text-white rounded-md px-3 py-2 text-sm font-medium hover:bg-gray-700"
                  aria-current="page"
                  :class="{
                    'bg-gray-900': counter.Path_Route.path === i.Url,
                  }"
                  >{{ i.Name }}</router-link
                >
              </div>
            </div>
          </div>
          <div
            class="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0"
          >
            <!-- Search -->
            <div
              class="flex items-center justify-between px-2 py-1 rounded-full border-[1px] border-slate-600 text-white mr-2"
            >
              <input
                v-model="counter.khoa_tim_kiem_san_pham"
                placeholder="Tìm kiếm"
                class="bg-transparent outline-none border-none"
              />
              <router-link
                :to="'/tim-kiem/san-pham/' + counter.khoa_tim_kiem_san_pham"
              >
                <svg
                  v-on:click="counter.F_tim_kiem_san_pham()"
                  xmlns="http://www.w3.org/2000/svg"
                  height="16"
                  width="16"
                  viewBox="0 0 512 512"
                >
                  <path
                    fill="white"
                    d="M416 208c0 45.9-14.9 88.3-40 122.7L502.6 457.4c12.5 12.5 12.5 32.8 0 45.3s-32.8 12.5-45.3 0L330.7 376c-34.4 25.2-76.8 40-122.7 40C93.1 416 0 322.9 0 208S93.1 0 208 0S416 93.1 416 208zM208 352a144 144 0 1 0 0-288 144 144 0 1 0 0 288z"
                  />
                </svg>
              </router-link>
            </div>
            <!-- end search -->
            <!-- Cart -->
            <router-link
              :to="{ name: 'gio_hang' }"
              class="flex gap-1 items-center cursor-pointer"
            >
              <div
                class="rounded-full flex items-center justify-center border-gray-600 border-[1px] w-[34px] h-[34px] text-white"
              >
                {{
                  counter.gio_hang_chi_tiet
                    ? counter.gio_hang_chi_tiet.Cart_detail_Cart.length
                    : 0
                }}
              </div>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                height="25"
                viewBox="0 0 576 512"
              >
                <path
                  fill="white"
                  d="M0 24C0 10.7 10.7 0 24 0H69.5c22 0 41.5 12.8 50.6 32h411c26.3 0 45.5 25 38.6 50.4l-41 152.3c-8.5 31.4-37 53.3-69.5 53.3H170.7l5.4 28.5c2.2 11.3 12.1 19.5 23.6 19.5H488c13.3 0 24 10.7 24 24s-10.7 24-24 24H199.7c-34.6 0-64.3-24.6-70.7-58.5L77.4 54.5c-.7-3.8-4-6.5-7.9-6.5H24C10.7 48 0 37.3 0 24zM128 464a48 48 0 1 1 96 0 48 48 0 1 1 -96 0zm336-48a48 48 0 1 1 0 96 48 48 0 1 1 0-96z"
                />
              </svg>
            </router-link>
            <!-- End cart -->
            <!-- Icon login and register -->
            <!-- <button
                v-on:click="counter.bang_dang_nhap_dang_ki = 3"
                type="button"
                class="border-[1px] border-slate-700 py-1 px-2 flex justify-center items-center bg-slate-900 hover:bg-slate-800 focus:ring-gray-500 focus:ring-offset-red-200 text-white w-full transition ease-in duration-200 text-center text-base font-semibold shadow-md focus:outline-none focus:ring-2 focus:ring-offset-2 rounded-lg"
                style="font-size: 14px"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  height="18"
                  width="18"
                  viewBox="0 0 512 512"
                  style="margin-right: 8px"
                >
                  <path
                    fill="white"
                    d="M352 96l64 0c17.7 0 32 14.3 32 32l0 256c0 17.7-14.3 32-32 32l-64 0c-17.7 0-32 14.3-32 32s14.3 32 32 32l64 0c53 0 96-43 96-96l0-256c0-53-43-96-96-96l-64 0c-17.7 0-32 14.3-32 32s14.3 32 32 32zm-9.4 182.6c12.5-12.5 12.5-32.8 0-45.3l-128-128c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L242.7 224 32 224c-17.7 0-32 14.3-32 32s14.3 32 32 32l210.7 0-73.4 73.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0l128-128z"
                  />
                </svg>
                Login / Register
              </button> -->
            <!-- endicon -->
            <!-- Profile dropdown -->
            <div class="relative ml-3" v-if="counter.token">
              <div
                :title="counter.thong_tin_user.Name"
                v-on:click="
                  counter.thong_tin_tai_khoan = !counter.thong_tin_tai_khoan
                "
              >
                <button
                  type="button"
                  class="relative flex rounded-full bg-gray-800 text-sm focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800"
                  id="user-menu-button"
                  aria-expanded="false"
                  aria-haspopup="true"
                >
                  <span class="absolute -inset-1.5"></span>
                  <span class="sr-only">Open user menu</span>
                  <img
                    v-if="counter.thong_tin_user.Avatar"
                    class="h-8 w-8 rounded-full"
                    :src="
                      counter.Domain_Backend + counter.thong_tin_user.Avatar
                    "
                    alt=""
                  />
                  <img
                    v-else
                    class="h-8 w-8 rounded-full"
                    src="https://cdn-icons-png.flaticon.com/256/3899/3899618.png"
                    alt=""
                  />
                </button>
              </div>

              <!--
                Dropdown menu, show/hide based on menu state.
    
                Entering: "transition ease-out duration-100"
                  From: "transform opacity-0 scale-95"
                  To: "transform opacity-100 scale-100"
                Leaving: "transition ease-in duration-75"
                  From: "transform opacity-100 scale-100"
                  To: "transform opacity-0 scale-95"
              -->
              <div
                v-show="counter.thong_tin_tai_khoan"
                class="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none"
                role="menu"
                aria-orientation="vertical"
                aria-labelledby="user-menu-button"
                tabindex="-1"
              >
                <router-link
                  :to="{ name: 'thong_tin_tai_khoan' }"
                  v-on:click="
                    counter.thong_tin_tai_khoan = !counter.thong_tin_tai_khoan
                  "
                  class="block px-4 py-2 text-sm text-gray-700"
                  role="menuitem"
                  tabindex="-1"
                  id="user-menu-item-0"
                  >Thông tin tài khoản</router-link
                >
                <router-link
                  :to="{ name: 'don-hang-da-dat' }"
                  v-on:click="
                    counter.thong_tin_tai_khoan = !counter.thong_tin_tai_khoan
                  "
                  class="block px-4 py-2 text-sm text-gray-700"
                  role="menuitem"
                  tabindex="-1"
                  id="user-menu-item-0"
                  >Xem các đơn hàng đã đặt</router-link
                >
                <a
                  v-on:click="counter.dang_xuat()"
                  href="#"
                  class="block px-4 py-2 text-sm text-gray-700"
                  role="menuitem"
                  tabindex="-1"
                  id="user-menu-item-1"
                  >Đăng xuất</a
                >
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Mobile menu, show/hide based on menu state. -->
      <div class="sm:hidden" id="mobile-menu">
        <div class="space-y-1 px-2 pb-3 pt-2">
          <!-- Current: "bg-gray-900 text-white", Default: "text-gray-300 hover:bg-gray-700 hover:text-white" -->
          <a
            href="#"
            class="bg-gray-900 text-white block rounded-md px-3 py-2 text-base font-medium"
            aria-current="page"
            >Dashboard</a
          >
          <a
            href="#"
            class="text-gray-300 hover:bg-gray-700 hover:text-white block rounded-md px-3 py-2 text-base font-medium"
            >Team</a
          >
          <a
            href="#"
            class="text-gray-300 hover:bg-gray-700 hover:text-white block rounded-md px-3 py-2 text-base font-medium"
            >Projects</a
          >
          <a
            href="#"
            class="text-gray-300 hover:bg-gray-700 hover:text-white block rounded-md px-3 py-2 text-base font-medium"
            >Calendar</a
          >
        </div>
      </div>
    </nav>
  </div>
</template>
<script>
import { useCounterStore } from "@/stores/counter";
import axios from "axios";
import VueCookies from "vue-cookies";

export default {
  setup() {
    const counter = useCounterStore();
    return { counter };
  },
  mounted: function () {},
  // destroyed () {
  // document.body.classList.remove('overflow-hidden')
  // },
  methods: {},
};
</script>
<style>
.main-mn {
}
.main-mn .megaparent {
  position: unset !important;
}
.main-mn .w-100,
.main-mn .megaparent > .sub-menu {
  position: absolute;
  left: 0;
  top: 56px;
  z-index: 100;
  background: url("https://viettelpost.com.vn/wp-content/themes/viettel/assets/images/bg_mega_nav.png")
    no-repeat #fff;
  background-position: 85% 100%;
  background-size: auto 50%;
  display: flex;
  width: 100%;
  border-top: 1px solid #ee0033;
  border-bottom: 2px solid #ee0033;
}
.main-mn .mega {
  width: 25%;
  padding: 29px 20px 20px 20px;
  display: unset;
  border-right: 1px solid #dcdadb;
}

.main-mn .mega > a {
  font-size: 15px;
  color: #000;
  font-weight: 600;
}

.main-mn .mega,
.main-mn .mega a {
  margin: 0;
  border-bottom: none;
  line-height: 35px;
}
.main-mn .mega li a {
  font-size: 14px;
}
.main-mn .mega li {
  width: 100%;
}
.main-mn .mega ul {
  border-radius: none;
  position: unset;
  width: 100%;
  position: relative;
  left: unset;
  top: unset;
  padding-top: 15px;
  background: transparent;
}
.main-mn .mega ul:before {
  content: "";
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  width: 25px;
  height: 2px;
  background: #ee0033;
}
.main-mn .mega .mega_more a {
  color: #ee0033;
  float: left;
  line-height: 15px;
  border-bottom: 1px solid #ee0033;
}
.megaparent > .sub-menu {
  display: flex !important;
  width: 100%;
}
</style>
