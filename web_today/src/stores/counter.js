import { defineStore } from "pinia";

import axios from "axios";
import VueCookies from "vue-cookies";
import { fa0 } from "@fortawesome/free-solid-svg-icons";

import { useRoute } from "vue-router";
const Route = useRoute();

export const useCounterStore = defineStore("counter", {
  state: () => {
    return {
      Domain_Backend: "http://127.0.0.1:8000",
      domain_Frontend: "",
      Path_Route: useRoute(),
      id_dh:useRoute().path.split('/')[useRoute().path.split('/').length - 1],

      // Social///////////////////////
      Table_Lg_Rg: 0,
      Form_Lg_R: true,
      Lg: { username: "", password: "" },
      Rg: { username: "", email: "", password: "", confirm_password: "" },
      thong_tin_user: {
        id: "",
        username: "",
        email: "",
        password: "",
        token: "",
      },
      Error_Lg: { so: 1, thong_bao: "" },
      Error_Rg: { so: 1, thong_bao: "" },
      Rg_TC: 1,
      Show_DD_image: false,
      Profile: { id: "", Date_of_birth: "", Address: "", Avatar: "" },
      Edit_Profile: { so: 1, Date_of_birth: "", Address: "", Phone_number: "" },
      Edit_Post: { so: 1, Date_of_birth: "", Address: "" },
      Data_Image: "",
      SL_F: 0,
      Create_Post: { Content: "" },
      examplee: "",
      list_user_post: "",
      show_delete: "",
      list_post_home: "",
      search_friend: "",
      list_search_friend: "",
      all_comments: 0,
      body_comment: "",
      show_delete_comment: 0,
      s_d_p: 0,
      show_image_inset: 0,
      Hair: 1,
      Select_Hair: 0,
      show_delete_post: 0,
      Scan_Hair: 0,
      change_password: { so: 0, thong_bao: "" },
      matkhaucu: "",
      matkhaumoi: "",
      tentaikhoan: "",
      show_change_password: 1,
      Image_base64: "",
      Loading: 1,
      Image_Text: null,
      xacnhan: 1,

      /////////////////////////////////////////////////////////////////////////
      dinh_co: "SLOC",
      Size: "",
      SSD: { PREC: 1.15, FLEX: 1, RESL: 1, TEAM: 1, PMAT: 1 },
      Chi_phi: "",
      EAF: 1,
      SCD: {
        RELY: 1.0,
        DATA: 1.0,
        CPLX: 1.0,
        RUSE: 1.0,
        DOCU: 1.0,
        ACAP: 1.0,
        PCAP: 1.0,
        PCON: 1.0,
        APEX: 1.0,
        PLEX: 1.0,
        LTEX: 1.0,
        PVOL: 1.0,
        TOOL: 1.0,
        SITE: 1.0,
        SCED: 1.0,
        STOR: 1.0,
        TIME: 1.0,
      },
      Data_Calculate: "",
      History_Calculate: [],
      Error_Tab: { so: 0, thongbao: "" },
      ////////////////////////////////////////////////////////////////////////
      Search: "",
      Data_Search: [],
      Data_Device_list: [],
      Device_table: 1,
      If_device: { Name: "", Species: "", Code: "" },
      list_delete: [],
      BTB: "",
      list_select: [],
      data_list_select: [],
      textInput: "",
      model_list_all: [],
      model_Name: "",
      time_start: "",
      time_end: "",
      test_score: "",
      data_dathi: "",
      check_model: 1,
      check_dathi: 1,
      Ten_SV: "",
      Lop_SV: "",
      data_device: { Species: "", Code: "", Name: "", Button: "" },
      Camera: 1,
      Image_Base64: "",
      Data_Feeling: "",
      bang_luu: "",
      MSV: "",
      mach_dau_noi: "",
      kt_mach: "",
      data_GG: "",
      data_xlsx: { status: "", path: "" },
      // Ngoc Khánh
      bang_nhan_vien: 1,
      bang_dang_nhap_dang_ki: 1,
      token: "",
      san_pham_danh_sach: "",
      san_pham_chi_tiet: "",
      khoa_tim_kiem_san_pham: "",
      khoa_loc_san_pham: {danh_muc:'',quoc_gia:'',thuong_hieu:''},
      page_san_pham: 1,
      thuong_hieu_danh_sach: "",
      quoc_gia_danh_sach: "",
      gio_hang_chi_tiet: "",
      danh_sach_don_hang: "",
      lg: { username: "", password: "" },
      dk: { email: "", username: "", password: "" },
      cn: {Name:"",Phone:"",Address:"", email: "",Avatar:"",password:""},
      danh_muc_danh_sach: "",
      thong_tin_tai_khoan:false,
      danh_sach_san_pham_ai:'',
    };
  },

  getters: {
    // cookievalue: (state) => state.thong_tin_user.token + "(Theta)" + state.thong_tin_user.id,
  },

  actions: {
    async dang_ki() {
      try {
        this.thong_tin_user = await axios({
          method: "post",
          url: this.Domain_Backend + "/User/",
          data: this.dk,
        });
      } catch (error) {
        console.log(error);
        this.thong_tin_user = error.response.data;
      }
      this.dk={ email: "", username: "", password: "" };
    },
    async dang_nhap() {
      try {
        this.thong_tin_user = await axios({
          method: "post",
          url: this.Domain_Backend + "/api/token/",
          data: { username: this.lg.username, password: this.lg.password },
        });
        this.thong_tin_user = this.thong_tin_user.data;
        VueCookies.set("mg", this.thong_tin_user.access, "10d");
        this.bang_dang_nhap_dang_ki = 1;
        this.lg = { username: "", password: "" };
        this.token = this.thong_tin_user.access;
        await this.lay_thong_tin_tai_khoan();
        this.gio_hang_chi_tiet = this.thong_tin_user.Cart_User;
        this.danh_sach_don_hang = this.thong_tin_user.Oder_User;
        this.F_Product_AI();
        // if(this.token){
        //   window.location.href = "/gio-hang";
        // }
      } catch (error) {
        console.log(error);
        this.thong_tin_user = error.response.data;
      }
    },
    async dang_xuat() {
      VueCookies.remove("mg");
      this.thong_tin_user = {
        id: "",
        username: "",
        email: "",
        password: "",
        token: "",
      };
      this.token='';
      window.location.href = "/";
    },
    async duy_tri_dang_nhap() {
      this.token = await VueCookies.get("mg");
      this.thong_tin_user = await axios({
        method: "post",
        url: this.Domain_Backend + "/get-user-info/",
        headers: { Authorization: "Bearer " + this.token },
      });
      this.thong_tin_user = this.thong_tin_user.data.user;

      this.cn.Name = this.thong_tin_user.Name
      this.cn.Phone = this.thong_tin_user.Phone
      this.cn.Address = this.thong_tin_user.Address
      this.cn.email = this.thong_tin_user.email

      this.gio_hang_chi_tiet = this.thong_tin_user.Cart_User;
      this.danh_sach_don_hang = this.thong_tin_user.Oder_User;

      this.F_Product_AI();
    },

    async lay_thong_tin_tai_khoan() {
      this.token = await VueCookies.get("mg");
      this.thong_tin_user = await axios({
        method: "post",
        url: this.Domain_Backend + "/get-user-info/",
        headers: { Authorization: "Bearer " + this.token },
      });
      this.thong_tin_user = this.thong_tin_user.data.user;

      this.cn.Name = this.thong_tin_user.Name
      this.cn.Phone = this.thong_tin_user.Phone
      this.cn.Address = this.thong_tin_user.Address
      this.cn.email = this.thong_tin_user.email

      this.gio_hang_chi_tiet = this.thong_tin_user.Cart_User;
      this.danh_sach_don_hang = this.thong_tin_user.Oder_User;

      this.F_Product_AI();
    },

    async F_danh_muc_danh_sach() {
      this.danh_muc_danh_sach = (
        await axios({ method: "get", url: this.Domain_Backend + "/Category/" })
      ).data;
    },

    async F_san_pham_danh_sach() {
      this.san_pham_danh_sach = (
        await axios({
          method: "get",
          url: this.Domain_Backend + "/Product/?page=" + this.page_san_pham,
        })
      ).data;
    },
    async F_tim_kiem_san_pham() {
      this.san_pham_danh_sach = (
        await axios({
          method: "get",
          url:
            this.Domain_Backend +
            "/Product/?search=" +
            this.khoa_tim_kiem_san_pham,
        })
      ).data;
    },
    async F_loc_san_pham(a,b,c) {
      this.san_pham_danh_sach = '';
      this.khoa_loc_san_pham = {
        danh_muc: a,
        quoc_gia: b,
        thuong_hieu: c,
      };
      if(this.khoa_loc_san_pham.danh_muc){
        this.san_pham_danh_sach = (
          await axios({
            method: "get",
            url:
              this.Domain_Backend +
              "/Product/?Category__Name=" +
              this.khoa_loc_san_pham.danh_muc,
          })
        ).data;
      };
      if(this.khoa_loc_san_pham.thuong_hieu){
        this.san_pham_danh_sach = (
          await axios({
            method: "get",
            url:
              this.Domain_Backend +
              "/Product/?Trademark__Name=" +
              this.khoa_loc_san_pham.thuong_hieu,
          })
        ).data;
      };
      if(this.khoa_loc_san_pham.quoc_gia){
        this.san_pham_danh_sach = (
          await axios({
            method: "get",
            url:
              this.Domain_Backend +
              "/Product/?Made__Name=" +
              this.khoa_loc_san_pham.quoc_gia,
          })
        ).data;
      };
    },
    async F_chi_tiet_san_pham(id) {
      this.san_pham_chi_tiet = (
        await axios({
          method: "get",
          url: this.Domain_Backend + "/Product/" + id + "/",
        })
      ).data;
    },

    async F_thuong_hieu_danh_sach() {
      this.thuong_hieu_danh_sach = (
        await axios({ method: "get", url: this.Domain_Backend + "/Trademark/" })
      ).data;
    },
    // async F_tim_kiem_thuong_hieu() {
    //   this.thuong_hieu_danh_sach = (await axios({ method: 'get', url: this.Domain_Backend + '/Trademark/' })).data;
    // },
    // async F_loc_thuong_hieu() {
    //   this.thuong_hieu_danh_sach = (await axios({ method: 'get', url: this.Domain_Backend + '/Trademark/' })).data;
    // },

    async F_quoc_gia_danh_sach() {
      this.quoc_gia_danh_sach = (
        await axios({ method: "get", url: this.Domain_Backend + "/Made/" })
      ).data;
    },
    // async F_tim_kiem_quoc_gia() {
    //   this.quoc_gia_danh_sach = (await axios({ method: 'get', url: this.Domain_Backend + '/province/' })).data;
    // },
    // async F_loc_quoc_gia() {
    //   this.quoc_gia_danh_sach = (await axios({ method: 'get', url: this.Domain_Backend + '/province/' })).data;
    // },

    async F_dang_nhap_gio_hang() {
      if (this.token) {
        window.location.href = "/gio-hang";
      } else {
        this.bang_dang_nhap_dang_ki = 3;
      }
    },

    async F_chi_tiet_gio_hang() {
      this.gio_hang_chi_tiet = (
        await axios({
          method: "get",
          url: this.Domain_Backend + "/Cart/" + this.thong_tin_user.Cart_User.id + "/",
        })
      ).data;
    },
    async F_them_vao_gio_hang(id_cart, id_cart_detail) {
      await axios({
        method: "post",
        url: this.Domain_Backend + "/add_detail_cart/",
        data: { id_cart: id_cart, id_cart_detail: id_cart_detail },
        headers: { Authorization: "Bearer " + this.token }
      });
      this.lay_thong_tin_tai_khoan();
    },
    async F_xoa_khoi_gio_hang(id) {
      await axios({
        method: "delete",
        url: this.Domain_Backend + "/Cart_detail/" + id + "/",
      });
      this.lay_thong_tin_tai_khoan();
    },
    async thay_doi_so_luong_trong_gio_hang(a,b){
      await axios({
        method: "post",
        url: this.Domain_Backend + "/change_amount/",
        data:{id_dk:a,amount:b,id_cart:this.gio_hang_chi_tiet.id},
        headers: { Authorization: "Bearer " + this.token }
      });
      this.lay_thong_tin_tai_khoan();
    },

    // async F_danh_sach_don_hang() {
    //   this.don_hang_danh_sach = (
    //     await axios({ method: "get",
    //     url: this.Domain_Backend + "/Oder/",data:{id_user:this.gio_hang_chi_tiet.id},
    //     headers: { Authorization: "Bearer " + this.token }
    //   })
    //   ).data;
    // },

    async F_dat_hang() {
      await axios({ method: "post",url: this.Domain_Backend + "/add_Oder/",
      data:{id_cart:this.gio_hang_chi_tiet.id,id_user:this.thong_tin_user.id},
      headers: { Authorization: "Bearer " + this.token } })
      this.lay_thong_tin_tai_khoan();
    },

    async F_Product_AI() {
      this.danh_sach_san_pham_ai = await axios({ method: "post",url: this.Domain_Backend + "/list_product_AI/",
      data:{id_user:this.thong_tin_user.id},
      headers: { Authorization: "Bearer " + this.token } });
      this.danh_sach_san_pham_ai = this.danh_sach_san_pham_ai.data
    },
  },
});
