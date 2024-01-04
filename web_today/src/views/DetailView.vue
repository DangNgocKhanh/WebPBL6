<template>
  <div class="flex w-[100%] grow min-h-screen">
    <div class="flex flex-col bg-white mx-auto max-w-7xl grow px-3 py-2">
      <h2 class="font-bold text-[22px] py-2">
        {{ counter.san_pham_chi_tiet.Name }}
      </h2>
      <div class="flex gap-4 w-full mt-2">
        <div class="flex flex-col gap-2 w-[50%]">
          <div
            class="flex justify-center items-center w-full h-[398px] rounded-md border-[1px] border-gray-[#e5e7eb] px-2 py-2"
          >
            <img :src="counter.san_pham_chi_tiet.Avatar" class="h-full" />
          </div>
          <!-- <div class="w-full">
            <img
              src="https://cdn2.cellphones.com.vn/insecure/rs:fill:58:58/q:80/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone_13_128gb_-_5_1_.png"
              class="w-[52px] h-[52px] rounded-md border-[1px] border-gray-[#e5e7eb]"
            />
          </div> -->
        </div>
        <div
          class="flex flex-col gap-2 h-[398px] w-[50%] rounded-md border-[1px] border-gray-[#e5e7eb] px-2 py-2"
        >
          <h2 class="w-full font-bold text-[20px]">Thông tin sản phẩm</h2>
          <div class="formatted-text w-full">
            {{ counter.san_pham_chi_tiet.Describe }}
          </div>
        </div>
        <!-- <div class="flex flex-col gap-2 w-[50%]">
          <div
            class="flex flex-col w-full h-[200px] rounded-md border-[1px] border-gray-[#e5e7eb]"
          >
            <div
              class="flex gap-2 items-center bg-red-300 px-2 py-2 rounded-t-md"
            >
              <svg
                height="20"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 512 512"
              >
                <path
                  fill="#d70018"
                  d="M152 0H154.2C186.1 0 215.7 16.91 231.9 44.45L256 85.46L280.1 44.45C296.3 16.91 325.9 0 357.8 0H360C408.6 0 448 39.4 448 88C448 102.4 444.5 115.1 438.4 128H480C497.7 128 512 142.3 512 160V224C512 241.7 497.7 256 480 256H32C14.33 256 0 241.7 0 224V160C0 142.3 14.33 128 32 128H73.6C67.46 115.1 64 102.4 64 88C64 39.4 103.4 0 152 0zM190.5 68.78C182.9 55.91 169.1 48 154.2 48H152C129.9 48 112 65.91 112 88C112 110.1 129.9 128 152 128H225.3L190.5 68.78zM360 48H357.8C342.9 48 329.1 55.91 321.5 68.78L286.7 128H360C382.1 128 400 110.1 400 88C400 65.91 382.1 48 360 48V48zM32 288H224V512H80C53.49 512 32 490.5 32 464V288zM288 512V288H480V464C480 490.5 458.5 512 432 512H288z"
                ></path>
              </svg>
              <p class="font-bold text-[20px] text-[#d70018]">Khuyến mãi</p>
            </div>
            <div class="px-2 py-2 font-semibold text-[18px]">
              Khuyến mãi đến 100% khi mua đơn hàng có giá trị trên 1 tr đồng
            </div>
          </div>
          <button
            v-on:click="
              counter.F_them_vao_gio_hang(
                counter.gio_hang_chi_tiet.id,
                counter.san_pham_chi_tiet.id
              )
            "
            class="flex flex-col bg-red-500 hover:bg-red-700 items-center gap-2 justify-center w-full rounded-md border-[2px] border-[#e04040] py-2"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              height="30"
              viewBox="0 0 576 512"
            >
              <path
                fill="white"
                d="M0 24C0 10.7 10.7 0 24 0H69.5c22 0 41.5 12.8 50.6 32h411c26.3 0 45.5 25 38.6 50.4l-41 152.3c-8.5 31.4-37 53.3-69.5 53.3H170.7l5.4 28.5c2.2 11.3 12.1 19.5 23.6 19.5H488c13.3 0 24 10.7 24 24s-10.7 24-24 24H199.7c-34.6 0-64.3-24.6-70.7-58.5L77.4 54.5c-.7-3.8-4-6.5-7.9-6.5H24C10.7 48 0 37.3 0 24zM128 464a48 48 0 1 1 96 0 48 48 0 1 1 -96 0zm336-48a48 48 0 1 1 0 96 48 48 0 1 1 0-96zM252 160c0 11 9 20 20 20h44v44c0 11 9 20 20 20s20-9 20-20V180h44c11 0 20-9 20-20s-9-20-20-20H356V96c0-11-9-20-20-20s-20 9-20 20v44H272c-11 0-20 9-20 20z"
              />
            </svg>
            <p class="font-medium text-[18px] text-white">Thêm vào giỏ hàng</p>
          </button>
        </div> -->
      </div>
      <button
        v-on:click="
          counter.F_them_vao_gio_hang(
            counter.gio_hang_chi_tiet.id,
            counter.san_pham_chi_tiet.id
          )
        "
        class="flex w-[300px] mt-3 bg-red-500 hover:bg-red-700 items-center gap-2 justify-center rounded-md border-[2px] border-[#e04040] py-2"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          height="20"
          viewBox="0 0 576 512"
        >
          <path
            fill="white"
            d="M0 24C0 10.7 10.7 0 24 0H69.5c22 0 41.5 12.8 50.6 32h411c26.3 0 45.5 25 38.6 50.4l-41 152.3c-8.5 31.4-37 53.3-69.5 53.3H170.7l5.4 28.5c2.2 11.3 12.1 19.5 23.6 19.5H488c13.3 0 24 10.7 24 24s-10.7 24-24 24H199.7c-34.6 0-64.3-24.6-70.7-58.5L77.4 54.5c-.7-3.8-4-6.5-7.9-6.5H24C10.7 48 0 37.3 0 24zM128 464a48 48 0 1 1 96 0 48 48 0 1 1 -96 0zm336-48a48 48 0 1 1 0 96 48 48 0 1 1 0-96zM252 160c0 11 9 20 20 20h44v44c0 11 9 20 20 20s20-9 20-20V180h44c11 0 20-9 20-20s-9-20-20-20H356V96c0-11-9-20-20-20s-20 9-20 20v44H272c-11 0-20 9-20 20z"
          />
        </svg>
        <p class="font-medium text-[18px] text-white">Thêm vào giỏ hàng</p>
      </button>
      <!-- <div
        class="rounded-md border-[1px] border-gray-[#e5e7eb] px-1 py-1 w-full"
      >
        <p class="py-2 font-bold text-[20px]">Gợi ý sản phẩm</p>
        <div class="grid grid-cols-9 gap-2 w-full">
          <div
            class="shadow-md relative cursor-pointer rounded-md h-[135px] bg-cover bg-center bg-[url('https://cdn11.dienmaycholon.vn/filewebdmclnew/public/userupload/files/dien-thoai-camera-tot-nhat-1.png')]"
            @mouseover="showText(index)"
            @mouseleave="hideText(index)"
          >
            <p
              class="absolute bottom-[140px] left-0 px-2 py-1 bg-white border-[1px] rounded-md border-gray-700 text-[14px] font-normal"
            >
              Chuột
            </p>
          </div>
        </div>
      </div> -->
      <p class="py-4 font-bold text-[20px]">Sản phẩm gợi ý</p>
      <div class="grid grid-cols-5 gap-4 w-full">
        <router-link
          :to="`/chi-tiet/${i.id}`"
          v-for="(i, index) in counter.danh_sach_san_pham_ai"
          :key="index"
          v-on:click="counter.F_chi_tiet_san_pham(i.id)"
          class="shadow-md flex flex-col items-center rounded-md py-2 px-2 hover:scale-105 cursor-pointer bg-white"
        >
          <div class="px-2">
            <img :src="counter.Domain_Backend + i.Avatar" />
          </div>
          <p class="font-bold text-[20px] text-slate-600 w-full">
            {{ i.Name }}
          </p>
          <div class="flex gap-2 w-full">
            <p class="text-[18px] text-red-500 font-semibold">
              {{ i.Price_has_decreased }}₫
            </p>
            <div class="w-full flex items-center justify-start font-semibold">
              <div class="relative">
                <p class="">{{ i.Price }}₫</p>
                <div
                  class="h-[0px] w-full border-[1px] border-slate-700 absolute top-[10px]"
                ></div>
              </div>
            </div>
          </div>
          <div class="flex items-center justify-between w-full">
            <div class="flex gap-1 items-center">
              <svg
                v-for="(i, index) in 5"
                :key="index"
                xmlns="http://www.w3.org/2000/svg"
                height="16"
                width="18"
                viewBox="0 0 576 512"
              >
                <path
                  fill="orange"
                  d="M316.9 18C311.6 7 300.4 0 288.1 0s-23.4 7-28.8 18L195 150.3 51.4 171.5c-12 1.8-22 10.2-25.7 21.7s-.7 24.2 7.9 32.7L137.8 329 113.2 474.7c-2 12 3 24.2 12.9 31.3s23 8 33.8 2.3l128.3-68.5 128.3 68.5c10.8 5.7 23.9 4.9 33.8-2.3s14.9-19.3 12.9-31.3L438.5 329 542.7 225.9c8.6-8.5 11.7-21.2 7.9-32.7s-13.7-19.9-25.7-21.7L381.2 150.3 316.9 18z"
                />
              </svg>
            </div>
            <div class="flex gap-1 items-center">
              <p>Yêu thích</p>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                height="16"
                width="16"
                viewBox="0 0 512 512"
              >
                <path
                  fill="red"
                  d="M225.8 468.2l-2.5-2.3L48.1 303.2C17.4 274.7 0 234.7 0 192.8v-3.3c0-70.4 50-130.8 119.2-144C158.6 37.9 198.9 47 231 69.6c9 6.4 17.4 13.8 25 22.3c4.2-4.8 8.7-9.2 13.5-13.3c3.7-3.2 7.5-6.2 11.5-9c0 0 0 0 0 0C313.1 47 353.4 37.9 392.8 45.4C462 58.6 512 119.1 512 189.5v3.3c0 41.9-17.4 81.9-48.1 110.4L288.7 465.9l-2.5 2.3c-8.2 7.6-19 11.9-30.2 11.9s-22-4.2-30.2-11.9zM239.1 145c-.4-.3-.7-.7-1-1.1l-17.8-20c0 0-.1-.1-.1-.1c0 0 0 0 0 0c-23.1-25.9-58-37.7-92-31.2C81.6 101.5 48 142.1 48 189.5v3.3c0 28.5 11.9 55.8 32.8 75.2L256 430.7 431.2 268c20.9-19.4 32.8-46.7 32.8-75.2v-3.3c0-47.3-33.6-88-80.1-96.9c-34-6.5-69 5.4-92 31.2c0 0 0 0-.1 .1s0 0-.1 .1l-17.8 20c-.3 .4-.7 .7-1 1.1c-4.5 4.5-10.6 7-16.9 7s-12.4-2.5-16.9-7z"
                />
              </svg>
            </div>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>
