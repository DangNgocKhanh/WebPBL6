<template>
  <div class="flex flex-col w-[100%] min-h-screen justify-between">
    <hea-der class="fixed" style="z-index: 999" />
    <router-view class="mt-[64px]" />
    <foo-ter />
  </div>
  <!-- Bảng đăng ki -->
  <div
    v-if="counter.bang_dang_nhap_dang_ki === 2"
    id="login-popup"
    tabindex="-1"
    class="bg-black/50 overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 h-full items-center justify-center flex"
  >
    <div class="relative p-4 w-full max-w-md h-full md:h-auto">
      <div class="relative bg-white rounded-lg shadow">
        <button
          v-on:click="counter.bang_dang_nhap_dang_ki = 1"
          type="button"
          class="absolute top-3 right-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center popup-close"
        >
          <svg
            aria-hidden="true"
            class="w-5 h-5"
            fill="#c6c7c7"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
              cliprule="evenodd"
            ></path>
          </svg>
          <span class="sr-only">Close popup</span>
        </button>

        <div class="p-5">
          <h3 class="text-2xl mb-0.5 font-medium"></h3>
          <p class="mb-4 text-sm font-normal text-gray-800"></p>

          <div class="text-center">
            <p class="mb-3 text-2xl font-semibold leading-5 text-slate-900">
              Đăng kí tài khoản
            </p>
            <!-- <p class="mt-2 text-sm leading-4 text-slate-600">
              Bạn phải đăng nhập để thực hiện hành động này.
            </p> -->
          </div>

          <!-- <div class="mt-7 flex flex-col gap-2">
            <button
              class="inline-flex h-10 w-full items-center justify-center gap-2 rounded border border-slate-300 bg-white p-2 text-sm font-medium text-black outline-none focus:ring-2 focus:ring-[#333] focus:ring-offset-1 disabled:cursor-not-allowed disabled:opacity-60"
            >
              <img
                src="https://www.svgrepo.com/show/512317/github-142.svg"
                alt="GitHub"
                class="h-[18px] w-[18px]"
              />
              Continue with GitHub
            </button>

            <button
              class="inline-flex h-10 w-full items-center justify-center gap-2 rounded border border-slate-300 bg-white p-2 text-sm font-medium text-black outline-none focus:ring-2 focus:ring-[#333] focus:ring-offset-1 disabled:cursor-not-allowed disabled:opacity-60"
            >
              <img
                src="https://www.svgrepo.com/show/475656/google-color.svg"
                alt="Google"
                class="h-[18px] w-[18px]"
              />Continue with Google
            </button>

            <button
              class="inline-flex h-10 w-full items-center justify-center gap-2 rounded border border-slate-300 bg-white p-2 text-sm font-medium text-black outline-none focus:ring-2 focus:ring-[#333] focus:ring-offset-1 disabled:cursor-not-allowed disabled:opacity-60"
            >
              <img
                src="https://www.svgrepo.com/show/448234/linkedin.svg"
                alt="Google"
                class="h-[18px] w-[18px]"
              />Continue with LinkedIn
            </button>
          </div> -->

          <div
            class="flex w-full items-center gap-2 py-6 text-sm text-slate-600"
          >
            <div class="h-px grow bg-slate-200"></div>
            THẾ GIỚI CÔNG NGHỆ
            <div class="h-px grow bg-slate-200"></div>
          </div>

          <div class="w-full">
            <input
              v-model="counter.dk.email"
              name="email"
              type="email"
              autocomplete="email"
              required=""
              class="block w-full rounded-lg border border-gray-300 px-3 py-2 shadow-sm outline-none placeholder:text-gray-400 focus:ring-2 focus:ring-black focus:ring-offset-1"
              placeholder="Email"
            />
            <input
              v-model="counter.dk.username"
              name="username"
              type="text"
              autocomplete="username"
              required=""
              class="mt-2 block w-full rounded-lg border border-gray-300 px-3 py-2 shadow-sm outline-none placeholder:text-gray-400 focus:ring-2 focus:ring-black focus:ring-offset-1"
              placeholder="Tài khoản đăng nhập"
            />
            <input
              v-model="counter.dk.password"
              name="password"
              type="password"
              autocomplete="current-password"
              required=""
              class="mt-2 mb-3 block w-full rounded-lg border border-gray-300 px-3 py-2 shadow-sm outline-none placeholder:text-gray-400 focus:ring-2 focus:ring-black focus:ring-offset-1"
              placeholder="Mật khẩu"
            />
            <!-- <p class="mb-3 mt-2 text-sm text-gray-500">
              <a
                href="/forgot-password"
                class="text-blue-800 hover:text-blue-600"
                >Đặt lại mật khẩu ?</a
              >
            </p> -->
            <button
              v-on:click="counter.dang_ki()"
              type="submit"
              class="inline-flex w-full items-center justify-center rounded-lg bg-black p-2 py-3 text-sm font-medium text-white outline-none focus:ring-2 focus:ring-black focus:ring-offset-1 disabled:bg-gray-400"
            >
              Tiếp tục
            </button>
          </div>

          <div class="mt-6 text-center text-sm text-slate-600">
            Bạn đã có tài khoản?
            <button
              v-on:click="counter.bang_dang_nhap_dang_ki = 3"
              class="font-medium text-[#4285f4]"
            >
              Đăng nhập
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- end bảng đăng kí -->
  <!-- Bảng đăng nhập -->
  <div
    v-if="counter.bang_dang_nhap_dang_ki === 3"
    id="login-popup"
    tabindex="-1"
    class="bg-black/50 overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 h-full items-center justify-center flex"
  >
    <div class="relative p-4 w-full max-w-md h-full md:h-auto">
      <div class="relative bg-white rounded-lg shadow">
        <button
          v-on:click="counter.bang_dang_nhap_dang_ki = 1"
          type="button"
          class="absolute top-3 right-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center popup-close"
        >
          <svg
            aria-hidden="true"
            class="w-5 h-5"
            fill="#c6c7c7"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
              cliprule="evenodd"
            ></path>
          </svg>
          <span class="sr-only">Close popup</span>
        </button>

        <div class="p-5">
          <h3 class="text-2xl mb-0.5 font-medium"></h3>
          <p class="mb-4 text-sm font-normal text-gray-800"></p>

          <div class="text-center">
            <p class="mb-3 text-2xl font-semibold leading-5 text-slate-900">
              Đăng nhập tài khoản
            </p>
            <!-- <p class="mt-2 text-sm leading-4 text-slate-600">
              Bạn phải đăng nhập để thực hiện hành động này.
            </p> -->
          </div>

          <!-- <div class="mt-7 flex flex-col gap-2">
            <button
              class="inline-flex h-10 w-full items-center justify-center gap-2 rounded border border-slate-300 bg-white p-2 text-sm font-medium text-black outline-none focus:ring-2 focus:ring-[#333] focus:ring-offset-1 disabled:cursor-not-allowed disabled:opacity-60"
            >
              <img
                src="https://www.svgrepo.com/show/512317/github-142.svg"
                alt="GitHub"
                class="h-[18px] w-[18px]"
              />
              Continue with GitHub
            </button>

            <button
              class="inline-flex h-10 w-full items-center justify-center gap-2 rounded border border-slate-300 bg-white p-2 text-sm font-medium text-black outline-none focus:ring-2 focus:ring-[#333] focus:ring-offset-1 disabled:cursor-not-allowed disabled:opacity-60"
            >
              <img
                src="https://www.svgrepo.com/show/475656/google-color.svg"
                alt="Google"
                class="h-[18px] w-[18px]"
              />Continue with Google
            </button>

            <button
              class="inline-flex h-10 w-full items-center justify-center gap-2 rounded border border-slate-300 bg-white p-2 text-sm font-medium text-black outline-none focus:ring-2 focus:ring-[#333] focus:ring-offset-1 disabled:cursor-not-allowed disabled:opacity-60"
            >
              <img
                src="https://www.svgrepo.com/show/448234/linkedin.svg"
                alt="Google"
                class="h-[18px] w-[18px]"
              />Continue with LinkedIn
            </button>
          </div> -->

          <div
            class="flex w-full items-center gap-2 py-6 text-sm text-slate-600"
          >
            <div class="h-px grow bg-slate-200"></div>
            THẾ GIỚI CÔNG NGHỆ
            <div class="h-px grow bg-slate-200"></div>
          </div>

          <div class="w-full">
            <input
              v-model="counter.lg.username"
              name="username"
              type="text"
              autocomplete="username"
              required=""
              class="block w-full rounded-lg border border-gray-300 px-3 py-2 shadow-sm outline-none placeholder:text-gray-400 focus:ring-2 focus:ring-black focus:ring-offset-1"
              placeholder="Tài khoản đăng nhập"
            />
            <input
              v-model="counter.lg.password"
              name="password"
              type="password"
              autocomplete="current-password"
              required=""
              class="mt-2 block w-full rounded-lg border border-gray-300 px-3 py-2 shadow-sm outline-none placeholder:text-gray-400 focus:ring-2 focus:ring-black focus:ring-offset-1"
              placeholder="Mật khẩu"
            />
            <p class="mb-3 mt-2 text-sm text-gray-500">
              <a
                href="/forgot-password"
                class="text-blue-800 hover:text-blue-600"
                >Đặt lại mật khẩu ?</a
              >
            </p>
            <button
              v-on:click="counter.dang_nhap()"
              class="inline-flex w-full items-center justify-center rounded-lg bg-black p-2 py-3 text-sm font-medium text-white outline-none focus:ring-2 focus:ring-black focus:ring-offset-1 disabled:bg-gray-400"
            >
              Tiếp tục
            </button>
          </div>

          <div class="mt-6 text-center text-sm text-slate-600">
            Bạn chưa có tài khoản?
            <button
              v-on:click="counter.bang_dang_nhap_dang_ki = 2"
              class="font-medium text-[#4285f4]"
            >
              Đăng kí
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- end bảng đăng nhập -->
</template>

