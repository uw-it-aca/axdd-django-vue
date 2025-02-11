import { defineStore } from "pinia";

export const useHelloStore = defineStore("hello", {
  state: () => ({ message: "Hello world, from the Pinia store!" }),
  getters: {},
  actions: {},
});
