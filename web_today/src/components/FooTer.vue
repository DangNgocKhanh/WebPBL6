<template>
  <div class="w-[100%]" style="box-shadow: 0 -5px 10px rgba(0, 0, 0, 0.1)">
    <footer class="mx-auto max-w-7xl px-3 pt-4 lg:px-9">
      <div class="grid gap-10 row-gap-6 mb-8 sm:grid-cols-2 lg:grid-cols-4">
        <div class="sm:col-span-2">
          <a href="#" class="inline-flex items-center">
            <img
              src="https://mcqmate.com/public/images/logos/60x60.png"
              alt="logo"
              class="h-8 w-8"
            />
            <span class="ml-2 text-xl font-bold tracking-wide text-gray-800"
              >Thế giới đồ Công nghệ</span
            >
          </a>
          <div class="mt-6 lg:max-w-xl">
            <p class="text-sm text-gray-800">
              Chuyên cung cấp các sản phẩm và đồ công nghệ liên quan.Chính sách
              bảo hành uy tín chất lượng.
            </p>
          </div>
        </div>

        <div class="flex flex-col gap-2 text-sm">
          <p class="text-base font-bold tracking-wide text-gray-900">
            Thông tin và chính sách
          </p>
          <a href="#">Mua hàng và thanh toán onile</a>
          <a href="#">Mua hàng trả góp onile</a>
          <a href="#">Xem ưu đãi</a>
          <p class="text-base font-bold tracking-wide text-gray-900">
            Dịch vụ khác
          </p>
          <a href="#">Khách hàng và Doanh nghiệp</a>
          <a href="#">Ưu đãi thanh toán</a>
          <a href="#">Quy chế hoạt động</a>
        </div>

        <div>
          <p class="text-base font-bold tracking-wide text-gray-900">
            Công ty có sẵn
          </p>
          <div class="flex items-center gap-1 px-2">
            <a href="#" class="w-full min-w-xl">
              <img
                src="https://mcqmate.com/public/images/icons/playstore.svg"
                alt="Playstore Button"
                class="h-10"
              />
            </a>
            <a
              class="w-full min-w-xl"
              href="https://www.youtube.com/channel/UCo8tEi6SrGFP8XG9O0ljFgA"
            >
              <img
                src="https://mcqmate.com/public/images/icons/youtube.svg"
                alt="Youtube Button"
                class="h-28"
              />
            </a>
          </div>
          <p class="text-base font-bold tracking-wide text-gray-900">Liên hệ</p>
          <div class="flex">
            <p class="mr-1 text-gray-800">Email:</p>
            <a href="#" title="send email">thegioicongnghe@company.com</a>
          </div>
        </div>
      </div>

      <div
        class="flex flex-col-reverse justify-between pt-5 pb-10 border-t lg:flex-row"
      >
        <p class="text-sm text-gray-600">
          © Copyright 2023 Company. All rights reserved.
        </p>
        <ul
          class="flex flex-col mb-3 space-y-2 lg:mb-0 sm:space-y-0 sm:space-x-5 sm:flex-row"
        >
          <li>
            <a
              href="#"
              class="text-sm text-gray-600 transition-colors duration-300 hover:text-deep-purple-accent-400"
              >Privacy &amp; Cookies Policy
            </a>
          </li>
          <li>
            <a
              href="#"
              class="text-sm text-gray-600 transition-colors duration-300 hover:text-deep-purple-accent-400"
              >Disclaimer
            </a>
          </li>
        </ul>
      </div>
    </footer>
  </div>
</template>
<script>
import { useCounterStore } from "@/stores/counter";
import axios from "axios";
import VueCookies from "vue-cookies";

export default {
  data() {
    return {
      cvb: "#E5E7EB",
    };
  },
  setup() {
    const counter = useCounterStore();
    return { counter };
  },
  mounted: function () {},
  methods: {
    async Follow(aa) {
      await this.counter.Follow_user(aa);
      this.counter.List_follow();
      this.counter.List_un_follow();
    },
    async F_FFF() {
      this.counter.xacnhan = 1;
      await this.counter.F_add_hair();
      this.counter.F_user_hair();
      this.counter.xacnhan = 2;
    },
  },
};
</script>

<style>
#slider::-webkit-scrollbar {
  width: 6px; /* Chiều rộng vùng chứa scrollbar */
}
#slider::-webkit-scrollbar-track {
  background: #f3f4f6; /* Màu nền ngoài của thanh scrollbar */
}
#slider::-webkit-scrollbar-thumb {
  background-color: v-bind(cvb); /* Màu của thanh cuộn (scroll thumb) */
  border-radius: 5px; /* Bo góc scroll thumb */
  /* border: 2px solid #ccc;  Không hỗ trợ padding, margin, transition nên dùng viền cùng màu nên để padding scroll thumb */
}
</style>
<style>
.social-chat li {
  margin: 5px 0;
}
.social-chat li a.o {
  padding-bottom: 0;
}
.social-chat li a {
  display: block;
  padding: 5px;
  transition: display ease 0.5s;
  cursor: pointer;
}
.social-chat li a:not(.o) {
  display: none;
}
.shadow {
  position: fixed;
  left: 0;
  right: 0;
  width: 100%;
  top: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 9991;
}
#popup_vipo {
  display: none;
  justify-content: center;
  align-items: center;
}
#popup_vipo .wrapper {
  max-width: 432px;
  border-radius: 5px;
  position: relative;
}
#popup_vipo img {
  max-width: 100%;
}
.close {
  position: absolute;
  right: -20px;
  top: -15px;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  opacity: 1;
  z-index: 9999;
  cursor: pointer;
}
</style>