<script>
// Import thành phần (components) NavBar, SideBar, FooterBar để sử dụng
import HeaDer from "@/components/HeaDer.vue";
import FooTer from "@/components/FooTer.vue";

import { useCounterStore } from "@/stores/counter";

// Để sử dụng được các thẻ (tag) của các component tương ứng
// <nav-bar />     -> component NavBar
// <side-bar />    -> component SideBar
// <footer-bar />  -> component FooterBar
// Chúng ta phải khai báo trong thuộc tính `components` của phần export default {}
export default {
  setup() {
    const counter = useCounterStore();
    return { counter };
  },
  filters: {
    formatCurrency(value) {
      // Sử dụng toLocaleString để định dạng số thành chuỗi với dấu phân tách hàng nghìn là dấu '.'
      return (
        value.toLocaleString("en-US", {
          minimumFractionDigits: 0,
          maximumFractionDigits: 0,
        }) + "₫"
      );
    },
  },
  mounted: function () {
    this.counter.F_danh_muc_danh_sach();
    this.counter.duy_tri_dang_nhap();
  },
  methods: {
    async F_all_user() {
      await this.counter.keep_login();
    },
  },
  components: {
    HeaDer,
    FooTer,
  },
};
</script>

<style>
body::-webkit-scrollbar {
  width: 14px;
  /* Chiều rộng vùng chứa scrollbar */
}

