<template>
  <div class="flex w-[100%] grow min-h-screen">
    <div class="flex flex-col bg-gray-100 mx-auto max-w-7xl grow px-3 py-3">
      <div class="flex justify-around w-full h-[42px]">
        <button
          v-on:click="counter.bang_nhan_vien = 1"
          :class="{ 'bg-blue-800': counter.bang_nhan_vien === 1 }"
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full h-[42px]"
        >
          Tạo đơn điểm tập kết đích
        </button>
        <button
          v-on:click="counter.bang_nhan_vien = 2"
          :class="{ 'bg-blue-800': counter.bang_nhan_vien === 2 }"
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full h-[42px]"
        >
          Xác nhận đơn điểm tập kết khác
        </button>
        <button
          v-on:click="counter.bang_nhan_vien = 3"
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full h-[42px]"
          :class="{ 'bg-blue-800': counter.bang_nhan_vien === 3 }"
        >
          Tạo đơn điểm giao dịch đích
        </button>
      </div>
      <!-- Bảng theo nút -->
      <div
        class="w-full border-gray-300 py-2 mt-3"
        style="border-top: 2px solid #333"
        v-if="counter.bang_nhan_vien == 1"
      >
        Tạo đơn điểm tập kết đích
      </div>
      <div
        class="w-full border-gray-300 py-2 mt-3"
        style="border-top: 2px solid #333"
        v-if="counter.bang_nhan_vien == 2"
      >
        Xác nhận đơn điểm tập kết khác
      </div>
      <div
        class="w-full border-gray-300 py-2 mt-3"
        style="border-top: 2px solid #333"
        v-if="counter.bang_nhan_vien == 3"
      >
        Tạo đơn điểm giao dịch đích
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