<script>
import { useCounterStore } from "@/stores/counter";
import axios from "axios";
import VueCookies from "vue-cookies";

export default {
  data() {
    return {
      url_image: [],
      url_image_inset: [{ id: 4, Image_post: "", post: 4 }],
      url_image_inset_one: "",
    };
  },
  setup() {
    const counter = useCounterStore();
    return { counter };
  },
  mounted: function () {
    // this.counter.F_chi_tiet_san_pham(this.counter.id_dh);
    this.chi_tiet();
  },
  created() {
    // this.counter.F_chi_tiet_san_pham(this.counter.id_dh);
  },
  computed: {},
  methods: {
    chi_tiet() {
      var x = this.counter.Path_Route.path;
      // Lấy phần cuối cùng sau dấu '/'
      x = x.substring(x.lastIndexOf("/") + 1);
      // Giải mã URL
      x = decodeURIComponent(x);
      this.counter.F_chi_tiet_san_pham(x);
    },
  },
  components: {},
};
</script>

<style>
#cjss::-webkit-scrollbar {
  width: 5px;
  height: 8px; /* Chiều rộng vùng chứa scrollbar */
}
#cjss::-webkit-scrollbar-track {
  background: #1f2937; /* Màu nền ngoài của thanh scrollbar */
}
#cjss::-webkit-scrollbar-thumb {
  background-color: #7dd3fc; /* Màu của thanh cuộn (scroll thumb) */
  border-radius: 1px; /* Bo góc scroll thumb */
  /* border: 2px solid #ccc;  Không hỗ trợ padding, margin, transition nên dùng viền cùng màu nên để padding scroll thumb */
}
#cjss::-webkit-scrollbar-thumb:hover {
  background-color: #e0f2fe; /* Hiệu ứng di chuột đổi màu*/
}

#cjss1::-webkit-scrollbar {
  width: 5px;
  height: 8px; /* Chiều rộng vùng chứa scrollbar */
}
#cjss1::-webkit-scrollbar-track {
  background: #393636; /* Màu nền ngoài của thanh scrollbar */
}
#cjss1::-webkit-scrollbar-thumb {
  background-color: #595857; /* Màu của thanh cuộn (scroll thumb) */
  border-radius: 1px; /* Bo góc scroll thumb */
  /* border: 2px solid #ccc;  Không hỗ trợ padding, margin, transition nên dùng viền cùng màu nên để padding scroll thumb */
}
#cjss1::-webkit-scrollbar-thumb:hover {
  background-color: #655f58; /* Hiệu ứng di chuột đổi màu*/
}

#video {
  transform: rotateY(180deg);
  -webkit-transform: rotateY(180deg); /* Safari and Chrome */
  -moz-transform: rotateY(180deg); /* Firefox */
}
</style>
