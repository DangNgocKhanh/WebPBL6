<template>
  <div class="flex w-[100%] grow min-h-screen">
    <div
      v-if="counter.token"
      class="flex flex-col items-center bg-gray-100 mx-auto max-w-7xl grow px-3 py-2"
    >
      <h2 class="text-[22px] font-bold py-2">Giỏ hàng của bạn</h2>
      <div
        v-if="
          counter.gio_hang_chi_tiet &&
          counter.gio_hang_chi_tiet.Cart_detail_Cart
        "
        class="grid grid-cols-1 divide-y w-[600px] rounded-md border-[1px] border-gray-[#e5e7eb] px-2 py-2 mt-2 bg-white"
      >
        <div
          v-for="(i, index) in counter.gio_hang_chi_tiet.Cart_detail_Cart"
          :key="index"
          class="flex justify-between w-full py-2"
        >
          <div class="flex gap-2">
            <img
              :src="counter.Domain_Backend + i.Product.Avatar"
              class="w-[100px]"
            />
            <div class="flex flex-col gap-2">
              <p class="text-[18px] font-bold">
                {{ i.Product ? i.Product.Name : "" }}
              </p>
              <div class="flex items-center gap-2 w-full">
                <p class="text-[18px] text-red-500 font-semibold">
                  {{ i.Product ? i.Product.Price_has_decreased : "" }}₫
                </p>
                <div
                  class="w-full flex items-center justify-start font-semibold"
                >
                  <div class="relative">
                    <p class="text-[19px] font-bold">
                      {{ i.Product ? i.Product.Price : "" }}₫
                    </p>
                    <div
                      class="w-full border-[1px] border-slate-700 absolute top-[10px]"
                    ></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="flex gap-1 items-center">
            <input
              v-model="i.Amount"
              @input="counter.thay_doi_so_luong_trong_gio_hang(i.id, i.Amount)"
              type="number"
              class="bg-transparent rounded-md border-[1px] border-gray-[#e5e7eb] px-1 py-1 w-[60px] h-[30px]"
            />
            <svg
              v-on:click="counter.F_xoa_khoi_gio_hang(i.id)"
              width="30"
              height="30"
              viewBox="0 0 16 16"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
              class="cursor-pointer"
              title="Xóa"
            >
              <path
                d="M13.9999 4H10.6666V2.88666C10.6509 2.45988 10.4667 2.0567 10.1543 1.76553C9.84188 1.47435 9.42675 1.31893 8.99992 1.33333H6.99992C6.57309 1.31893 6.15796 1.47435 5.84554 1.76553C5.53312 2.0567 5.34889 2.45988 5.33325 2.88666V4H1.99992C1.82311 4 1.65354 4.07024 1.52851 4.19526C1.40349 4.32028 1.33325 4.48985 1.33325 4.66666C1.33325 4.84348 1.40349 5.01305 1.52851 5.13807C1.65354 5.26309 1.82311 5.33333 1.99992 5.33333H2.66659V12.6667C2.66659 13.1971 2.8773 13.7058 3.25237 14.0809C3.62744 14.456 4.13615 14.6667 4.66659 14.6667H11.3333C11.8637 14.6667 12.3724 14.456 12.7475 14.0809C13.1225 13.7058 13.3333 13.1971 13.3333 12.6667V5.33333H13.9999C14.1767 5.33333 14.3463 5.26309 14.4713 5.13807C14.5963 5.01305 14.6666 4.84348 14.6666 4.66666C14.6666 4.48985 14.5963 4.32028 14.4713 4.19526C14.3463 4.07024 14.1767 4 13.9999 4ZM6.66659 2.88666C6.66659 2.78 6.80659 2.66666 6.99992 2.66666H8.99992C9.19325 2.66666 9.33325 2.78 9.33325 2.88666V4H6.66659V2.88666ZM11.9999 12.6667C11.9999 12.8435 11.9297 13.013 11.8047 13.1381C11.6796 13.2631 11.5101 13.3333 11.3333 13.3333H4.66659C4.48977 13.3333 4.32021 13.2631 4.19518 13.1381C4.07016 13.013 3.99992 12.8435 3.99992 12.6667V5.33333H11.9999V12.6667Z"
                fill="#212B36"
              ></path>
              <path
                d="M5.99992 11.3333C6.17673 11.3333 6.3463 11.2631 6.47132 11.1381C6.59635 11.013 6.66658 10.8435 6.66658 10.6667V8C6.66658 7.82319 6.59635 7.65362 6.47132 7.5286C6.3463 7.40357 6.17673 7.33334 5.99992 7.33334C5.82311 7.33334 5.65354 7.40357 5.52851 7.5286C5.40349 7.65362 5.33325 7.82319 5.33325 8V10.6667C5.33325 10.8435 5.40349 11.013 5.52851 11.1381C5.65354 11.2631 5.82311 11.3333 5.99992 11.3333Z"
                fill="#212B36"
              ></path>
              <path
                d="M9.99992 11.3333C10.1767 11.3333 10.3463 11.2631 10.4713 11.1381C10.5963 11.013 10.6666 10.8435 10.6666 10.6667V8C10.6666 7.82319 10.5963 7.65362 10.4713 7.5286C10.3463 7.40357 10.1767 7.33334 9.99992 7.33334C9.82311 7.33334 9.65354 7.40357 9.52851 7.5286C9.40349 7.65362 9.33325 7.82319 9.33325 8V10.6667C9.33325 10.8435 9.40349 11.013 9.52851 11.1381C9.65354 11.2631 9.82311 11.3333 9.99992 11.3333Z"
                fill="#212B36"
              ></path>
            </svg>
          </div>
        </div>
      </div>
      <div
        class="flex justify-between w-[600px] rounded-md border-[1px] border-gray-[#e5e7eb] px-2 py-2 mt-2 bg-white"
      >
        <div class="flex flex-col gap-2 w-full">
          <div class="flex gap-2 w-full">
            <p class="text-[18px] font-semibold">Tạm tính :</p>
            <p class="text-[18px] text-red-500 font-semibold">
              {{ counter.gio_hang_chi_tiet.Total_money | formatCurrency }}
              ₫
            </p>
          </div>
          <a
            href="/don-hang-da-dat/"
            class="underline text-green-500 font-medium text-[16px] cursor-pointer"
            >Xem các đơn hàng đã đặt</a
          >
        </div>
        <button
          v-on:click="counter.F_dat_hang()"
          class="w-[300px] rounded-md text-[18px] text-white font-semibold bg-red-500 py-2"
        >
          Đặt hàng
        </button>
      </div>
      <div class="flex flex-col gap-3 scale-75">
        <p class="pt-3 font-bold text-[23px]">Sản phẩm gợi ý</p>
        <div class="grid grid-cols-5 gap-[15px] w-full grow-0">
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
    <div
      v-else
      class="flex flex-col justify-center items-center bg-gray-100 mx-auto max-w-7xl grow px-3 py-2"
    >
      <p class="font-medium text-[30px] text-gray-900">
        Đăng nhập để xem giỏ hàng của bạn
      </p>
      <button
        v-on:click="counter.bang_dang_nhap_dang_ki = 3"
        class="bg-green-500 rounded-md px-2 py-1 font-bold text-[18px] mt-3"
      >
        Đăng nhập ngay
      </button>
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
  filters: {
    formatCurrency(value) {
      // Chuyển đổi giá trị thành số trước khi định dạng
      const numericValue = Number(value);
      if (isNaN(numericValue)) {
        // Nếu không thể chuyển đổi thành số, trả về giá trị gốc
        return value;
      }

      // Sử dụng toLocaleString để định dạng số thành chuỗi với dấu phân tách hàng nghìn là dấu '.'
      return (
        numericValue.toLocaleString("en-US", {
          minimumFractionDigits: 0,
          maximumFractionDigits: 0,
        }) + "₫"
      );
    },
  },
  mounted: function () {
    //   this.counter.F_Device_list();
    //   this.counter.data_list_select=[];
  },
  computed: {},
  methods: {},
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