body::-webkit-scrollbar-track {
  background: #e5e7eb;
  /* Màu nền ngoài của thanh scrollbar */
}

body::-webkit-scrollbar-thumb {
  background-color: #bcbcbc;
  /* Màu của thanh cuộn (scroll thumb) */
  border-radius: 5px;
  /* Bo góc scroll thumb */
  /* border: 2px solid #ccc;  Không hỗ trợ padding, margin, transition nên dùng viền cùng màu nên để padding scroll thumb */
}

body::-webkit-scrollbar-thumb:hover {
  background-color: #bcbcbc;
  /* Hiệu ứng di chuột đổi màu*/
}

#slider2::-webkit-scrollbar {
  width: 6px;
  /* Chiều rộng vùng chứa scrollbar */
}

#slider2::-webkit-scrollbar-track {
  background: #f3f4f6;
  /* Màu nền ngoài của thanh scrollbar */
}

#slider2::-webkit-scrollbar-thumb {
  background-color: v-bind(cvb);
  /* Màu của thanh cuộn (scroll thumb) */
  border-radius: 5px;
  /* Bo góc scroll thumb */
  /* border: 2px solid #ccc;  Không hỗ trợ padding, margin, transition nên dùng viền cùng màu nên để padding scroll thumb */
}

#cjss::-webkit-scrollbar {
  width: 5px;
  height: 8px; /* Chiều rộng vùng chứa scrollbar */
}
#cjss::-webkit-scrollbar-track {
  background: #e0f2fe; /* Màu nền ngoài của thanh scrollbar */
}
#cjss::-webkit-scrollbar-thumb {
  background-color: #7dd3fc; /* Màu của thanh cuộn (scroll thumb) */
  border-radius: 5px; /* Bo góc scroll thumb */
  /* border: 2px solid #ccc;  Không hỗ trợ padding, margin, transition nên dùng viền cùng màu nên để padding scroll thumb */
}
#cjss::-webkit-scrollbar-thumb:hover {
  background-color: #e0f2fe; /* Hiệu ứng di chuột đổi màu*/
}
</style>
