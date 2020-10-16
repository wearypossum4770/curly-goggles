import fs from "fs";
import FloridaHillNurseryScrapper from "./FloridaHillNurseryScrapper.js";
const writeStream = fs.createWriteStream("../data/florida_hill_nursery.json");

console.log("NO errors!!");

//const {url,product:{name,unit_price,category,other_names,other_names_description,keywords},description:{short,long},vendor:{vendor_sku,inventory},img={primary,secondary},care_instructions:{light_and_water,pest_and_diseases,general_care} = FloridaHillNurseryScrapper

const url =
  "https://floridahillnursery.com/product/red-lady-dwarf-pomegranate-punica-granatum-plants/";

const FloridaHillNursery = () => Array.from(FloridaHillNurseryScrapper(url));
