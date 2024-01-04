<template>
  <div class="flex w-[100%] grow min-h-screen">
    <div
      v-if="counter.token"
      class="flex flex-col items-center bg-gray-100 mx-auto max-w-7xl grow px-3 py-2"
    >
      <div
        class="grid grid-cols-1 w-[800px] rounded-md border-[1px] border-gray-[#e5e7eb] px-2 py-2 mt-2 bg-white"
      >
        <p
          class="text-green-700 font-bold text-[22px] border-b-[1px] border-green-900 pb-2"
        >
          Thông tin tài khoản '{{ counter.thong_tin_user.username }}'
        </p>
        <div class="flex flex-col gap-3 py-3">
          <div class="flex items-center justify-center">
            <img
              v-if="counter.thong_tin_user.Avatar"
              :src="counter.Domain_Backend + counter.thong_tin_user.Avatar"
              class="w-[150px] h-[150px] rounded-full"
            />
            <img
              v-else
              src="https://cdn-icons-png.flaticon.com/256/3899/3899618.png"
              class="w-[150px] h-[150px] rounded-full"
            />
          </div>
          <div class="flex flex-col gap-1 text-gray-700">
            <p class="text-[18px] font-medium">Tên:</p>
            <input
              v-model="counter.cn.Name"
              class="border-none outline-none px-2 py-1 rounded-md bg-gray-300 font-normal"
            />
          </div>
          <div class="flex flex-col gap-1 text-gray-700">
            <p class="text-[18px] font-medium">Email:</p>
            <input
              v-model="counter.cn.email"
              class="border-none outline-none px-2 py-1 rounded-md bg-gray-300 font-normal"
            />
          </div>
          <div class="flex flex-col gap-1 text-gray-700">
            <p class="text-[18px] font-medium">Số điện thoại:</p>
            <input
              v-model="counter.cn.Phone"
              class="border-none outline-none px-2 py-1 rounded-md bg-gray-300 font-normal"
            />
          </div>
          <div class="flex flex-col gap-1 text-gray-700">
            <p class="text-[18px] font-medium">Địa chỉ:</p>
            <input
              v-model="counter.cn.Address"
              class="border-none outline-none px-2 py-1 rounded-md bg-gray-300 font-normal"
            />
          </div>
          <div class="flex flex-col gap-1 text-gray-700">
            <p class="text-[18px] font-medium">
              Mật khẩu (hãy điền thêm trường này nếu bạn muốn đổi mật khẩu):
            </p>
            <input
              v-model="counter.cn.password"
              class="border-none outline-none px-2 py-1 rounded-md bg-gray-300 font-normal"
            />
          </div>
          <div class="flex flex-col gap-1 text-gray-700">
            <p class="text-[18px] font-medium">
              Chọn ảnh dại diện (hãy chọn thêm ảnh nếu bạn muốn dổi ảnh đại
              diện):
            </p>
            <input
              id="update_user_avatar"
              type="file"
              accept="image/*"
              multiple
              class="border-none outline-none px-2 py-1 rounded-md bg-gray-300 font-normal"
            />
          </div>
          <button
            v-on:click="updateUser()"
            class="bg-green-600 px-2 py-1 rounded-md text-white text-[17px] font-bold w-[150px] hover:bg-green-500"
          >
            Cập nhật
          </button>
        </div>
      </div>
    </div>
    <div
      v-else
      class="flex flex-col justify-center items-center bg-gray-100 mx-auto max-w-7xl grow px-3 py-2"
    >
      <p class="font-medium text-[30px] text-gray-900">
        Đăng nhập để xem thông tin tài khoản của bạn
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
  mounted: function () {
    //   this.counter.F_Device_list();
    //   this.counter.data_list_select=[];
  },
  computed: {},
  methods: {
    updateUser() {
      // Tạo FormData để chứa dữ liệu và các tệp tin
      var formData = new FormData();
      formData.append("Name", this.counter.cn.Name);
      formData.append("Phone", this.counter.cn.Phone);
      formData.append("Address", this.counter.cn.Address);
      formData.append("email", this.counter.cn.email);
      formData.append("password", this.counter.cn.password);

      // Lấy tệp tin Avatar
      var avatarFile = document.getElementById("update_user_avatar").files[0];
      formData.append("Avatar", avatarFile);

      const headers = {
        Authorization: `Bearer ${this.counter.token}`,
        "Content-Type": "multipart/form-data",
      };

      // Gửi dữ liệu đến API bằng axios
      axios
        .patch(
          `${this.counter.Domain_Backend}/User/${this.counter.thong_tin_user.id}/`,
          formData,
          { headers }
        )
        .then((response) => {
          console.log("Success:", response.data);
          this.counter.lay_thong_tin_tai_khoan();
        })
        .catch((error) => {
          console.error("Error:", error);
        });
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
